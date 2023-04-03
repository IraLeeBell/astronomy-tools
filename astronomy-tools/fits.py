# -=-=-=--=-=-=-=-=-=-=-=-=--=-
# MIT License
# Originaly written by Ira Bell
# -=-=-=--=-=-=-=-=-=-=-=-=--=-


# may change this file name

from astropy.io import fits

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f1000w_v1_i2d.fits')

# Get the header of the primary HDU
header = hdul[0].header

# Extract three pieces of metadata

simple_name = header['SIMPLE']
bitpix_name = header['BITPIX']
NAXIS_name = header['']
NAXIS1_name = header['']
NAXIS2_name = header['']
EXTEND_name = header['']
MJD-BEG_name = header['']
MJD-AVG_name = header['']
MJD-END_name = header['']
TDB-BEG_name = header['']
TDB-MID_name = header['']
TBD-END_name = header['']
XPOSURE_name = header['']
TELAPSE_name = header['']
REFFRAME_name = header['']
EPH_TYPE_name = header['']
EPH_TIME_name = header['']
JWST_X_name = header['']
jwst_y_name = header['']
jwst_z_name = header['']
obsgeo-x_name = header['']
obsgeo-y_name = header['']
obsgeo-z_name = header['']
jwst_dx_name = header['']
jwst_dy_name = header['']
jwst_dz_name = header['']
obsgeodx_name = header['']
obsgeody_name = header['']
obsgeodz_name = header['']
pa_aper_name = header['']
va_scale_name = header['']
bunit_name = header['']
phototmjsr_name = header['']
photouja2_name = header['']
pixar_sr_name = header['']
pixar_a2_name = header['']
_name = header['']
_name = header['']
_name = header['']
_name = header['']
_name = header['']
_name = header['']
_name = header['']
_name = header['']
_name = header['']

# Print the metadata
print('Simple name: ', simple_name)
print('Bitpix name:', bitpix_name)

# Close the FITS file
hdul.close()