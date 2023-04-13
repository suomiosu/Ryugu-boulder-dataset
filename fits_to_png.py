"""
Convert FITS files to png images

This dataset uses only images taken at altitudes <5km and in visible light

"""
import numpy as np
from astropy.io import fits
from scipy import ndimage

from PIL import Image
import os
import glob

# get folder names (yyyymmdd)
path = "path/to/dir"
folder_names = os.listdir(path)

# parameters
contrast_sigma = 2.
offset_mean = 96.

for folder_name in folder_names:
    # get image names of visible band images(file names end with tvf_l2c.fit)
    folder_path = os.path.join(path, folder_name)
    img_names = glob.glob(folder_path+"/*tvf_l2c.fit")
    output_folder = os.path.join(path, "image")
    os.makedirs(output_folder, exist_ok=True)

    for i, img_name in enumerate(img_names):
        basename = os.path.basename(img_name)
        png_name = os.path.splitext(basename)[0]+'.png'
        output_path = os.path.join(output_folder, png_name)

        # get fits data and save as png
        hdulist_onc=fits.open(img_name)
        hdu_onc=hdulist_onc[1]

        header_onc=hdu_onc.header

        data_onc=hdu_onc.data

        mean_onc = np.mean(data_onc[np.where(data_onc>0)])
        std_onc = np.std(data_onc[np.where(data_onc>0)])

        udata_onc = np.array(np.clip( (data_onc-mean_onc)
                                    / (contrast_sigma * std_onc)*128 + offset_mean,0,255),dtype='u1')

        pil_img = Image.fromarray(udata_onc)
        pil_img.save(output_path)
