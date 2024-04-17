import cv2 as cv
import sys

img = cv.imread("Photos/sunflower.jpg")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow('Sunflower', img)

k = cv.waitKey(0)

if k == 1:
    cv.destroyWindow('Cat')