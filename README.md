# Ryugu-boulder-dataset
This is the dataset for **instance segmentation of boulders on Ryugu**.
This dataset contains 275 images and 20,420 masks (as of March 15th, 2023).

# Getting Started
Images are provided in [https://data.darts.isas.jaxa.jp/pub/hayabusa2/onc_bundle/browse/](https://data.darts.isas.jaxa.jp/pub/hayabusa2/onc_bundle/browse/)
Download and unzip fits file.

```
wget -i url_list.txt
ls *.tgz | xargs -n1 tar xvzf
```

Convert fits files into png files with:

```
python fits_to_png.py
```

The following updates are planned for the future.
* Expansion of annotation data
* Improvement of annotation data accuracy
* Publication of datasets with data augmentation
* Improvement of image sharpness
* Publication of the instance segmentation model for automatic boulder detection
