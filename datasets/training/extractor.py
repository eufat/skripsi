import cv2
from spectral import imshow, view_cube
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib
import spectral.io.envi as envi

repo_dir = '/home/nodeflux/gits/skripsi'
date_dir = '11042019'
num = '1'

dark_ref = envi.open('{}/datasets/training/{}/dark_ref/capture/dark_ref.hdr'.format(repo_dir, date_dir), '{}/datasets/training/{}/dark_ref/capture/dark_ref.raw'.format(repo_dir, date_dir))
white_ref = envi.open('{}/datasets/training/{}/white_ref/capture/white_ref.hdr'.format(repo_dir, date_dir), '{}/datasets/training/{}/white_ref/capture/white_ref.raw'.format(repo_dir, date_dir))
data_ref = envi.open('{}/datasets/training/{}/bisbul_{}_cut/capture/bisbul_{}_cut.hdr'.format(repo_dir, date_dir, num, num), '{}/datasets/training/{}/bisbul_{}_cut/capture/bisbul_{}_cut.raw'.format(repo_dir, date_dir, num, num))

white_nparr = np.array(white_ref.load())
dark_nparr = np.array(dark_ref.load())
data_nparr = np.array(data_ref.load())

# imshow(data_nparr, (64, 55, 19))

corrected_nparr = np.divide(
    np.subtract(data_nparr, dark_nparr),
    np.subtract(white_nparr, dark_nparr))

corrected_nparr.shape

corrected_nparr = corrected_nparr[120:320, 130:380, :]

# imshow(corrected_nparr, (32, 32, 32))

from numpy import genfromtxt

bands = genfromtxt('{}/datasets/training/helpers/bands.csv'.format(repo_dir), delimiter=',')

leaf_pixel_y = 150
leaf_pixel_x = 150
teflon_pixel_y = 100
teflon_pixel_x = 100

leaf_pixel = corrected_nparr[
    leaf_pixel_y:leaf_pixel_y+1,
    leaf_pixel_x:leaf_pixel_x+1,
    :]
teflon_pixel = corrected_nparr[
    teflon_pixel_y:teflon_pixel_y+1,
    teflon_pixel_x:teflon_pixel_x+1,
    :]

leaf_pixel_squeezed = np.squeeze(leaf_pixel)
teflon_pixel_squeezed = np.squeeze(teflon_pixel)

def hsi2rgb(hsi_nparr, rgb):
    (r, g, b) = rgb
    rgb_nparr = np.dstack((hsi_nparr[:, :, r], hsi_nparr[:, :, g], hsi_nparr[:, :, b]))
    return rgb_nparr


def extract_roi(arr, x, y, w, h):
    roi = arr[y:y+h, x:x+w, :]

    return roi

def draw_bbox(img, x, y, w, h, line):
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), line)
    return img


def extract_rois(coordinates, hsi_nparr, length, line):
    rgb_nparr = hsi2rgb(hsi_nparr, (100, 100, 100))
    img_with_bbox = rgb_nparr
    rois = [] # returned ROIs

    for coordinate in coordinates:
        (x, y) = coordinate
        img_with_bbox = draw_bbox(img_with_bbox, x, y, length, length, line)

        roi = extract_roi(hsi_nparr, x, y, length, length)

        rois.append(roi)

    return rois, img_with_bbox

length = 25 # width and height
line = 2 # bounding box line width

coordinates = [
    (15, 28),
    (100, 23),
    (198, 22),
    (20, 155),
    (114, 148),
    (202, 142)]

rois, bounding_boxed = extract_rois(coordinates, corrected_nparr, length, line)
cv2.imshow('image', bounding_boxed)

# for item in rois:
#     imshow(item, (100, 100, 100))

np.save("{}/datasets/training/{}/bisbul_{}_rois.npy".format(repo_dir, date_dir, num), rois)
np.save("{}/datasets/training/{}/bisbul_{}_corrected.npy".format(repo_dir, date_dir, num), corrected_nparr)

# for i in range(len(rois)):
#     roi = rois[i]
#     intensity = []
#     for b in range(roi.shape[2]):
#         intensity.append(np.mean(roi[:, :, b]))
#     plt.plot(bands, intensity, label='ROI {}'.format(i+1))

# plt.legend(loc='upper left')
# plt.title('Leaf Spectral Footprint\n Mean in ROI Area')
# plt.xlabel('Wavelength (nm)')
# plt.ylabel('Reflectance')
# plt.show()