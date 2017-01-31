
import numpy as np
import cv2
#import scipy
from scipy.misc import derivative


#integration
#https://docs.scipy.org/doc/scipy-0.18.1/reference/integrate.html
#convolution
#https://docs.scipy.org/doc/numpy-1.10.1/reference/routines.math.html

def __integralPart(x):
    return x**2

def __derivativePart(eyeImage,):
    return derivative(__integralPart,5,1)

def inte_difer_Operator(eyeImage):
    #http: // www.codeforge.com / article / 227219  # comment
    print __derivativePart(eyeImage)