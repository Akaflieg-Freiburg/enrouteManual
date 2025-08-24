
Altitude Measurement
====================


Types of Altitude used in **Enroute Flight Navigation**
-------------------------------------------------------

Geometric Altitude
Absolute Altitude
Pressure Altitude
Cabin Altitude



Airspace Side View
------------------

The airspace side view is only available if **Enroute Flight Navigation** has
access to static pressure information.  This section of the manual explains why
and helps to provide the necessary data.


Why does **Enroute** need static pressure for the airspace side view?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vertical airspace boundaries are defines as barometric altitudes, either over
QNH or over the standard pressure level.  As a consequence, the geometric
altitude of airspaces changes with the weather: Airspaces are typically much
lower on cold winter days than they are in summer. In order to show your
aircraft in relation to airspaces, **Enroute Flight Navigation** therefore needs
to know the barometric altitude of your aircraft, or equivalently, the static
pressure.  

.. warning:: Never use true altitude to judge vertical distances to airspaces.


How can I provide static pressure data?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the steps outlined in chapter :ref:`traffic` to connect **Enroute Flight
Navigation** to a traffic data receiver that provides static pressure data.  As
a rule of thumb, any traffic data receiver that handles ADS-B signals will
report static pressure, as static pressure is required to interpret ADS-B data.
In particular, all PowerFLARM devices use and report static pressure.

If you fly an aircraft where static pressure and cabin pressure agree, you can
run the additional app `CCAS <https://ccas.aero/>`__, which runs in the
background, uses pressure sensors in your mobile device and reports the pressure
as static pressure to **Enroute Flight Navigation**.

.. warning:: We strongly recommend connecting **Enroute Flight Navigation** to a 
  proper traffic data receiver.  While CCAS might have its use for pilots flying 
  balloons, paragliders or gyrocopters, think twice before using xx in a 
  motorized plane or glider. In typical GA aircraft, static pressure and cabin 
  pressure do not necessarily agree and errors upwards of 500ft are common.  The 
  precise error typically depends on airspeed and configuration of heating and 
  ventilation system.


But other apps show side views without static pressure data!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We do not know the internal workings of other apps.  However, we do not see how
sufficiently reliable information can possibly be provided without static
pressure data. 

We fly general aviation aircraft in Germany and Switzerland, where vertical
separation between jet aircraft and airspace limits is sometimes no more than
500ft.  In view of the extremely severe consequences of airspace violations, we
decided against showing questionable data.