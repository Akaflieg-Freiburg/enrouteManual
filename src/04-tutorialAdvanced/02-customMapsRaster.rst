.. _rasterMaps:

Raster Maps
===========

**Enroute Flight Navigation** comes with a set of general-purpose base maps in
vector format, which are shown together with the aviation data in a style that
we consider suitable for most aviation purposes.  Still, there might be
situations where a user would like to see a different map.

- Many pilots prefer to fly with the official VFR or ICAO chart of their
  country, which they know from printed charts and from flight training.
- Some users might prefer raster maps that follow a different style.

**Enroute Flight Navigation** can show raster maps on top of the base map.
There are two ways to get raster maps onto your device.

- For many countries, we offer raster charts for download, right next to the
  aviation maps.  The charts are installed and updated like any other map, and no
  further action is required on your part.  The section :ref:`rasterDownload`
  explains the details.

- You can import your own raster maps in MBTILES format, as explained in the
  section :ref:`importRaster`.

.. note::
  Even if you decide to use raster maps, we still recommend installing our
  regular maps, because **Enroute Flight Navigation** needs the data to provide
  airspace and waypoint information.


.. _rasterDownload:

Download Raster Charts
----------------------

For many European countries, we distribute the VFR charts published by the
`open flightmaps <https://www.openflightmaps.org>`_ project.  These charts follow
the familiar style of the official ICAO charts and cover, among others, Austria,
France, Germany, Italy, Poland, Sweden and Switzerland.  The charts are updated
with every AIRAC cycle, that is, every 28 days.  In addition, we distribute the
official ICAO charts for France and Switzerland and the Swiss glider chart.  The
section :ref:`rasterData` lists all charts that are currently available, and the
section :ref:`licensePage` describes the licenses under which the charts are
distributed.

To install a chart, open the main menu and go to "Library/Maps and Data".  The
page "Map and Data Library" will then open.  Its "Maps" tab lists the available
maps by continent; the raster charts appear next to the aviation and base maps
of the respective country, with names such as "Germany VFR Chart (open
flightmaps)" or "Switzerland ICAO Chart".  Tap on the download button to install
a chart.

Once installed, the charts are available immediately.  Like all other maps, they
are updated automatically whenever you update your maps, and they can be
uninstalled on the page "Map and Data Library".

.. note::
  The downloaded charts are provided for information only.  Always check the
  official publications of the national aeronautical information services
  before you fly.


.. _importRaster:

Import Custom Raster Maps
-------------------------

If we do not offer a raster chart for your region, or if you prefer a chart from
a different source, you can import your own maps.  **Enroute Flight Navigation**
is able to import MBTILES files containing raster data.


MBTILES Map Data Sources
........................

The website `open flightmaps <https://www.openflightmaps.org>`_ provides
excellent aviation maps in raster format for a variety of European countries, as
well as South Africa and Namibia.  Most of these maps can be downloaded
directly within the app, as explained in the section :ref:`rasterDownload`.  We
are also aware of aviation authorities that offer ICAO raster maps in GeoTIFF
format. The Section :ref:`mapconversiontools` explains how these can be
converted to the MBTILES format suitable for **Enroute Flight Navigation**.


Import Raster Maps
..................

Transfer the MBTILES file to your device and open the file on your device.  The
Section :ref:`importData` explains the process in detail.


Manage Raster Maps
------------------

To manage the raster maps installed in **Enroute Flight Navigation**, whether
downloaded or imported, open the main menu and go to "Library/Maps and Data".


Use Raster Maps
---------------

.. |ico1| image:: ../01-gettingStarted/ic_layers.png

As soon as raster maps are installed, a button with the label |ico1| will become
visible on the moving map page.  A tap on the button will open the Raster Map
Menu, which shows all raster maps installed.  Tap on an entry to show the
relevant map inside the moving map display.  Tap on the same entry again to hide
it.

.. note::
  In order to avoid confusion, at most one raster map will be shown at any given
  time.
