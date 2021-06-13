# RIDGESEGMENT - Normalises fingerprint image and segments ridge region
#
# Function identifies ridge regions of a fingerprint image and returns a
# mask identifying this region.  It also normalises the intesity values of
# the image so that the ridge regions have zero mean, unit standard
# deviation.
#
# This function breaks the image up into blocks of size blksze x blksze and
# evaluates the standard deviation in each region. If the standard
# deviation is above the threshold it is deemed part of the fingerprint.
# Note that the image is normalised to have zero mean, unit standard
# deviation prior to performing this process so that the threshold you
# specify is relative to a unit standard deviation.
#
# Usage:   [normim, mask, maskind] = ridgesegment(im, blksze, thresh)
#
# Arguments:   im     - Fingerprint image to be segmented.
#              blksze - Block size over which the the standard
#                       deviation is determined (try a value of 16).
#              thresh - Threshold of standard deviation to decide if a
#                       block is a ridge region (Try a value 0.1 - 0.2)
#
# Returns:     normim - Image where the ridge regions are renormalised to
#                       have zero mean, unit standard deviation.
#              mask   - Mask indicating ridge-like regions of the image,
#                       0 for non ridge regions, 1 for ridge regions.
#              maskind - Vector of indices of locations within the mask.
#
# Suggested values for a 500dpi fingerprint image:
#
#   [normim, mask, maskind] = ridgesegment(im, 16, 0.1)
#
# See also: RIDGEORIENT, RIDGEFREQ, RIDGEFILTER

# REFERENCES

# Peter Kovesi
# School of Computer Science & Software Engineering
# The University of Western Australia
# pk at csse uwa edu au
# http://www.csse.uwa.edu.au/~pk

import numpy as np


def normalise(img, mean, std):
    normed = (img - np.mean(img))/(np.std(img))
    return(normed)


def ridge_segment(im, blksze, thresh):

    rows, cols = im.shape

    # normalise to get zero mean and unit standard deviation
    im = normalise(im, 0, 1)

    # gettting updated number of rows and cols
    new_rows = np.int(blksze * np.ceil((np.float(rows))/(np.float(blksze))))
    new_cols = np.int(blksze * np.ceil((np.float(cols))/(np.float(blksze))))

    # we have to padd the image because we after
    padded_img = np.zeros((new_rows, new_cols))
    stddevim = np.zeros((new_rows, new_cols))

    padded_img[0:rows][:, 0:cols] = im

    for i in range(0, new_rows, blksze):
        for j in range(0, new_cols, blksze):
            # get the current block
            block = padded_img[i:i+blksze][:, j:j+blksze]

            # then get the std deviation of current block and multiply it with unit array of size (block_size x block_size)
            stddevim[i:i+blksze][:, j:j +
                                 blksze] = np.std(block)*np.ones(block.shape)

    stddevim = stddevim[0:rows][:, 0:cols]

    # get only those values for which std deviation is > threshold value
    mask = stddevim > thresh

    # get the mean and standard deviation of this mask
    mean_val = np.mean(im[mask])

    std_val = np.std(im[mask])

    # normalize the mask
    normim = (im - mean_val)/(std_val)

    # at last return this normalized image along with the mask
    return(normim, mask)
