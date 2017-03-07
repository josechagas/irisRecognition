import numpy as np
import cv2
import math
from scipy.signal import convolve2d

from IrisProcessing import showImage



#This method calculates and returns the corresponding point of circle on its border for some angle
def __pointOfCircle(circle,angle):
    rads = angle * math.pi / 180
    cosValue = math.cos(rads)
    sinValue = math.sin(rads)
    x = int(circle[0] + circle[2] * cosValue)
    y = int(circle[1] + circle[2] * sinValue)
    return [x,y]


#This method extracts the iris information
#pupilRadioOffset this value indicates how many pixels you want to increment on pupil radio to avoid the possibility
#to appear some pupil pixels
#The size of normalized image depends of irisRadio - pupilRadio, that can change because of pupil dilation for example
def normalizeIrisRegion(eyeImage,pupilCircle,irisCircle,pupilRadioOffset=0):
    lins = int(irisCircle[2] - pupilCircle[2] - pupilRadioOffset)  # int(irisCircle[2] - pupilCircle[2])
    cols = 360#int((irisCircle[2] - pupilCircle[2]) + 2)
    irisData = np.zeros((lins, cols), np.uint8)

    xDif = irisCircle[0] - pupilCircle[0]
    yDif = irisCircle[1] - pupilCircle[1]

    for ri in range(int(pupilCircle[2] + pupilRadioOffset),irisCircle[2]):
        line = np.zeros(360, np.uint8)
        for angle in range(0,cols):
            cosValue = math.cos(angle*math.pi/180)
            sinValue = math.sin(angle * math.pi / 180)
            x = int(irisCircle[0] + (ri - xDif*cosValue)*cosValue)
            y = int(irisCircle[1] + (ri - yDif*sinValue) * sinValue)
            line[angle] = eyeImage[y][x]
        irisData[int(ri - pupilCircle[2] - pupilRadioOffset)] = line

    return irisData

#Rubber Sheet Model
# this method normalize the iris region using the same method of Daugman, so the normalized image
#always has the same dimensions fixing some problems like pupil dilation and other thing that might cause
#changes on normalized iris region image size

#eyeImage = image that contains a localized iris and pupil
#pupilCircle = circle with the same localization of pupil region
#irisCircle = circle with the same localization of iris region
#numbOfLins = number of lines you want the normalized iris region to have
#pupilOffset =increment on pupilCenter ray to avoid for example getting some pupil information
def RSM_NormIrisRegion(eyeImage,pupilCircle,irisCircle,numbOfLins=40,pupilOffset=0):
    numbOfCols = 360
    irisData = np.zeros((numbOfLins, numbOfCols), np.uint8)
    for p in np.arange(0.0, 1.0, 1.0 / numbOfLins):
        line = np.zeros(numbOfCols, np.uint8)
        for angle in range(0,360,360/numbOfCols):
            pupilPoint = __pointOfCircle([pupilCircle[0],pupilCircle[1],pupilCircle[2]+pupilOffset],angle)
            irisPoint = __pointOfCircle(irisCircle,angle)
            xo = int((1-p)*pupilPoint[0] + p*irisPoint[0])
            yo = int((1-p)*pupilPoint[1] + p*irisPoint[1])
            line[angle] = eyeImage[yo][xo]
        irisData[int(p*numbOfLins)] = line
    return irisData

############################# Fourier Transform ####################################
#tutorial = http://www.peterkovesi.com/matlabfns/PhaseCongruency/Docs/convexpl.html

#http://docs.opencv.org/3.1.0/de/dbc/tutorial_py_fourier_transform.html
#fourier transform using numpy methods
def __NP_fourierTransformOf(image,showProcess=False):
    if showProcess: showImage(image,"Image")
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    if showProcess:
        magnitude_spectrum = 20 * np.log(np.abs(fshift))
        showImage(magnitude_spectrum.astype(np.uint8), "Fourier transform")
    return fshift

#using cv2
#teorically faster
#fourier transform using opencv methods
def CV2_fourierTransformOf(image,showProcess=False):
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    if showProcess:
        magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
        showImage(magnitude_spectrum.astype(np.uint8), "Fourier transform")
    return dft_shift

#invert fourier transform using opencv methods
def CV2_invertFourierTransformOf(data,showProcess=False):
    f_ishift = np.fft.ifftshift(data)
    img_back = cv2.idft(f_ishift)
    if showProcess:
        img_mag = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
        showImage(img_mag.astype(np.uint8),"mag")
    return img_back

#invert fourier transform using numpy methods
def __NP_invertFourierTransformOf(data):
    f_ishift = np.fft.ifftshift(data)
    img_back = np.fft.ifft2(f_ishift)
    #img_mag = np.abs(img_back)
    return img_back

