.. _aircraftPage:

Aircraft
========

The Aircraft Page is used to configure the settings that depend on your
aircraft. For convenience, you can save the current settings as a new aircraft
in the aircraft library, and you can select an aircraft from the library to load
its settings.


Page Header
-----------

The three-dot-menu in the top right corner of the page header opens a menu with
the following functions.

View Library…
  Open the Aircraft Library Page, where you can select an aircraft from the
  library.

Save to library…
  Save the current aircraft settings as a new aircraft in the aircraft library.


Page Body
---------

The body of the page contains the data entry fields described below.

Aircraft
^^^^^^^^

Name
  Enter a name for your aircraft.


Use cabin pressure...
  If this option is checked, Enroute Flight Navigation will use the pressure
  sensor of your mobile device to measure the pressure altitude and determine
  vertical distances to airspaces. This option is only available if your device
  has a pressure sensor.

.. note:: If available, Enroute Flight Navigation will always use the pressure altitude
   provided by an external traffic data receiver instead of the pressure altitude
   calculated from the pressure sensor of your mobile device.

Precise measurement of pressure altitude is safety critical. Consider the
following before you decide to enable the option "Use cabin pressure...".

- The pressure sensor of your device is probably not certified for use in
  aviation.

- In typical GA aircraft, static pressure and cabin pressure do not necessarily
  agree, with an error depending on airspeed and on the configuration of the
  heating and ventilation systems.

- Do not enable this option unless you convinced yourself that the data provided
  by your sensor is good enough for the intended use.

- Do not rely on data shown in this app.

- Always use an approved altimeter to judge vertical distance to airspaces.

.. warning:: We strongly recommend connecting **Enroute Flight Navigation** to a 
  proper traffic data receiver.  While option "Use cabin pressure..." might have 
  its use for pilots flying balloons, paragliders or gyrocopters, think twice 
  before using it in a motorized plane or glider. 


Units
^^^^^

Select the units you want to use for horizontal and vertical distances, and fuel
volume.


True airspeed
^^^^^^^^^^^^^

Enter typical values for the aircraft's true airspeed.

Cruise 
  This speed is used to calculate estimated time enroute (ETE) and estimated
  time of arrival (ETA) for your route.

Descent
  This speed is currently not used. It will be used in future versions to
  improve the accuracy of ETE and ETA calculations.

Minimum
  This speed is used to determine whether your aircraft is flying or not.


Fuel Consumption
^^^^^^^^^^^^^^^^

Enter a typical value for the aircraft's fuel consumption. This value is used to
calculate a very rough estimate of the fuel required for your route.

Transponder Code
^^^^^^^^^^^^^^^^
  Enter your aircraft's ICAO 24-bit address (e.g., "3D1C11") or OGN source ID 
  (e.g., "ICA3D1C11", "FLR123456"). This identifier is used to filter out your 
  own aircraft when receiving traffic data from the Open Glider Network, preventing 
  it from being displayed twice on the map.
  
  You can enter multiple codes separated by spaces if your aircraft has multiple 
  identifiers. The comparison is case-insensitive.
  
  .. note:: This field is primarily used for OGN traffic filtering. If you don't 
     use OGN traffic data, you can leave this field empty.

  **How to find your transponder code:**
  
  When your aircraft is visible in the traffic data (for example, when flying with 
  OGN coverage), you can find your transponder code as follows:
  
  1. Open the main menu and navigate to "Information" → "Traffic Receiver"
  2. Look at the list of received traffic
  3. Find your own aircraft in the list (identified by position or callsign)
  4. Note the ID shown for your aircraft
  5. The last 6 characters of the ID are typically your transponder code
  
  For example, if the ID shows "ICA3D1C11", your transponder code is "3D1C11". 
  You can enter either the full ID or just the 6-digit code.

