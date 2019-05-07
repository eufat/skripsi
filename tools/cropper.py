# import the necessary packages
import argparse
import cv2
import numpy as np
import spectral.io.envi as envi

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
ref_pt = []
end_pt = ()
cropping = False

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-r", "--repo", required=True, help="Path to the directory")
ap.add_argument("-d", "--date", required=True, help="Date of image taken")
ap.add_argument("-w", "--width", required=True, help="Width of image taken")

args = vars(ap.parse_args())

repo_dir = args["repo"]
date_dir = args["date"]
image_name = args["image"]
width = int(args["width"])
length = width

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global ref_pt, end_pt, cropping

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_pt = [(x, y)]
        cropping = True

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        start_pt = (ref_pt[-1][0], ref_pt[-1][1])
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        end_pt = (ref_pt[-1][0] + width, ref_pt[-1][1] + length)
        cropping = False

        # draw a rectangle around the region of interest
        cv2.rectangle(image, start_pt, end_pt, (0, 255, 0), 2)
    cv2.imshow("image", image)

dark_ref = envi.open(
    '{}/{}/dark_ref/capture/dark_ref.hdr'.format(repo_dir, date_dir),
    '{}/{}/dark_ref/capture/dark_ref.raw'.format(repo_dir, date_dir))
white_ref = envi.open(
    '{}/{}/white_ref/capture/white_ref.hdr'.format(repo_dir, date_dir),
    '{}/{}/white_ref/capture/white_ref.raw'.format(repo_dir, date_dir))
data_ref = envi.open(
    '{}/{}/{}/capture/{}.hdr'.format(repo_dir, date_dir, image_name, image_name),
    '{}/{}/{}/capture/{}.raw'.format(repo_dir, date_dir, image_name, image_name))

white_nparr = np.array(white_ref.load())
dark_nparr = np.array(dark_ref.load())
data_nparr = np.array(data_ref.load())

corrected_nparr = np.divide(
    np.subtract(data_nparr, dark_nparr),
    np.subtract(white_nparr, dark_nparr))

# load the image, clone it, and setup the mouse callback function
image_path = '{}/{}/{}/{}.png'.format(
    repo_dir, date_dir, image_name, image_name)
image = cv2.imread(image_path)
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

def extract_roi(arr, x, y, w, h):
    roi = arr[y:y+h, x:x+w, :]

    return roi

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        rois = []

        for point in ref_pt:
            x = point[0]
            y = point[1]
            roi = extract_roi(corrected_nparr, x, y, width, width)
            rois.append(roi)

        save_path = "{}/{}/{}_rois.npy".format(repo_dir, date_dir, image_name)
        print("Saved at {}.".format(save_path))
        np.save(save_path, rois)
        break

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

# close all open windows
cv2.destroyAllWindows()