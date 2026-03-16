.. _geotiffConversionTools:

Approach Chart Conversion Tools
===============================

As explained in Section :ref:`vac_tutorial`, **Enroute Flight Navigation** is
able to import and use third-party visual approach charts MBTILES format. Since
GeoTIFF is  an exceptionally complex format that covers use cases ranging from
astronomy to high-precision land survey, **Enroute Flight Navigation** only
supports a subset of the GeoTIFF standard.  If you encounter a GeoTIFF file that
**Enroute Flight Navigation** does not recognize, please `open an issue report
<https://github.com/Akaflieg-Freiburg/enroute/issues/new/choose>`_.  We will be
glad to help! 

Alternatively, you can use the industry-standard `GDAL tools
<https://gdal.org>`_ to convert any GeoTIFF into a format supported by **Enroute
Flight Navigation**. On the Linux command line, this can be done as follows.

::

  gdalwarp -t_srs EPSG:4326 -ot Byte -co "PHOTOMETRIC=RGB" input.tif output.tif

::

