import numpy as np
import cv2
import math
#import scipy.integrate as integrate

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
    for i in circles[0:]:
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
def drawRectangleOnImage(image,topLeftPoint,width,height,filled=False):
    thickness = 2
    if filled: thickness = -1
    bottomRightPoint = (topLeftPoint[0]+width,topLeftPoint[1]+height)
    cv2.rectangle(image,topLeftPoint,bottomRightPoint,(255,255,255),thickness)


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

# this method return the corresponding point(x,y) for some angle on the border of circle
def __maxPointsOfCircleForAngle(circle,angle):
    r = circle[2]
    centerX = circle[0]
    centerY = circle[1]
    x = int(centerX + r * math.cos(angle * math.pi / 180))
    y = int(centerY + r * math.sin(angle * math.pi / 180))
    return(x,y)

def __pixelsOfCircle(image,circle,showProcess=False):
    lins = int(circle[2])  # int(irisCircle[2] - pupilCircle[2])
    cols = 360#int((irisCircle[2] - pupilCircle[2]) + 2)
    circleData = np.zeros((lins, cols), np.uint8)

    for ri in range(0,lins):
        line = np.zeros(360, np.uint8)
        for angle in range(0,cols):
            x = int(circle[0] + ri*math.cos(angle*math.pi/180))
            y = int(circle[1] + ri * math.sin(angle * math.pi / 180))
            line[angle] = image[y][x]
        circleData[ri] = line

    if showProcess: showImage(circleData,"Pixels on Circle")
    return circleData

#-------------------- Find Iris methods


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

def __irisCircleOnImageV1(eyeImage,pupilCircle,showProcess=False):
    # eyeImage.shape[0] lines
    # eyeImage.shape[1] columns


    blackedPupilEyeImage = eyeImage.copy()
    drawCirclesOnImage(blackedPupilEyeImage,[pupilCircle],True)

    if showProcess: showImage(blackedPupilEyeImage, "Painted pupil")

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
    #return [int(pupilCircle[0] + 15),int(pupilCircle[1] + 6),bestIrisCircle[2]]#fixing some deviation on center

#raspcamera
def __irisCircleOnImageRaspCam(eyeImage,pupilCircle,showProcess=False):
    blackedPupilEyeImage = eyeImage.copy()
    rect = rectangleOfCircle(pupilCircle,(2,2))
    drawRectangleOnImage(blackedPupilEyeImage,(rect[0],rect[1]),rect[2],rect[3],True)

    if showProcess: showImage(blackedPupilEyeImage, "Painted pupil")

    yInitial = int(pupilCircle[1] - 2*pupilCircle[2])
    yFinal = int(pupilCircle[1] + 2*pupilCircle[2])
    xInitial = int(pupilCircle[0] - 2*pupilCircle[2])
    xFinal = int(pupilCircle[0] + 2*pupilCircle[2])
    blackedPupilEyeImage = blackedPupilEyeImage[yInitial:yFinal,xInitial:xFinal]
    if showProcess: showImage(blackedPupilEyeImage, "cutted pupil image")


    center = (blackedPupilEyeImage.shape[0] / 2, blackedPupilEyeImage.shape[1] / 2)
    #processedImage = cv2.medianBlur(blackedPupilEyeImage, 11)
    processedImage = cv2.bilateralFilter(blackedPupilEyeImage, 30, 10, 100, 25)
    #processedImage = cv2.GaussianBlur(blackedPupilEyeImage, (9,9), 3, 3)  # change on 1_5

    #processedImage = cv2.medianBlur(blackedPupilEyeImage,11)
    #processedImage = cv2.bilateralFilter(processedImage, 30, 10, 100, 25)
    if showProcess: showImage(processedImage, "Median Blurred Iris Image")

    i = 30
    max = 100
    bestIrisCircle = None
    while (i < max and bestIrisCircle is None):
        print "tentativa "+str(i - 30)
        objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 200, i, pupilCircle[2],int(pupilCircle[2] + 20))#
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

    drawCirclesOnImage(blackedPupilEyeImage,[bestIrisCircle])
    showImage(blackedPupilEyeImage,"asd")

    #return bestIrisCircle

    return np.array([bestIrisCircle[0] + xInitial,bestIrisCircle[1] + yInitial,bestIrisCircle[2]],np.float32)

    #return [pupilCircle[0],pupilCircle[1],bestIrisCircle[2]]#fixing some deviation on center


