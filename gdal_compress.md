gdal_translate \
  -co COMPRESS=JPEG \
  -co PHOTOMETRIC=YCBCR \
  -co TILED=YES \
  5255C.tif 5255C_JPEG_YCBCR.tif
  
gdaladdo \
  --config COMPRESS_OVERVIEW JPEG \
  --config PHOTOMETRIC_OVERVIEW YCBCR \
  --config INTERLEAVE_OVERVIEW PIXEL \
  -r average \
  5255C_JPEG_YCBCR.tif \
  2 4 8 16 32 64
