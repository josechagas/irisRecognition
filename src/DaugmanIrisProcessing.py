import math
from scipy.integrate import tplquad
from scipy.integrate import dblquad

from scipy.misc import derivative
import cv2

#integration
#https://docs.scipy.org/doc/scipy-0.18.1/reference/integrate.html
#convolution
#https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.math.html


def __gaussianKernel(r):
    k = 0.84089642
    return (1/(k*math.sqrt(2*math.pi)))*math.exp(-(r**2)/2*(k**2))


def __func(y0,x0,image):
    #return image[y0][x0]/2*math.pi*r
    return image[x0][y0]


def integrand(rmin,rmax,image):
    #return dblquad(__func,x0-r,x0+r,y0-r,y0+r,args=(r,image))
    width = image.shape[1]
    height = image.shape[0]

    def xmin(y):
        return y
    def xmax(y):
        return width
    return dblquad(__func,0,height,xmin,xmax,args=([image]))


def derivand():
    return derivative()

def executeOpForImage(imagePath):
    eyeImage = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    width = eyeImage.shape[1]
    height = eyeImage.shape[0]
    value = integrand(30,width/2,eyeImage)#/2*math.pi*width/4
    print value

