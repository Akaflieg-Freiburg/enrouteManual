Connect via USB
===============

**Enroute Flight Navigation** is able to connect to your traffic data receiver
using USB connections. Compared with Wi-Fi, USB connections are equally
reliable, but require a bit of manual configuration. By nature, USB supports
only point-to-point connections, so that only one single app can access traffic
data at any given time.  Pilots and co-pilots must therefore decide who gets to
see traffic data.

.. note:: **Enroute Flight Navigation** expects a stream for FLARM/NMEA sentences
    from the USB.

.. note:: USB communication is not available on iPhone or iPad devices. 


One-time Setup
--------------

Step 0: Before You Connect
^^^^^^^^^^^^^^^^^^^^^^^^^^

Before you try to connect this app to your traffic receiver, make sure that the
following conditions are met.

- The hardware is set up. You know the communication parameters of your device,
  depending on the hardware in use, this might be the baud rate.
- Your traffic receiver is switched on and broadcasts FLARM/NMEA via its USB
  connection. 
- No other app on your device uses the USB connection.


Step 1: Configure a Data Connection to the USB Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the steps described in the Section :ref:`SettingsDataConnectionsPage`.
You will need to know or guess the name of the USB device on your device.


Step 2: Check Connectivity
^^^^^^^^^^^^^^^^^^^^^^^^^^

After the data connection to the USB device has been configured in Step 1,
everything else should be automatic.  To check, open the main menu and navigate
to the "Information" menu.  If the entry "Traffic Receiver" is highlighted in
green, then **Enroute Flight Navigation** has already found the traffic receiver
and has connected to it. Congratulations, you are done!

If the entry "Traffic Receiver" is not highlighted in green, then something has
gone wrong.  


Daily Operations
----------------

Once things are set up properly, your device should automatically connect to the
traffic data stream whenever you go flying.  We recommend the following
procedure.

- Connect your device to the USB cable if not connected already.
- After you power on the avionics and the traffic receiver has booted, start
  **Enroute Flight Navigation**.
- **Enroute Flight Navigation** will connect to your traffic data receiver via
  the configured USB connection and show traffic information in the moving map.
- If the data connection gets lost in mid-flight, **Enroute Flight Navigation**
  will automatically try to re-connect.
