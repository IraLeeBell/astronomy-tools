# -=-=-=--=-=-=-=-=-=-=-=-=--=-
# MIT License
# Originaly written by Ira Bell
# -=-=-=--=-=-=-=-=-=-=-=-=--=-

from astropy.io import fits

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f1000w_v1_i2d.fits')

# Get the pixel data from the first HDU
data = hdul[0].data

# Print the shape of the data array
print("Data shape:", data.shape)

# Print the first few elements of the data array
print("Data values:")
print(data[:10, :10])

# Close the FITS file
hdul.close()