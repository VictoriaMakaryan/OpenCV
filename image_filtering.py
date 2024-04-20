import cv2 as cv
import sys

img = cv.imread("Photos/sunflower.jpg")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("sunflower", img)
#the default way of reading image in opencv is BGR

def to_gray(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("sunflower", img)
    cv.imshow("Gray", gray)
    cv.waitKey(0)

#to_gray(img)

def to_rgb(img):
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    cv.imshow("sunflower", img)
    cv.imshow("Gray", rgb)
    cv.waitKey(0)
#to_rgb(img)

#hsv means high saturation value

def to_hsv(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    cv.imshow("sunflower", img)
    cv.imshow("HSV", hsv)
    cv.waitKey(0)
#to_hsv(img)

#LAB means 
def to_lab(img):
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

    cv.imshow("sunflower", img)
    cv.imshow("LAB", lab)
    cv.waitKey(0)
#to_lab(img)

def average_blur(img):
    average = cv.blur(img, (3, 3))
    cv.imshow("Aveage blur", average)

    cv.waitKey(0)
#average_blur(img)

def gaussian_blur(img):
    gaussian = cv.GaussianBlur(img, (3, 3), 0)
    cv.imshow("Gaussian blur", gaussian)

    cv.waitKey(0)
#gaussian_blur(img)


