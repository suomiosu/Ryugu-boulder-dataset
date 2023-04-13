# Ryugu-boulder-dataset
This is the dataset for **automatic detection of boulders on asteroid Ryugu**, presented at Lunar and Planetary Science Conference 2023. [View abstract](https://www.hou.usra.edu/meetings/lpsc2023/pdf/1888.pdf)

This dataset contains 275 images and 20,420 masks (as of March 15th, 2023).

|Original Images|Annotation Masks|
|---|---|
|<img width="300" alt="Picture3" src="https://user-images.githubusercontent.com/119026940/231690315-f6ac3256-66f2-4c3b-9527-3c54a1d12767.png">|<img width="300" alt="Picture1" src="https://user-images.githubusercontent.com/119026940/231690664-7a69bd29-ba96-464e-8b13-373ef9e98fb9.png">|
|<img width="300" alt="Picture1" src="https://user-images.githubusercontent.com/119026940/231690369-fe14005a-7e64-44f2-8e6d-1db31f0c68b3.png">|<img width="300" alt="Picture1" src="https://user-images.githubusercontent.com/119026940/231690499-64e4ac88-9d21-4938-83e8-ca6c9841ed2c.png">|

# Getting Started
Images are provided from [Data ARchives and Transmission System (DARTS)](https://data.darts.isas.jaxa.jp/pub/hayabusa2/onc_bundle/browse/).
1. Download and unzip FITS files with:

```
wget -i url_list.txt -P path/to/dstdir
cd path/to/dstdir
ls *.tgz | xargs -n1 tar xvzf
```

2. Convert fits files into png files with:

```
python fits_to_png.py
```
Note that the FITS file contains information such as altitude and location, 
and is also used to determine the size and distribution of detected boulders.

The following updates are planned for the future.
* Expansion of annotation data
* Improvement of annotation data accuracy
* Publication of datasets with data augmentation
* Improvement of image sharpness
* Publication of the instance segmentation model for automatic boulder detection
