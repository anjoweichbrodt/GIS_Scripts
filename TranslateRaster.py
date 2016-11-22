import os
import re
from osgeo import gdal

for dirpath, subdirs, files in os.walk(os.getcwd()) :

    for line in files :
        if line.endswith(('.tif')) :

            ImagePath = os.path.join(dirpath, line)

            PosOrthImg = ImagePath.find('_Const')
            Images_RelPath = ImagePath[PosOrthImg-2 : PosOrthImg]

            if Images_RelPath == 'NE' :
                #gdall.AllRegister()
                rast_src = gdal.Open(ImagePath, 1)
                gt = rast_src.GetGeoTransform()
                # Convert tuple to list, so we can modify it
                gtl = list(gt)
                gtl[0] += 0 #move 200 m west
                gtl[3] -= 7 # move 7 m north
                # Save the geotransform to the raster
                rast_src.SetGeoTransform(tuple(gtl))
                rast_src = None # equivalent to save/close

            elif Images_RelPath == 'SO' :
                #gdall.AllRegister()
                rast_src = gdal.Open(ImagePath, 1)
                gt = rast_src.GetGeoTransform()
                # Convert tuple to list, so we can modify it
                gtl = list(gt)
                gtl[0] += 0 #move 200 m west
                gtl[3] += 7 # move 7 m north
                # Save the geotransform to the raster
                rast_src.SetGeoTransform(tuple(gtl))
                rast_src = None # equivalent to save/close
