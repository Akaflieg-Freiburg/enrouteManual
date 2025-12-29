#!/usr/bin/env python3
"""
Generate a forwarding HTML file for Sphinx documentation anchors.
Scans HTML files recursively and creates forward.html for stable anchor links.
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser
from typing import Dict, Set
import json


class AnchorExtractor(HTMLParser):
    """Extract anchors (id attributes) from HTML."""
    
    # Common Sphinx/theme-generated anchors to ignore
    IGNORE_ANCHORS = {
        'rtd-search-form', 'searchbox', 'search-documentation',
        'navigation', 'main-content', 'page-content', 'sidebar',
        'site-navigation', 'breadcrumbs', 'page-navigation',
        'mobile-nav', 'nav-menu', 'page-top', 'footer',
        'header', 'searchresults', 'navbar', 'toc'
    }
    
    # Prefixes for theme/UI-related anchors to ignore
    IGNORE_PREFIXES = (
        'rtd-', 'nav-', 'mobile-', 'sidebar-', 'header-',
        'footer-', 'menu-', 'toggle-', 'search-'
    )
    
    def __init__(self):
        super().__init__()
        self.anchors: Set[str] = set()
        self.in_section = False
        self.current_tag = None
    
    def handle_starttag(self, tag, attrs):
        """Extract id attributes from content tags only."""
        self.current_tag = tag
        attrs_dict = dict(attrs)
        anchor_id = attrs_dict.get('id', '')
        
        if not anchor_id:
            return
        
        # Skip common UI/navigation anchors
        if anchor_id in self.IGNORE_ANCHORS:
            return
        
        # Skip anchors with ignored prefixes
        if any(anchor_id.startswith(prefix) for prefix in self.IGNORE_PREFIXES):
            return
        
        # Accept anchors from content elements:
        # - Section tags (div.section is common in Sphinx)
        # - Heading tags (h1-h6)
        # - Definition lists (dl, dt)
        # - Code blocks and literals (pre, code with ids)
        # - Figures and tables
        # - Explicit Sphinx reference targets (span with id)
        
        classes = attrs_dict.get('class', '').split()
        
        is_content_anchor = (
            tag in ('section', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 
                   'dt', 'dl', 'figure', 'table', 'span', 'div', 'p') and
            ('section' in classes or 
             tag.startswith('h') or 
             tag in ('dt', 'figure', 'table') or
             'target' in classes or
             'std' in classes or
             tag == 'span')  # Sphinx reference targets
        )
        
        if is_content_anchor:
            self.anchors.add(anchor_id)


def scan_html_files(root_dir: str = '.') -> Dict[str, str]:
    """
    Recursively scan directory for HTML files and extract anchors.
    
    Returns:
        Dict mapping anchor names to relative file paths
    """
    anchor_map = {}
    root_path = Path(root_dir).resolve()
    
    # Find all HTML files
    html_files = list(Path(root_dir).rglob('*.html'))
    
    print(f"Found {len(html_files)} HTML files")
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract anchors
            parser = AnchorExtractor()
            parser.feed(content)
            
            # Get relative path from root - resolve the file path first
            html_file_resolved = html_file.resolve()
            rel_path = html_file_resolved.relative_to(root_path)
            
            # Store anchor mappings
            for anchor in parser.anchors:
                if anchor in anchor_map:
                    print(f"Warning: Duplicate anchor '{anchor}' in {rel_path} "
                          f"(already in {anchor_map[anchor]})")
                anchor_map[anchor] = str(rel_path)
            
            if parser.anchors:
                print(f"  {html_file.name}: {len(parser.anchors)} anchors")
        
        except Exception as e:
            print(f"Error processing {html_file}: {e}")
    
    return anchor_map


def generate_forwarding_html(anchor_map: Dict[str, str], output_file: str = 'forward.html'):
    """
    Generate the forwarding HTML file.
    
    Args:
        anchor_map: Dictionary mapping anchors to file paths
        output_file: Name of the output HTML file
    """
    # Convert anchor map to JSON for embedding
    anchor_json = json.dumps(anchor_map, indent=2)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anchor Forwarding</title>
    <style>
        body {{
            font-family: system-ui, -apple-system, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            line-height: 1.6;
        }}
        .error {{
            background: #fee;
            border: 1px solid #fcc;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .info {{
            background: #eef;
            border: 1px solid #ccf;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        code {{
            background: #f5f5f5;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <h1>Anchor Forwarding</h1>
    <div id="message" class="info">
        <p><strong>Loading...</strong></p>
        <p>If you are not redirected automatically, please check the URL.</p>
    </div>

    <script>
        // Anchor map embedded from Python script
        const anchorMap = {anchor_json};
        
        // Get the anchor from the URL
        const hash = window.location.hash.substring(1); // Remove the '#'
        
        if (!hash) {{
            document.getElementById('message').innerHTML = `
                <p><strong>No anchor specified</strong></p>
                <p>Usage: <code>forward.html#anchorname</code></p>
                <p>Found ${{Object.keys(anchorMap).length}} anchors in the documentation.</p>
                <p>Redirecting to index.html...</p>
            `;
            setTimeout(() => {{ window.location.href = 'index.html'; }}, 2000);
        }} else if (anchorMap[hash]) {{
            // Redirect to the file containing this anchor
            const targetUrl = anchorMap[hash] + '#' + hash;
            document.getElementById('message').innerHTML = `
                <p>Redirecting to: <code>${{targetUrl}}</code></p>
            `;
            window.location.href = targetUrl;
        }} else {{
            // Anchor not found - redirect to index.html
            document.getElementById('message').className = 'error';
            document.getElementById('message').innerHTML = `
                <p><strong>Anchor not found: <code>${{hash}}</code></strong></p>
                <p>The anchor you're looking for does not exist in the documentation.</p>
                <p>Redirecting to index.html...</p>
            `;
            setTimeout(() => {{ window.location.href = 'index.html'; }}, 2000);
        }}
    </script>
</body>
</html>"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\nGenerated {output_file} with {len(anchor_map)} anchors")


def main():
    """Main execution function."""
    print("Sphinx Anchor Forwarding Generator")
    print("=" * 50)
    
    # Scan for anchors
    print("\nScanning HTML files...")
    anchor_map = scan_html_files()
    
    if not anchor_map:
        print("\nNo anchors found! Make sure you're running this in a directory with HTML files.")
        return
    
    # Generate forwarding file
    print("\nGenerating forwarding HTML...")
    generate_forwarding_html(anchor_map)
    
    print("\nDone! You can now use: forward.html#anchorname")
    print(f"Total anchors mapped: {len(anchor_map)}")


if __name__ == '__main__':
    main()
