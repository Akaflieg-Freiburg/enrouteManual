Connect via Bluetooth
=====================

**Enroute Flight Navigation** to your traffic data receiver using the Bluetooth Classic radio standard.  
Compared with Wi-Fi, Bluetooth connections are less reliable and require manual configuration.  
Bluetooth Classic supports only point-to-point connections, so that only one single app
can access traffic data at any given time.  Pilots and co-pilots must 
therefore decide who gets to see traffic data and configure their devices appropriately.

.. note:: At present, **Enroute Flight Navigation** supports only Bluetooth Classic
    communication. Bluetooth Low Energy may be supported in the future if there is
    sufficient demand from the user community.

.. note:: Access to Bluetooth radio is severely limited on iOS platforms. For that reason,
    Bluetooth communication is not supported at all on iPhone or iPad devices. 


One-time Setup
--------------

Step 0: Before You Connect
^^^^^^^^^^^^^^^^^^^^^^^^^^

Before you try to connect this app to your traffic receiver, make sure that the
following conditions are met.

- Your traffic receiver supports Bluetooth Classic radio. 
- You know the Bluetooth name of your traffic receiver.
- Bluetooth is switched on in your phone.
- Bluetooth is switched on in your traffic data receiver and set to 'discoverable mode'.



Step 1: Configure a Data Connection to the Bluetooth Classic Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the steps described in the Section :ref:`SettingsDataConnectionsPage`.


Step 2: Check Connectivity
^^^^^^^^^^^^^^^^^^^^^^^^^^

After your device has entered the traffic receiver's Wi-Fi network in Step 1,
everything else should be automatic.  To check, open the main menu and navigate
to the "Information" menu.  If the entry "Traffic Receiver" is highlighted in
green, then **Enroute Flight Navigation** has already found the traffic receiver
in the network and has connected to it. Congratulations, you are done!

If the entry "Traffic Receiver" is not highlighted in green, then something has
gone wrong.  The section "Troubleshooting" below might help you find the issue.


Daily Operations
----------------

Once things are set up properly, your device should automatically detect the
traffic receiver's Wi-Fi network, enter the network and connect to the traffic
data stream whenever you go flying.  Here is a breakdown of what will happen.

- As soon as you board your aircraft and power on the avionics, the traffic
  receiver's Wi-Fi network will become visible to your device.
- In a typical scenario, your device might already be connected to a Wi-Fi in a
  nearby building. In that case, nothing will happen for the moment.  As you
  taxi to the runway, your device leaves the range of that network and
  automatically connects to the traffic receiver's Wi-Fi network as the next
  best alternative.
- Traffic information will be shown in the moving map.


Troubleshooting
---------------

The app cannot connect to the traffic data stream
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the main menu and navigate to the "Information" menu.  If the entry
"Traffic Receiver" is not highlighted in green, then **Enroute Flight
Navigation** does not receive any traffic data or traffic data receiver
heartbeat.  Work through the following steps to identify the issue.

**Step 1: Check Wi-Fi** 

Open the Wi-Fi settings of your device and confirm that your device is indeed
connected to the traffic data receiver's network.  If not, then reconnect.  It
might help move your device closer to the traffic data receiver's Wi-Fi antenna.

Some traffic data receivers offer a web-interface that can be accessed with your
web browser.  In that case, check if you can access the web-interface with your
browser.  Close the web browser afterwards, because some devices cannot
concurrently operate the web interface and transmit traffic data.

**Step 2: Check Connection** 

If you are sure that your device has connected to the correct Wi-Fi network,
then return to **Enroute Flight Navigation** open the main menu and go to
"Settings/Data Connections".  Look at the connections of type "TCP" and "UDP".

If none of the TCP/UDP connections has status "Connected", then **Enroute Flight
Navigation** cannot see your traffic data receiver in the Wi-Fi network.  This
means that your traffic data receiver is not available at any of the standard IP
address/Port combinations known to **Enroute Flight Navigation**.

Check the manual of your traffic data receiver or Wi-Fi interface and note the
IP address and port that the traffic data receiver uses.  Go back to **Enroute
Flight Navigation** and check that the combination of IP address and port
appears in the list of data connections.  

If a data connection for that IP address and port exists but cannot connect,
then there is a communication issue that we cannot resolve. It might be
interesting to check if another app is able to communicate with your traffic
data receiver.  If a data connection for that IP address and port does not
exist, then please do the following.

- Contact us! We want to support all traffic data receivers on the market, and
  we will be glad to support your traffic data receiver as well. Return to the
  main moving map screen of **Enroute Flight Navigation**, open the main menu
  and go to "Bug Report".

- Check if your traffic data receiver can be configured to use one of the
  supported IP address/port combinations.

**Step 3: [Censored Profanity]** 

If **Enroute Flight Navigation** has connected to your traffic data receiver via
a TCP/UDP connections but does not receive heartbeat of traffic data, then you
are out of luck. Please contact us, as we would like to hear about your case.
Return to the main moving map screen of **Enroute Flight Navigation**, open the
main menu and go to "Bug Report".  It might be worth checking if other apps
experience similar problems.

  
The connection breaks down frequently
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two common causes for unstable connections.


**Limitations of your Traffic Data Receiver**

Some traffic receivers and some Wi-Fi adaptors cannot serve more than one client
concurrently and abort connections at random if more than one device tries to
access.

- Make sure that there no second device connected to the traffic receiver's
  Wi-Fi network. The other device might well be in your friend's pocket!
- Make sure that there is no other app trying to connect to the traffic
  receiver's data stream.
- Many traffic receivers offer "configuration panels" that can be accessed via a
  web browser. Close all web browsers.


**Electromagnetic Interference**

Electromagnetic interference is a major problem in many avionics installations.
This is not easily solved.  Try moving your device closer to the Wi-Fi antenna
and try to install the antenna in other locations.