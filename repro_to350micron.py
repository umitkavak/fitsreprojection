#!/usr/bin/python

#-------------------------------------------
# importing libraries
#-------------------------------------------
import os
import math
import numpy as np
from astropy.wcs import WCS
import matplotlib.pyplot as plt

from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename

hdu1 = fits.open(get_pkg_data_filename('ngc7538_350micron_erg.fits'))[1]
hdu2 = fits.open(get_pkg_data_filename('ngc7538_350micron_erg.fits'))[1]

from reproject import reproject_interp
array, footprint = reproject_interp(hdu2, hdu1.header)

fits.writeto('ngc7538_spire350_repro350_erg.fits', array, hdu1.header, overwrite=True)
