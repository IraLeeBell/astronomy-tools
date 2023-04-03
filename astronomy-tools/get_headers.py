from astropy.io import fits

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f1000w_v1_i2d.fits')

# Get the header of the primary HDU
header = hdul[0].header

# Create variables for each header keyword and assign its value
for key in header:
    exec(f"{key.lower()} = header['{key}']")

# Print the values of the variables
print("Location name:", location)
print("Exposure time:", exptime)
print("Filter name:", filter)

# Close the FITS file
hdul.close()
