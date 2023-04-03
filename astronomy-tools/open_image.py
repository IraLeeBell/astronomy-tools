# -=-=-=--=-=-=-=-=-=-=-=-=--=-
# MIT License
# Originaly written by Ira Bell
# -=-=-=--=-=-=-=-=-=-=-=-=--=-

import numpy as np
from astropy.io import fits
from PIL import Image

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f1000w_v1_i2d.fits')

# Get the pixel data
data = hdul[0].data

# Apply a histogram stretch to the data
pmin, pmax = np.percentile(data, (1, 99))
data_stretched = np.clip((data - pmin) / (pmax - pmin), 0, 1)

# Convert the data to a Pillow-compatible image
img = Image.fromarray((data_stretched * 255).astype(np.uint8))

# Display the image
img.show()

# Close the FITS file
hdul.close()
