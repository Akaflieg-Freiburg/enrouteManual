.. _mappingTools:

Mapping Tools
=============

**Enroute Flight Navigation** is able to import location information ("Map Pins") from
popular mapping tools. This feature has been requested by helicopter pilots working in medical
evacuation, rescue and police operations.  It can also be used by general aviation pilots
who would like to add landmarks ("Hohenzollern Castle") to their flight routes or to their
waypoint library.

.. note:: 
  The functionality described here is only available in version 2.30.9 or later. At the time 
  of writing, the functionality is only available on the Android and Linux/Desktop
  platforms.

.. note:: 
  After a change in Google's policies in early 2025, it is no longer possible to share 
  locations from Google Maps with **Enroute Flight Navigation**. We recommend using one of 
  the other mapping tools described below.


HERE WeGo (Android App)
-----------------------

To share locations from the app `HERE WeGo
<https://play.google.com/store/apps/details?id=com.here.app.maps&hl=de&gl=US>`_
with **Enroute Flight Navigation**, proceed as follows.

- Open the App "Here WeGo" and mark a location by tapping into the moving map. A 
  dialog with location information will open at the bottom of the screen.

- Click on the button "Share".

- You will be presented with a list of contacts and apps that you can share the location
  with. Choose **Enroute Flight Navigation** from this list. If **Enroute Flight 
  Navigation** is not listed, it might be necessary to use the button "More" to present
  an extended list of apps that are able to accept Google Map Share.

- **Enroute Flight Navigation** will open. Depending on the precise form of the data
  shared, one of the following things will happen.
  
  - **Enroute Flight Navigation** will open a waypoint description dialog for the 
    location marked by Google Maps.  As usual, use this dialog to add the location 
    to your route or to the waypoint library.

  - **Enroute Flight Navigation** cannot immediately determine the geographic coordinates
    of the location from the data shared by Google. To obtain coordinates, **Enroute 
    Flight Navigation** will then open Google Maps in an embedded browser window. 
    For privacy reasons, you might be asked to authorize **Enroute Flight Navigation** 
    to open the external website, and Google might ask you to accept their privacy
    policies.  If all goes well, the embedded browser will close itself after a few 
    seconds and the waypoint dialog will appear.  

.. note:: 
  If the embedded browser remains open for more than 30 seconds, then the coordinate
  lookup has failed.  This can happen when there is no internet access. Close the embedded 
  web browser page manually to continue using **Enroute Flight Navigation**.


OpenStreetMap (Online)
----------------------

The procedure depends on the platform in use.

- Android:

  - Double-click into the map to mark a location.

  - Open the main menu of your web browser and choose "Share".

  - You will be presented with a list of contacts and apps that you can share the location
    with. Choose **Enroute Flight Navigation** from this list.

  - **Enroute Flight Navigation** will open a waypoint description dialog for the 
    location.

- Linux/Desktop:

  - Double-click into the map to mark a location.

  - Copy the text from the URL field of your text browser to the clipboard. Depending on the 
    browser, this can be done with a context menu after a right-click into the URL field, 
    or by activating the text field and then using the keyboard shortcuts Ctrl+A Ctrl+C.
  
  - Activate the window of **Enroute Flight Navigation** and paste the text using Ctrl+V. 
    Alternatively, drag-and-drop the text from the URL field of your browser into the
    window of **Enroute Flight Navigation**.


OsmAnd (Android App)
--------------------

Location sharing from the app `OsmAnd 
<https://play.google.com/store/apps/details?id=net.osmand&hl=de&gl=US>`_
does not require coordinate lookup through an embedded browser and is 
therefore particularly easy and hassle-free. Proceed as follows.

- Open the App "OsmAnd" and mark a location by tapping into the moving map. A 
  dialog with location information will open at the bottom of the screen.

- Click on the button "Share". A dialog will open that allows choosing the
  data format.

- Choose the data format "geo:".  A dialog with appropriate apps will open.

- Choose **Enroute Flight Navigation**. 

- **Enroute Flight Navigation** will open with a waypoint description dialog for the 
  location marked by Google Maps.  As usual, use this dialog to add the location 
  to your route or to the waypoint library.
