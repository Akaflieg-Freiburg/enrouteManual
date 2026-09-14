Import Airspace Data
====================

**Enroute Flight Navigation** comes with a set of aviation maps that cover large
parts of the world and are updated frequently. In addition, users can import
airspace data in standard `OpenAir
<http://www.winpilot.com/usersguide/userairspace.asp>`_ format and in the binary
`CUB <https://github.com/naviter/seeyou_file_formats>`_ format used by Naviter
and LXNav products, such as SeeYou and the LX9000. Aviation clubs
and airfield operators use this feature to distribute airspace files to their
members to highlight noise-sensitive areas or airspaces available by local
agreement, or to describe wave windows.

Airspaces defined in imported data will be shown in addition to the standard
aviation maps included with **Enroute Flight Navigation**.  Imported airspaces
are drawn in the same style as the airspaces of the standard maps.  OpenAir
files specify the airspace class in the record "AC" and, optionally, a more
specific airspace type in the record "AY".  **Enroute Flight Navigation**
understands the airspace classes A to G, as well as the airspace types commonly
found in OpenAir files: control zones (CTR), aerodrome traffic zones (ATZ),
radio and transponder mandatory zones (RMZ, TMZ), traffic information areas and
zones (TIA, TIZ), flight information regions and services (FIR, FIS), gliding
sectors (GSEC), and prohibited, restricted and danger areas (P, R, Q).  The
type may be given in the record "AY" or, as in older files, in the record "AC".
Airspaces of any other class or type are drawn as generic special use airspace.

To import airspace data, transfer the OpenAir or CUB file to your device and
open the file on your device.  The Section :ref:`importData` explains the
process in detail.

.. note:: **Enroute Flight Navigation** has no way to represent activation
    times.  Activation times found in OpenAir or CUB files are ignored, and the
    airspaces are shown at all times.  When importing an OpenAir file that
    specifies activation times, the app shows a warning, so that seasonal
    airspace is not mistaken for permanent airspace.  NOTAM-defined airspaces
    found in CUB files are ignored as well.

To view and manage your maps, open the main menu and go to "Library/Maps and
Data".
