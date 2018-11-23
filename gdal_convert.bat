SET PATH=%PATH%;C:\LogicielLabo\Qgis_321\bin
set "var=%cd%"
for %%N in (%var%\*.tif) DO gdal_translate -b 1 -b 2 -b 3 -a_nodata 0 -co COMPRESS=JPEG -co JPEG_QUALITY=90 -co PHOTOMETRIC=YCBCR -co TILED=YES %%N %var%\%%~nN_compr.tif
for %%N in (%var%\*_compr.tif) DO gdaladdo --config COMPRESS_OVERVIEW JPEG --config JPEG_QUALITY_OVERVIEW 90 --config PHOTOMETRIC_OVERVIEW YCBCR --config INTERLEAVE_OVERVIEW PIXEL -r average %%N 2 4 8 16 32 64