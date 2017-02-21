import IrisProcessing as irisP
import DataCodification as dataCod
import operator

from cv2 import imread
from cv2 import IMREAD_GRAYSCALE

# def pupilV1():
# ###### Pupil
#
#      irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L01.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R01.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L02.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R02.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L03.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R03.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L04.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R04.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R05.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L05.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R06.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L06.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R07.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L07.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L09.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R09.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R10.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L10.jpg")
#
#
# def pupilV1_5():
# ###### Pupil
#
# # initial
#      irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L01.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R01.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L02.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R02.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L03.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R03.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L04.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R04.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R05.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L05.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R06.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L06.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R07.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L07.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L09.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R09.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001R10.jpg")
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/S1001L10.jpg")
#
#
#
# def pupilV2():
# ###### Pupil
#
#
# # # others
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/1.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/2.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/3.jpg")#3
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/4.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/5.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/6.jpg")#3
#      irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/7.jpg")#not working
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/8.jpg")#not working
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/9.jpg")#3
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/10.jpg")#not working
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/11.jpg")#3
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/12.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/13.jpg")#3
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/IrisRecognition/Images/iris/others/14.jpg")#3
#
# def pupilV3():
#
# ## Picamera
#
#     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/1.jpg")
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/2.jpg")
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/3.jpg")
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/4.jpg")
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/5.jpg") #not working
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/6.jpg") #not working
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/7.jpg") #not working
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/8.jpg")
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/9.jpg")
# #    irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/10.jpg")
#
# # # others
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/1.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/2.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/3.jpg")#3
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/4.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/5.jpg")#2
# #     irisP.tryToShowPupil("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/6.jpg")#3
#
def iris():
##### Iris
## Picamera

    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/1.jpg")
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/2.jpg")
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/3.jpg")
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/4.jpg")
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/5.jpg") #not working
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/6.jpg") #not working
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/7.jpg") #not working
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/8.jpg")
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/9.jpg")
#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/10.jpg")


#Initial
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R01.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L02.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R02.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L03.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R03.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L04.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R04.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R05.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L05.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R06.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L06.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R07.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L07.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L08.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R08.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L09.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R09.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R10.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L10.jpg")
#
# #others
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/1.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/2.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/3.jpg")#with canny
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/4.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/5.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/6.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/7.jpg")#not working
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/8.jpg")#not working
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/9.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/10.jpg")#not working
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/11.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/12.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/13.jpg")
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/14.jpg")



def eyelids():
##### Iris

#Initial
    testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R01.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L02.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R02.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L03.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R03.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L04.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R04.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R05.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L05.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R06.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L06.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R07.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L07.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L08.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R08.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L09.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R09.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R10.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L10.jpg")
#
# #others
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/1.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/2.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/3.jpg")#with canny
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/4.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/5.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/6.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/7.jpg")#not working
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/8.jpg")#not working
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/9.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/10.jpg")#not working
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/11.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/12.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/13.jpg")
#     testFindEyelidsOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/14.jpg")



def validateImageAtPah(path):

    image = imread(path, IMREAD_GRAYSCALE)
    # pupilCircle = irisP.findPupilInImage(image,True)
    # blackedPupilImage = irisP.drawCirclesOnImage(image.copy(),[pupilCircle],True)
    # irisCircle = irisP.findIrisInImage(blackedPupilImage,pupilCircle,True)
    # #eyeImage, pupilCircle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    # code = dataCod.codificateIrisData(image,pupilCircle,irisCircle,40,0,True)

    irisP.showImage(image,"Original Image")
    irisP.segmentationOfIris(image,True)

    return True


# https://docs.python.org/2/library/operator.html
# Teste de indenependencia proposto por Daugman
# Distancia de Hamming(Hamming Distance)
#mais proximo de zero maior a possibilidade de serem iguais
#Ex hd < 0.5 (mesma iris) hd > 0.5 (iris diferente)
def testIndependencyOf(codeA,maskA,codeB,maskB):
    rows = codeA.shape[0]
    cols = codeA.shape[1]
    # for row in range(0,rows):
    #     for col in range(0,cols):
    #hd2 = (operator.xor(codeA,codeB) & maskA & maskB)/(maskA & maskB)
    #hd3 = (operator.xor(codeA.sum(),codeB.sum()) & maskA.sum() & maskB.sum())/(maskA.sum() & maskB.sum())
    hd = 0
    for row in range(0,rows):
        for col in range(0,cols):
            for i in range(0,1):
                a = codeA[row][col][i]
                b = codeB[row][col][i]
                ma = maskA[row][col][i]
                mb = maskB[row][col][i]
                hd += (operator.xor(a,b) & ma & mb)/(ma & mb)
    return hd/10000.0



#--------------------------Test methods
import numpy as np
def testValidation():
    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg", IMREAD_GRAYSCALE)
    pupilCircleA = irisP.findPupilInImage(imageA,True)
    blackedPupilImageA = irisP.drawCirclesOnImage(imageA.copy(),[pupilCircleA],True)
    irisCircleA = irisP.findIrisInImage(blackedPupilImageA,pupilCircleA,True)
    #eyeImage, pupilCircle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    codeA = dataCod.codificateIrisData(imageA,pupilCircleA,irisCircleA,45,0,True)
    maskA = np.ones((codeA.shape[0],codeA.shape[1],2),np.uint8)

    imageB = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L05.jpg", IMREAD_GRAYSCALE)
    pupilCircleB = irisP.findPupilInImage(imageB, True)
    blackedPupilImageB = irisP.drawCirclesOnImage(imageB.copy(), [pupilCircleB], True)
    irisCircleB = irisP.findIrisInImage(blackedPupilImageB, pupilCircleB, True)
    # eyeImage, pupilCircsle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    codeB = dataCod.codificateIrisData(imageB, pupilCircleB, irisCircleB, 45, 0, True)
    maskB = np.ones((codeA.shape[0],codeA.shape[1],2),np.uint8)

    value = testIndependencyOf(codeA,maskA,codeB,maskB)

def testFindEyelidsOnImageAtPath(path):
    image = imread(path, IMREAD_GRAYSCALE)
    irisP.showImage(image,"Original Image")
    irisP.findEyelidsInImage(image,True)

def testUsageOfFourier():

    #imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg", IMREAD_GRAYSCALE)
    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/1.jpg", IMREAD_GRAYSCALE)

    value = dataCod.CV2_fourierTransformOf(imageA, True)

    data = dataCod.CV2_invertFourierTransformOf(value)

#-------------------------

def main():
    print "ola"


    ###### Pupil
    #pupilV3()
    ###### Iris
    iris()
    #eyelids()

    #testUsageOfFourier()
    #testValidation()
main()



