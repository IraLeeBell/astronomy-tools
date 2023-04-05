# -=-=-=--=-=-=-=-=-=-=-=-=--=-
# MIT License
# Originally written by Ira Bell
# -=-=-=--=-=-=-=-=-=-=-=-=--=-

import numpy as np
from astropy.io import fits

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f770w_v1_i2d.fits')

# Get the pixel data
data = hdul[1].data

# Print the shape of the data
print("Data shape:", data.shape)

# Set the numpy print options
np.set_printoptions(threshold=np.inf, precision=10, suppress=True)

# Set the number of rows to print
num_rows = 400
num_columns = 400

# Print the data
print("Data values:")
print(data[:num_rows, :num_columns:])

# Close the FITS file
hdul.close()