#-------------------------------------------------------------------

#-------------------- Find pupil methods

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
# this is for casia images
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

def __pupilCircleOnImageV3(eyeImage,showProcess=False):
    width = eyeImage.shape[1]
    height = eyeImage.shape[0]
    average = np.median(eyeImage)
    center = (width / 2, height / 2)  # change on 2 fixing

    if showProcess : showImage(eyeImage, "Original Iris Image")

    #processedImage = cv2.medianBlur(eyeImage, 11)
    kernel = np.ones((20, 20), np.uint8)
    #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    processedImage = cv2.dilate(eyeImage,kernel,1)
    #processedImage = cv2.erode(processedImage,kernel,1)
    processedImage = cv2.morphologyEx(eyeImage, cv2.MORPH_CLOSE, kernel)
    #processedImage = cv2.morphologyEx(processedImage, cv2.MORPH_GRADIENT, kernel)
    if showProcess: showImage(processedImage, "preprocessed binary Image")

    processedImage = cv2.Canny(processedImage, 150, 150, 30)
    if showProcess:  showImage(processedImage, "After Apply Canny")


    objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, width, 150, 60,1,5)

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

#this is for picamera
def __pupilCircleOnImageRaspCam(eyeImage,showProcess=False):
    width = eyeImage.shape[1]
    height = eyeImage.shape[0]
    average = np.median(eyeImage)
    center = (width / 2, height / 2)  # change on 2 fixing

    if showProcess : showImage(eyeImage, "Original Iris Image")

    print "primeira tentativa da pupila"
    #processedImage = cv2.Canny(eyeImage, 150, 50, 3)
    #if showProcess:  showImage(processedImage, "After Apply Canny")

    preprocessedImage = cv2.inRange(eyeImage,0,average+average*0.3)
    if showProcess: showImage(preprocessedImage, "preprocessed binary Image")
    processedImage = eyeImage*(preprocessedImage/255)

    if showProcess: showImage(processedImage, "preprocessed Image")

    processedImage = cv2.medianBlur(processedImage, 11)

    #processedImage = cv2.bilateralFilter(eyeImage, 30, 10, 100, 25)
    #processedImage = cv2.GaussianBlur(eyeImage, (9,9), 3, 3)  # change on 1_5

    #processedImage = cv2.medianBlur(eyeImage,11)
    #processedImage = cv2.bilateralFilter(processedImage, 30, 10, 100, 25)

    if showProcess: showImage(processedImage, "Median Blurred Iris Image")
    # processedImage = cv2.Canny(processedImage, 50, 70, 3)
    # if showProcess:  showImage(processedImage, "After Apply Canny")
    # objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT,2, center[0] / 2, 30, 151)#change on 2 works on all initial
    #objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 100, 127, 1,10)
    #objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 100, 9, 1,5)
    #objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, width, 100, 9, 1,5)

    #objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, width, 100, 100, 1,5)
    #objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, width, 100, 60, 1,5)
    objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, width, 150, 60,1,5)

    if objCircles is None:
        print "segunda tentativa da pupila"
        #processedImage = cv2.bilateralFilter(eyeImage, 30, 50, 100, 25)
        processedImage = cv2.bilateralFilter(eyeImage, 30, 10, 100, 25)
        if showProcess: showImage(processedImage, "Bilateral Filtered Iris Image")
        objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, width, 100, 60, 1, 5)

    if objCircles is None:
        print "terceira tentativa da pupila"
        baseKSize = 9
        blurKSize = (baseKSize, baseKSize)

        processedImage = cv2.GaussianBlur(eyeImage, blurKSize, 3, 3)  # change on 1_5

        if showProcess: showImage(processedImage, "Gaussian Blurred Iris Image")

        objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 30,
                                      151)  # change on 2 works on all initial
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

#-------------------------------------------------------------------

