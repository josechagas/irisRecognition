import numpy as np
import cv2
import math

def captureVideoFromCamera():
    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on thqe frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        tryToShowPupil(gray)
        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

#this method presents the image with some title
#image = choosed image
#title = title for choosed image
def showImage(image,title):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#This method draw circle on respective image
#image = choosed image
#circles = array of circles to draw
#filled = boolean value that indicates if the circles will be filled with white color or not
def drawCirclesOnImage(image,circles,filled=False):
    thickness = 2
    if filled: thickness = -1
    for i in circles:
        # draw the outer circle
        cv2.circle(image, (i[0], i[1]), i[2], (255, 255, 255), thickness, 2)
        # draw the center of the circle
        cv2.circle(image, (i[0], i[1]), 2, (255, 255, 255), thickness, 3)
    return image

#Draw lines on image
#image  = choosed image
#lines = array of lines to draw
def drawLinesOnImage(image,lines):
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    return image

#Draw a rectangle on a image
#image = choosed image
#topLefPoint = the top left corner point
#width = width of rectangle
#height = height of rectangle
def drawRectangleOnImage(image,topLeftPoint,width,height):

    bottomRightPoint = (topLeftPoint[0]+width,topLeftPoint[1]+height)
    cv2.rectangle(image,topLeftPoint,bottomRightPoint,(255,255,255))

#returns a rectangle based on parameters
#circle region
#offSetBy a tuple with some values indicating how much it should be bigger or smaller than circle
def rectangleOfCircle(circle,offSetBy=(0,0)):
    # rect with radio equal iris circle
    heightOne = int(circle[2] * 2 + offSetBy[1])
    widthOne = int(circle[2] * 2 + offSetBy[0])

    circleCenterXOne = circle[0]
    circleCenterYOne = circle[1]

    topLeftPointOne = (int(circleCenterXOne - widthOne / 2), int(circleCenterYOne - heightOne / 2))
    return [topLeftPointOne[0],topLeftPointOne[1],widthOne,heightOne]

#This method only calculates the distance between two points
def __distanceBetweenPoints(px1,py1,px2,py2):
    a = (px2 - px1) ** 2 + (py2 - py1) ** 2
    b = math.sqrt(a)
    return b

# this method codificates the iris region, preparing it to be saved and/or recognized
# eyeImage = the original image with iris
#pupilCircle = the circle that represents the pupil region
#irisCircle = the circle that represents the iris region
#showProcess = Boolean value that indicates if you want to see steps of process
def __irisCodification(eyeImage,pupilCircle,irisCircle,showProcess=False):
    copyImage = eyeImage.copy()
    # rect inside iris circle
    # heightOne = int(irisCircle[2]  - 5)
    # widthOne =  int(math.sqrt((irisCircle[2] ** 2) - (heightOne ** 2)/4)*2)

    # rect with radio equal iris circle
    offSetBy = (0, -3*int(irisCircle[2] - pupilCircle[2])/2)#(widthOffset,heightOffset)
    rectOutIris = rectangleOfCircle(irisCircle,offSetBy)
    if showProcess: drawRectangleOnImage(copyImage, (rectOutIris[0],rectOutIris[1]), rectOutIris[2],rectOutIris[3])  # iris region rectangle


    rectOutPupil = rectangleOfCircle(pupilCircle)
    if showProcess: drawRectangleOnImage(copyImage, (rectOutPupil[0], rectOutPupil[1]), rectOutPupil[2],
                                         rectOutPupil[3])  # iris region rectangle

    # only iris region image
    irisRectImage = eyeImage[rectOutIris[1]:rectOutIris[1] + rectOutIris[3],
                    rectOutIris[0]:rectOutIris[0] + rectOutIris[2]]

    cv2.imshow("cropped iris rect", irisRectImage)
    cv2.imshow("iris image", copyImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#This method try to find iris outer countorn
#eyeImage must have the pupil paited of black
#pupilCircle = circle that represents the pupil region
def __irisCircleOnImage(blackedPupilEyeImage,pupilCircle,showProcess):
    # eyeImage.shape[0] lines
    # eyeImage.shape[1] columns
    center = (blackedPupilEyeImage.shape[0] / 2, blackedPupilEyeImage.shape[1] / 2)
    processedImage = cv2.medianBlur(blackedPupilEyeImage, 11)#11#cv2.Canny(blackedPupilEyeImage, 5, 70, 3)  # cv2.Canny(processedImage, 55, 60,3)#

    if showProcess: showImage(processedImage, "Canny Iris Image")

    #processedImage = cv2.GaussianBlur(processedImage, (9,9), 0,0)  # cv2.GaussianBlur(eyeImage, (9, 9), 2, 2)

    #if showProcess: showImage(processedImage, "Blurred Iris Image")

    i = 30
    max = 100
    bestIrisCircle = None
    while (i < max and bestIrisCircle is None):
        print "tentativa "+str(i - 30)
        objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200, i, pupilCircle[2],int(pupilCircle[2] + 20))
        if i == max - 1:
            print "teste"
        if objCircles is None:
            print"No Circles were found"
        elif objCircles.__len__() > 0:
            circles = objCircles[0]
            if circles.__len__() > 0:
                if circles.__len__() == 1:
                    bestIrisCircle = circles[0]
                else:
                    if bestIrisCircle is None:
                        bestIrisCircle = circles[0]
                    lastDistance = __distanceBetweenPoints(pupilCircle[0], pupilCircle[1], bestIrisCircle[0],
                                                             bestIrisCircle[1])
                    for k in circles:
                        d = __distanceBetweenPoints(pupilCircle[0], pupilCircle[1], k[0], k[1])
                        if d == 0 and k[2] > pupilCircle[2]:
                            return k
                        elif d < lastDistance:
                            lastDistance = d
                            bestIrisCircle = k

        i += 1

    print int(pupilCircle[2] + 20)
    print bestIrisCircle[2]
    #return bestIrisCircle
    return [pupilCircle[0],pupilCircle[1],bestIrisCircle[2]]#fixing some deviation on center

