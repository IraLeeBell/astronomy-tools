# -=-=-=--=-=-=-=-=-=-=-=-=--=-
# MIT License
# Originaly written by Ira Bell
# -=-=-=--=-=-=-=-=-=-=-=-=--=-

from astropy.io import fits

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f1000w_v1_i2d.fits')

# Get the header of the primary HDU
header = hdul[0].header

header_keys = list(header.keys())
print(header_keys)

# Create variables for each header keyword and assign its value
for key in header:
    if key == 'COMMENT':
        if isinstance(header[key], str) and header[key].strip():
            value = header[key].replace("'", "\\'").replace('"', '\\"')
            exec(f"{key.lower().replace('-', '_')} = '{value}'")
    elif key == 'CONTINUE':
        continue
    else:
        var_name = key.lower().replace('-', '_')
        try:
            if isinstance(header[key], str):
                value = header[key].replace("'", "\\'").replace('"', '\\"')
                exec(f"{var_name} = '{value}'")
            else:
                exec(f"{var_name} = {header[key]}")
        except fits.verify.VerifyError as e:
            if str(e).startswith('CONTINUE cards must have string values'):
                continue
            else:
                raise e

# Print the values of the variables
for key in header:
    var_name = key.lower().replace('-', '_')
    try:
        value = eval(var_name)
        print(f"{var_name} = {value}")
    except NameError:
        pass


# Use the variables in a sentence
# Need to modify this to make sure something exists or it
# doesn't print... 

print(f'The right ascension of this object is: {ra}')
print(f'The declination of this object is: {dec}')

# Close the FITS file
hdul.close()
