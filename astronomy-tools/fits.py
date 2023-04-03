#
# MIT License
# Originaly written by Ira Bell
# ASU SESE
#


# may change this file name

from astropy.io import fits

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f1000w_v1_i2d.fits')

# Get the header of the primary HDU
header = hdul[0].header

# Extract three pieces of metadata

simple_name = header['SIMPLE']
bitpix_name = header['BITPIX']
# exposure_time = header['EXPTIME']
# filter_name = header['FILTER']

# Print the metadata
print('Simple name: ', simple_name)
print('Bitpix name:', bitpix_name)
# print('Exposure time:', exposure_time, 'seconds')
# print('Filter name:', filter_name)

# Close the FITS file
hdul.close()