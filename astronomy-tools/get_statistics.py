# -=-=-=--=-=-=-=-=-=-=-=-=--=-
# MIT License
# Originally written by Ira Bell
# -=-=-=--=-=-=-=-=-=-=-=-=--=-

import numpy as np
from astropy.io import fits
from scipy.stats import skew

# Open the FITS file
hdul = fits.open('hlsp_jwst-ero_jwst_miri_stephansquintet_f770w_v1_i2d.fits')

# Get the pixel data
data = hdul[1].data

# Print the shape of the data
print("Data shape:", data.shape)

# Calculate and print the minimum, maximum, median, mean, variance, standard deviation, skewness, kurtosis, and percentiles of the data
min_val = np.min(data)
min_idx = np.unravel_index(np.argmin(data), data.shape)
print(f"Minimum value: {min_val:.6f} (Location: {min_idx})")

max_val = np.max(data)
max_idx = np.unravel_index(np.argmax(data), data.shape)
print(f"Maximum value: {max_val:.6f} (Location: {max_idx})")

median_val = np.median(data)
print(f"Median value: {median_val:.6f}")

mean_val = np.mean(data)
print(f"Mean value: {mean_val:.6f}")

var_val = np.var(data)
print(f"Variance: {var_val:.6f}")

std_val = np.std(data)
print(f"Standard deviation: {std_val:.6f}")

skew_val = skew(data, axis=None)
print(f"Skewness: {skew_val:.6f}")

# Close the FITS file
hdul.close()


