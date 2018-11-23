SET PATH=%PATH%;C:\LogicielLabo\Qgis_321\bin
SET GDAL_DATA=C:\LogicielLabo\Qgis_321\share\gdal
set "var=%cd%"
for %%N in (%var%\*.tif) DO C:\LogicielLabo\Qgis_321\bin\gdalwarp -t_srs EPSG:2056 %%N %var%\%%~nN_2056.tif