#this method fixes the image to best size for improve performance of fourier transform
def __fixImgToFTBestSize(image):
    # get best size
    rows = image.shape[0]
    columns = image.shape[1]
    nrows = cv2.getOptimalDFTSize(rows)
    ncols = cv2.getOptimalDFTSize(columns)
    right = ncols - columns
    bottom = nrows - rows
    nimg = cv2.copyMakeBorder(image, 0, bottom, 0, right, cv2.BORDER_CONSTANT, value=0)
    return nimg

#############################

#This method apply the last codification process on filtered and normalized image of iris region
def __extractCharacteristics(filteredIrisData):
    rows = filteredIrisData.shape[0]
    cols = filteredIrisData.shape[1]
    irisCode = np.zeros((rows, cols,2),np.uint8)

    # old way (working)
    # for row in range(0, rows):
    #     lineCode = np.zeros((cols,2),np.uint8)
    #     for col in range(0, cols):
    #         complexValue = filteredIrisData[row][col]
    #         hRE = 1
    #         if complexValue.real < 0 : hRE = 0
    #         hIM = 1
    #         if complexValue.imag < 0: hIM = 0
    #         lineCode[col] = [hRE,hIM]
    #     irisCode[row] = lineCode

    #improved way
    for row in range(0, rows):
        lineCode = np.zeros((cols,2),np.uint8)
        for col in range(0, cols/2):
            complexValue = filteredIrisData[row][col]
            hRE = 1
            if complexValue.real < 0 : hRE = 0
            hIM = 1
            if complexValue.imag < 0: hIM = 0
            lineCode[col] = [hRE,hIM]

            delta = (cols / 2) + col
            complexValue = filteredIrisData[row][delta]
            hRE = 1
            if complexValue.real < 0 : hRE = 0
            hIM = 1
            if complexValue.imag < 0: hIM = 0
            lineCode[delta] = [hRE,hIM]

        irisCode[row] = lineCode
    return irisCode


def __codificate(irisData,showProcess=False):
    imgFT = __NP_fourierTransformOf(irisData,showProcess)
    rows = imgFT.shape[0]
    cols = imgFT.shape[1]
    gFilter = __2DLogGaborFilter(rows,cols,4.0,0.65)

    filtered = imgFT*gFilter
    #filtered = cv2.filter2D(imgFT,-1,gFilter)
    #filtered = convolve2d(imgFT,gFilter)
    if showProcess: showImage(filtered.astype(np.uint8),"filtered")

    #img = __CV2_invertFourierTransformOf(imgFT)
    #img = __NP_invertFourierTransformOf(imgFT)
    img = __NP_invertFourierTransformOf(filtered)
    if showProcess: showImage(img.astype(np.uint8),"Template")
    return img


#This method codificate the normalized irisData
#irisData=Normalized irisRegion
#showProcess=Present or not some steps of process as images
def codificateNormImg(normImg,showProcess=False):
    img = __codificate(normImg,showProcess)
    return __extractCharacteristics(img)

#This method normalize the irisRegion localized on irisCircle and codificate it
#eyeImage = image that contains a localized iris and pupil
#pupilCircle = circle with the same localization of pupil region
#irisCircle = circle with the same localization of iris region
#numbOfLins = number of lines you want the normalized iris region to have
#pupilOffset =increment on pupilCenter ray to avoid for example getting some pupil information
#showProcess=Present or not some steps of process as images

def codificateIrisData(eyeImage,pupilCircle,irisCircle,numbOfLins=40,pupilOffset=0,showProcess=False):

    normIrisImg = RSM_NormIrisRegion(eyeImage,pupilCircle,irisCircle,numbOfLins,pupilOffset)
    if showProcess: showImage(normIrisImg,"Normalized iris region")
    img = __codificate(normIrisImg,showProcess)
    return __extractCharacteristics(img)


def __2DLogGaborFilter(lins,cols,waveLenght,sigmaOnf):
    if not hasattr(__2DLogGaborFilter, "cachedFilter"):
        __2DLogGaborFilter.cachedFilter = __build2DLogGaborFilter(lins, cols, waveLenght, sigmaOnf)
    return __2DLogGaborFilter.cachedFilter

