import cv2 as cv
import sys 
import numpy as np

img = cv.imread('Photos/sunflower.jpg')

if img is None:
    sys.exit("Unable to read the image.")

#rescale the image
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#funcion calls

#rescaled_img = rescaleFrame(img, scale=0.75)

#cv.imshow("Original Sunflower", img)

#cv.imshow("Rescaled Sunflower", rescaled_img)

# while True:
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cv.destroyAllWindows()

#rotation
def rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]

    if rotationPoint is None:
        rotationPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

#function calls

# rotated_image = rotate(img, 60)

# cv.imshow("Original Sunflower", img)
# cv.imshow('Rotated', rotated_image)

# while True:
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cv.destroyAllWindows()


def flip_vertically(img):
    return cv.flip(img, 0)

#function calls

# flipped_image = flip_vertically(img)


# cv.imshow("original sunflower", img)
# cv.imshow("flipped vertically image", flipped_image)

# while True:
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cv.destroyAllWindows()


def flip_horizontally(img):
    return cv.flip(img, 1)

#function calls

# flipped_image = flip_horizontally(img)


# cv.imshow("original sunflower", img)
# cv.imshow("flipped vertically image", flipped_image)

# while True:
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cv.destroyAllWindows()

def crop(img):
    return img[200:400, 300:400]

#function calls

# cropped_image = crop(img)
# cv.imshow("original image", img)
# cv.imshow("cropped image", cropped_image)

# while True:
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cv.destroyAllWindows()