def __irisCircleOnImageV1(blackedPupilEyeImage,pupilCircle,showProcess=False):
    # eyeImage.shape[0] lines
    # eyeImage.shape[1] columns

    center = (blackedPupilEyeImage.shape[0] / 2, blackedPupilEyeImage.shape[1] / 2)
    processedImage = cv2.medianBlur(blackedPupilEyeImage, 11)

    if showProcess: showImage(processedImage, "Median Blurred Iris Image")

    i = 30
    max = 100
    bestIrisCircle = None
    while (i < max and bestIrisCircle is None):
        print "tentativa "+str(i - 30)
        objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200, i, pupilCircle[2],int(pupilCircle[2] + 20))
        if i == max - 1:
            print "teste"
        if objCircles is None:
            print"No Circles were found"
        elif objCircles.__len__() > 0:
            circles = objCircles[0]
            if circles.__len__() > 0:
                if circles.__len__() == 1:
                    bestIrisCircle = circles[0]
                else:
                    if bestIrisCircle is None:
                        bestIrisCircle = circles[0]
                    lastDistance = __distanceBetweenPoints(pupilCircle[0], pupilCircle[1], bestIrisCircle[0],
                                                             bestIrisCircle[1])
                    for k in circles:
                        d = __distanceBetweenPoints(pupilCircle[0], pupilCircle[1], k[0], k[1])
                        if d == 0 and k[2] > pupilCircle[2]:
                            return k
                        elif d < lastDistance:
                            lastDistance = d
                            bestIrisCircle = k

        i += 1

    print int(pupilCircle[2] + 20)
    print bestIrisCircle[2]
    #return bestIrisCircle
    return [pupilCircle[0],pupilCircle[1],bestIrisCircle[2]]#fixing some deviation on center


#This method tries to find the region that corresponds to pupil
def __pupilCircleOnImage(eyeImage,showProcess):
    if showProcess : showImage(eyeImage, "Original Iris Image")
    # eyeImage.shape[0] lines
    # eyeImage.shape[1] columns
    center = (eyeImage.shape[0] / 2, eyeImage.shape[1] / 2)
    aspectRatio = center[1]/center[0]
    baseKSize = 9
    blurKSize = (baseKSize,baseKSize)

    processedImage = eyeImage
    processedImage = cv2.GaussianBlur(processedImage, blurKSize, blurKSize[0]/2,blurKSize[1]/2)  # cv2.GaussianBlur(eyeImage, (9, 9), 2, 2)

    if showProcess: showImage(processedImage, "Blurred Iris Image")

    # do not offer a really good improvement
    #processedImage = cv2.Canny(processedImage, 5, 70, 3)  # cv2.Canny(processedImage, 55, 60,3)#
    #if showProcess: showImage(processedImage, "Canny Iris Image")

    print "primeira tentativa da pupila"
    # HoughCircles(gray, circles, CV_HOUGH_GRADIENT,2, gray->rows/4, 200, 100 );//center[0] / 2
    objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200, 100)
    # objCircles = cv2.HoughCircles(eyeImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200, 100)

    if objCircles is None:
        print "segunda tentativa da pupila"
        objCircles = cv2.HoughCircles(eyeImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200, 100)

    if objCircles is None:
        raise Exception("No Circles were found")
    elif objCircles.__len__() > 0:
        circles = objCircles[0]
        if circles.__len__() > 0:
            circle = circles[0]
            if circles.__len__() > 1:
                print("found "+str(circles.__len__())+" circles")
                lastDistance = __distanceBetweenPoints(center[0], center[1], circles[0][0], circles[0][1])
                for i in circles:
                    d = __distanceBetweenPoints(center[0], center[1], i[0], i[1])
                    if d < lastDistance:
                        lastDistance = d
                        circle = i
            return circle
    return objCircles