def __build2DLogGaborFilter(lins,cols,waveLenght,sigmaOnf):
    #radius matrix
    #populate the radius matrix
    x = -(cols/2.0)
    y = -(lins/2.0)

    #old way (working)
    # radius = np.zeros((lins, cols))
    # for lin in range(0,lins):
    #     yLin = (y + lin)/lins
    #     line = np.zeros(cols)
    #     for col in range(0,cols):
    #         xCol = (x + col)/cols
    #         line[col] = math.sqrt(((xCol)**2 + (yLin)**2))#math.sqrt((((x + col)/cols)**2 + ((y + lin)/lins)**2)/2.0)
    #     radius[lin] = line
    # radius[lins/2][cols/2] = 1
    # #return radius
    #
    #
    # ################################# radial part of filter
    # #waveLenght = 3.0#10.0# at least 2 #######
    # f0 = 1.0/waveLenght
    # #sigmaOnf = 0.55#0.75 ########
    # gaborRadial = np.zeros((lins, cols))
    # for lin in range(0,lins):
    #     lineLog = np.zeros(cols)
    #     for col in range(0,cols):
    #         f = radius[lin][col]
    #         radialPart = math.exp(-((math.log10(f / f0)) ** 2) / (2 * (math.log10(sigmaOnf)) ** 2))
    #         lineLog[col] = radialPart
    #     gaborRadial[lin] = lineLog
    # gaborRadial[lins/2][cols/2] = 0
    # #return gaborRadial
    #
    # #new = cv2.normalize(gaborRadial,0,1,cv2.NORM_MINMAX)
    # #showImage(new,"read")
    #
    # ################################## angular part of filter
    # spread = np.zeros((lins, cols))
    # thetaSigma = 1.5 ######
    # for lin in range(0,lins):
    #     yLin = (y + lin)/lins
    #     spreadLine = np.zeros(cols)
    #     for col in range(0,cols):
    #         xCol = (x + col)/cols
    #         theta = math.atan2(-yLin,xCol)
    #         sinTheta = math.sin(theta)
    #         cosTheta = math.cos(theta)
    #
    #         angl = col*math.pi/180
    #         ds = sinTheta*math.cos(angl) - cosTheta*math.sin(angl)
    #         dc = cosTheta*math.cos(angl) + sinTheta*math.sin(angl)
    #         dTheta = abs(math.atan2(ds,dc))
    #
    #         anglePart = math.exp(-(dTheta**2)/(2*(thetaSigma)**2))
    #         spreadLine[col] = anglePart
    #     spread[lin] = spreadLine
    #
    # filter0 = spread * gaborRadial
    ####

    #new way

    ################################# radial part of filter
    # waveLenght = 3.0#10.0# at least 2 #######
    f0 = 1.0 / waveLenght
    # sigmaOnf = 0.55#0.75 ########
    gaborRadial = np.zeros((lins, cols))
    #################################

    ################################## angular part of filter
    spread = np.zeros((lins, cols))
    thetaSigma = 1.5  ######
    #################################

    for lin in range(0,lins):
        yLin = (y + lin)/lins

        lineLog = np.zeros(cols)###radial

        spreadLine = np.zeros(cols)###angular
        for col in range(0,cols):

            xCol = (x + col)/cols
            ################################# radial part of filter
            f = math.sqrt(((xCol)**2 + (yLin)**2))#math.sqrt((((x + col)/cols)**2 + ((y + lin)/lins)**2)/2.0)
            if lin == lins/2 and col == cols/2:
                f = 1

            radialPart = math.exp(-((math.log10(f / f0)) ** 2) / (2 * (math.log10(sigmaOnf)) ** 2))
            lineLog[col] = radialPart
            #################################

            ################################## angular part of filter
            theta = math.atan2(-yLin,xCol)
            sinTheta = math.sin(theta)
            cosTheta = math.cos(theta)

            angl = col*math.pi/180
            ds = sinTheta*math.cos(angl) - cosTheta*math.sin(angl)
            dc = cosTheta*math.cos(angl) + sinTheta*math.sin(angl)
            dTheta = abs(math.atan2(ds,dc))

            anglePart = math.exp(-(dTheta**2)/(2*(thetaSigma)**2))
            spreadLine[col] = anglePart
            #################################

        gaborRadial[lin] = lineLog###radial
        spread[lin] = spreadLine###angular

    gaborRadial[lins/2][cols/2] = 0###radial

    #gaborRadial = cv2.blur(gaborRadial,(2,2))# last thing added
    showImage((gaborRadial*100).astype(np.uint8),"radial part")

    showImage((spread*100).astype(np.uint8),"angular part")

    filter = spread*gaborRadial
    showImage((filter*100).astype(np.uint8),"filter part")

    return filter

def cache2DLGFilter(codNumbOfLins=40):
    # #waveLenght = 3.0#10.0# at least 2 #######
    # f0 = 1.0/waveLenght
    # #sigmaOnf = 0.55#0.75 ########

    __2DLogGaborFilter(codNumbOfLins,360,8.0,0.55)
    #__2DLogGaborFilter(codNumbOfLins,codNumbOfLins,4.0,0.65)
    #__2DLogGaborFilter(5,5,4.0,0.65)