# -=-=-=--=-=-=-=-=-=-=-=-=--=-
# MIT License
# Originally written by Ira Bell
# -=-=-=--=-=-=-=-=-=-=-=-=--=-

from astropy.io import fits

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f770w_v1_i2d.fits')

# Get the number of image extensions and their titles
num_images = 0
for hdu in hdul:
    if isinstance(hdu, fits.ImageHDU):
        num_images += 1
        print(f"Extension {num_images} - Title: {hdu.header['EXTNAME']}")

# Output the number of image extensions
print(f"Number of image extensions in the file: {num_images}")

# Close the FITS file
hdul.close()