#make all initial images work
# working
def __pupilCircleOnImageV1(eyeImage,showProcess):
   return __pupilCircleOnImage(eyeImage,showProcess)


#make all initial images work on first trial
# working
def __pupilCircleOnImageV1_5(eyeImage,showProcess):
    if showProcess : showImage(eyeImage, "Original Iris Image")

    center = (eyeImage.shape[0] / 2, eyeImage.shape[1] / 2)
    baseKSize = 9
    blurKSize = (baseKSize,baseKSize)

    processedImage = eyeImage
    processedImage = cv2.GaussianBlur(processedImage, blurKSize, 3,3)# change

    if showProcess: showImage(processedImage, "Blurred Iris Image")


    print "primeira tentativa da pupila"
    objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200, 100)

    if objCircles is None:
        print "segunda tentativa da pupila"
        objCircles = cv2.HoughCircles(eyeImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200, 100)

    if objCircles is None:
        raise Exception("No Circles were found")
    elif objCircles.__len__() > 0:
        circles = objCircles[0]
        if circles.__len__() > 0:
            circle = circles[0]
            if circles.__len__() > 1:
                print("found "+str(circles.__len__())+" circles")
                lastDistance = __distanceBetweenPoints(center[0], center[1], circles[0][0], circles[0][1])
                for i in circles:
                    d = __distanceBetweenPoints(center[0], center[1], i[0], i[1])
                    if d < lastDistance:
                        lastDistance = d
                        circle = i
            return circle
    return objCircles



