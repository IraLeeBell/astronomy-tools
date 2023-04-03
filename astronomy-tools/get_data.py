# -=-=-=--=-=-=-=-=-=-=-=-=--=-
# MIT License
# Originaly written by Ira Bell
# -=-=-=--=-=-=-=-=-=-=-=-=--=-

import numpy as np
from astropy.io import fits

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f1000w_v1_i2d.fits')

# Get the pixel data
data = hdul[0].data

# Print the shape of the data
print("Data shape:", data.shape)

# Set the numpy print options
np.set_printoptions(threshold=np.inf, precision=4, suppress=True)

# Set the number of rows to print
num_rows = 1
num_columns = 1

# Print the data
print("Data values:")
print(data[:num_rows, :num_columns:])

# Close the FITS file
hdul.close()

