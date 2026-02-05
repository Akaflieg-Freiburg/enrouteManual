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
  Enter the callsign of your aircraft. Together with the Hex ID, the name is
  used to filter out your own aircraft when receiving traffic data from the Open
  Glider Network, preventing it from being displayed twice on the map.

Hex ID
  Enter the "ICAO 24-bit address" of your transponder (e.g., "3D1C11"), the
  "FLARM Radio ID" of your FLARM device (e.g., "3EDE26") or the "Open Glider
  Network Source ID" of your aircraft (e.g., "ICA3D1C11", "FLR123456"). Together
  with the name, this identifier is used to filter out your own aircraft when
  receiving traffic data from the Open Glider Network, preventing it from being
  displayed twice on the map. If you do not use Open Glider Network traffic
  data, you can leave this field empty.
  
  You can enter multiple codes separated by spaces if your aircraft has multiple
  identifiers. The comparison is case-insensitive.
  
  .. note::

    The ICAO 24-bit address of your transponder is found in the aircraft
    documents. Many transponders show the ICAO 24-bit address on their display
    on startup.  If you have a FLARM device, the FLARM Radio ID is typically
    found in the configuration files written to a connected SD card. If you
    FLARM device can be configured via a web interface, you may also find the
    Radio ID there.
    
    Failing everything else, you can also find the ID the traffic data shown by
    **Enroute Flight Navigation** (for example, when flying in a region with
    Open Glider Network coverage and sufficient internet connectivity). Proceed
    as follows:
    
    1. Open the main menu and navigate to "Information" → "Traffic Receiver"
    2. Look at the list of received traffic
    3. Find your own aircraft in the list (identified by position or callsign)
    4. Note the ID shown for your aircraft
    5. The last 6 characters of the ID are typically your transponder code
    
    For example, if the ID shows "ICA3D1C11", your transponder code is "3D1C11".
    You can enter either the full ID or just the 6-digit code.

  
Use cabin pressure...
  If this option is checked, Enroute Flight Navigation will use the pressure
  sensor of your mobile device to measure the pressure altitude and determine
  vertical distances to airspaces. This option is only available if your device
  has a pressure sensor.

  If available, Enroute Flight Navigation will always use the pressure altitude
  provided by an external traffic data receiver instead of the pressure altitude
  calculated from the pressure sensor of your mobile device.

  .. warning:: 

    Precise measurement of pressure altitude is safety critical. We strongly
    recommend connecting **Enroute Flight Navigation** to a proper traffic data
    receiver.  While option "Use cabin pressure..." might have its use for
    pilots flying balloons, paragliders or gyrocopters, think twice before using
    it in a motorized plane or glider. 

    Consider the following before you decide to enable this option.

    - The pressure sensor of your device is probably not certified for use in
      aviation.
    
    - In typical GA aircraft, static pressure and cabin pressure do not
      necessarily agree, with an error depending on airspeed and on the
      configuration of the heating and ventilation systems.
    
    - Do not enable this option unless you convinced yourself that the data
      provided by your sensor is good enough for the intended use.
    
    - Do not rely on data shown in this app.
    
    - Always use an approved altimeter to judge vertical distance to airspaces.


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