#make all other images work
def __pupilCircleOnImageV2(eyeImage,showProcess=False):
    width = eyeImage.shape[1]
    height = eyeImage.shape[0]
    average = np.median(eyeImage)
    center = (width / 2, height / 2)  # change on 2 fixing

    if showProcess : showImage(eyeImage, "Original Iris Image")

    baseKSize = 9
    blurKSize = (baseKSize,baseKSize)
    #radius = width - 50
    #if height < width: radius = height
    #cv2.circle(processedImage, center, radius/2, (0, 0, 0), -1, 8,0)
    #cv2.ellipse(processedImage,center,(radius/2,radius/3),0,0,360,(255, 255, 255),-1,8)
    #cv2.rectangle(processedImage,(center[0] - radius/2,center[1] - radius/2),(center[0] + radius/2,center[1] + radius/2),(255, 255, 255),-1,8)
    #processedImage = eyeImage - processedImage
    #if showProcess: showImage(processedImage, "cutted Iris Image")

    # // Homogeneous
    # blur:
    # blur(image, dstHomo, Size(kernel_length, kernel_length), Point(-1, -1));
    # // Gaussian
    # blur:
    # GaussianBlur(image, dstGaus, Size(kernel_length, kernel_length), 0, 0);
    # // Median
    # blur:
    # medianBlur(image, dstMed, kernel_length);
    # // Bilateral
    # blur:
    # bilateralFilter(image, dstBila, kernel_length, kernel_length * 2, kernel_length / 2);

    print "primeira tentativa da pupila"

    processedImage = cv2.GaussianBlur(eyeImage, blurKSize, 3,3)# change on 1_5
    #processedImage = cv2.bilateralFilter(processedImage,30,50,100,25)
    #processedImage  = cv2.medianBlur(processedImage,7)
    #processedImage = cv2.blur(processedImage,(5,5),(-1,-1))

    if showProcess: showImage(processedImage, "Gaussian Blurred Iris Image")

    #average = np.median(processedImage)
    #processedImage = cv2.inRange(processedImage,0,average)#inRange(original, Scalar(30,30,30), Scalar(80,80,80), mask_pupil);
    #if showProcess: showImage(processedImage, "Teste Image")

    # # do not offer a really good improvement
    # v = np.median(eyeImage)
    # # apply automatic Canny edge detection using the computed median
    # lower = int(max(0, (1.0 - 0.33) * v))
    # upper = int(min(255, (1.0 - 0.33) * v))
    #
    # processedImage = cv2.Canny(processedImage, lower,upper, 3)#cv2.Canny(processedImage, 40,170, 3)  # cv2.Canny(processedImage, 55, 60,3)#
    # if showProcess: showImage(processedImage, "Canny Iris Image")

    objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT,2, center[0] / 2, 30, 151)#change on 2 works on all initial

    if objCircles is None:
        print "segunda tentativa da pupila"
        processedImage = cv2.bilateralFilter(eyeImage, 30, 50, 100, 25)
        if showProcess: showImage(processedImage, "Bilateral Filtered Iris Image")
        objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 30,151)

    if objCircles is None:
        print "terceira tentativa da pupila"
        processedImage = cv2.medianBlur(eyeImage, 11)#11
        if showProcess: showImage(processedImage, "Median Blurred Iris Image")
        objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT,2, center[0] / 2, 30, 151)#change on 2 works on all initial

    if objCircles is None:
        print "quarta tentativa da pupila"
        if showProcess: showImage(eyeImage, "Original Iris Image")
        objCircles = cv2.HoughCircles(eyeImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200,200)  # change on 2 works on all initial

    if objCircles is None:
        raise Exception("No Circles were found")
    elif objCircles.__len__() > 0:
        circles = objCircles[0]
        if circles.__len__() > 0:
            circle = circles[0]
            if circles.__len__() > 1:
                print("found "+str(circles.__len__())+" circles")# change on V2
                copiedImage = eyeImage.copy()
                drawCirclesOnImage(copiedImage,circles,False)
                showImage(copiedImage, "Found these ones")
            return circle
    return objCircles



#not in use
def __averageOfAreaOnCircle(image,circle):
    img = image.copy()

    y = int(circle[0]) - 1 - int(circle[2])
    x = int(circle[1]) + 5 - int(circle[2])

    crop_img = img[y:y + 2 * int(circle[2]),
               x:x + 2 * int(circle[2])]  # Crop from x, y, w, h -> 100, 200, 300, 400
    #cv2.imshow("cropped", crop_img)
    #cv2.waitKey(0)
    return np.median(crop_img)


#The image must be on gray scale
#tenta encontrar a linha formada pelas palpebras
def __eyelidsLines(eyeImage,showProcess):
    cannyImage = cv2.Canny(eyeImage,  50, 70, 3)
    if showProcess :  showImage(cannyImage,"After Apply Canny")

    lines = cv2.HoughLines(cannyImage,1,np.pi/180,1)
    if lines is None:
        raise Exception("No Lines of eyelids where found")
    print   "encontrou" + str(lines.__len__()) + " linhas"
    return lines




#-------------


#Finds the pupil on a image and draws a circle on a image presenting the pupil
def tryToShowPupil(path):
    eyeImage = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    try:
        pupilCircle = __pupilCircleOnImageV2(eyeImage, True)
        drawCirclesOnImage(eyeImage,[pupilCircle])
        showImage(eyeImage,"Circles found on Iris Image")
    except Exception, e:
        print e


def showEyeLidsOnImageAtPath(path):
    eyeImage = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    showImage(eyeImage,"Original Image")
    try:
        lines = __eyelidsLines(eyeImage, True)
        drawLinesOnImage(eyeImage,lines)
        showImage(eyeImage, "Detected Lines of eyelids")
    except Exception, e:
        print e



def segmentIrisOnImageAtPath(path):

    eyeImage = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    copyImage = eyeImage.copy()
    try:
        pupilCircle = __pupilCircleOnImageV2(copyImage,True)

        drawCirclesOnImage(copyImage,[pupilCircle],True)
        showImage(copyImage,"Painted pupil")

        irisCircle = __irisCircleOnImageV1(copyImage,pupilCircle,True)
        drawCirclesOnImage(copyImage,[irisCircle])
        showImage(copyImage,"Circles for Iris found on Iris Image")

        __irisCodification(eyeImage,pupilCircle,irisCircle,True)

    except Exception, e:
        print e