#-------------------- Find Eyelids methods

#The image must be on gray scale
#tenta encontrar a linha formada pelas palpebras
def __eyelidsLines(eyeImage,showProcess):
    cannyImage = cv2.Canny(eyeImage,  50, 70, 3)
    if showProcess :  showImage(cannyImage,"After Apply Canny")

    lines = cv2.HoughLines(cannyImage,1,np.pi/180,1)
    if lines is None:
        raise Exception("No Lines of eyelids where found")
    print   "encontrou " + str(lines.__len__()) + " linhas"
    return lines

#-------------------- Public methods

def findEyelidsInImage(eyeImage,showProcess=False):
    try:

        lines = __eyelidsLines(eyeImage, showProcess)
        if showProcess:
            copy = eyeImage.copy()
            drawLinesOnImage(copy, lines)
            showImage(copy, "Detected Lines of eyelids")
        return lines
    except Exception, e:
        print e

#Tries to find the pupil location on a image and returns it
def findPupilInImage(image,showProcess=False):
    try:
        pupilCircle = __pupilCircleOnImageV2(image, showProcess)
        if showProcess:
            copy = image.copy()
            drawCirclesOnImage(copy, [pupilCircle])
            showImage(copy, "Location of pupil")
        return pupilCircle
    except Exception, e:
        print e

# Tries to find the pupil location on a image and returns it
def findPupilInImageAtPath(path, showProcess=False):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    try:
        pupilCircle = __pupilCircleOnImageV2(image, showProcess)
        if showProcess:
            copy = image.copy()
            drawCirclesOnImage(copy, [pupilCircle])
            showImage(copy, "Location of pupil")
        return pupilCircle
    except Exception, e:
        print e


#This image has the pupil region blacked
def findIrisInImage(image,pupilCircle,showProcess=False):

    irisCircle = __irisCircleOnImageV1(image,pupilCircle,showProcess)
    if showProcess:
        copy = image.copy()
        drawCirclesOnImage(copy, [irisCircle])
        showImage(copy, "Location of Iris")
    return irisCircle

def findIrisInImageAtPath(path,pupilCircle,showProcess=False):

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    irisCircle = __irisCircleOnImageV1(image,pupilCircle,showProcess)
    if showProcess:
        copy = image.copy()
        drawCirclesOnImage(copy, [irisCircle])
        showImage(copy, "Location of Iris")
    return irisCircle


def segmentationOfIris(eyeImage,showProcess=False):
    #processedImage = cv2.equalizeHist(eyeImage)

    #if showProcess:  showImage(equalized, "After Histogram Equalization")

    #processedImage = cv2.Canny(equalized, 40, 40,3)

    #if showProcess:  showImage(processedImage, "After Apply Canny")

    #processedImage = cv2.medianBlur(eyeImage, 11)

    #processedImage = cv2.bilateralFilter(processedImage, 30, 10, 100, 25)
    #processedImage = cv2.medianBlur(eyeImage, 11)
    #processedImage = cv2.GaussianBlur(eyeImage, (9,9), 3, 3)  # change on 1_5

    processedImage = cv2.medianBlur(eyeImage,11)
    processedImage = cv2.bilateralFilter(processedImage, 30, 10, 100, 25)
    if showProcess:  showImage(processedImage, "After Apply Bilateral filter")
    processedImage = cv2.Canny(processedImage, 10, 100,3)

    if showProcess:  showImage(processedImage, "After Apply Canny")

    width = eyeImage.shape[1]
    height = eyeImage.shape[0]
    center = (width / 2, height / 2)
    #objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 2, 30,151) #near eyeimage
    objCircles = cv2.HoughCircles(processedImage, cv2.HOUGH_GRADIENT, 2, center[0] / 4, 30,150)

    if objCircles is None:
        print "nenhum circulo encontrado"
    elif objCircles.__len__() > 0:
        circles = objCircles[0]
        if circles.__len__() > 0:
            circle = circles[0]
            copiedImage = eyeImage.copy()
            drawCirclesOnImage(copiedImage, circles, False)
            showImage(copiedImage, "Found these ones")
            return circle
    return objCircles