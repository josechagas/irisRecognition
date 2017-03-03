import IrisProcessing as irisP
import DataCodification as dataCod
import operator
import IrisRecognition as irisR

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

#    validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/1.jpg")
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
     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/2.jpg")
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
    irisP.showImage(image,"Original Image")

    #irisP.eyeLids(image,True)
    #irisP.verticalCountours(image,True)

    #irisP.showImage(image,"Original Image")
    #irisP.horizontalCountours(image,True)

    #irisP.countours(image,True)

    irisP.segmentationOfPupil(image,True)

    return True





#--------------------------Test methods
import numpy as np
def testValidation():
    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg", IMREAD_GRAYSCALE)
    pupilCircleA = irisP.findPupilInImage(imageA,False)
    blackedPupilImageA = irisP.drawCirclesOnImage(imageA.copy(),[pupilCircleA],False)
    irisCircleA = irisP.findIrisInImage(blackedPupilImageA,pupilCircleA,False)
    #eyeImage, pupilCircle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    codeA = dataCod.codificateIrisData(imageA,pupilCircleA,irisCircleA,45,0,False)
    maskA = np.ones((codeA.shape[0],codeA.shape[1],2),np.uint8)

    imageB = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L05.jpg", IMREAD_GRAYSCALE)
    pupilCircleB = irisP.findPupilInImage(imageB, False)
    blackedPupilImageB = irisP.drawCirclesOnImage(imageB.copy(), [pupilCircleB], False)
    irisCircleB = irisP.findIrisInImage(blackedPupilImageB, pupilCircleB, False)
    # eyeImage, pupilCircsle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    codeB = dataCod.codificateIrisData(imageB, pupilCircleB, irisCircleB, 45, 0, False)
    maskB = np.ones((codeA.shape[0],codeA.shape[1],2),np.uint8)

    value = irisR.testIndependencyOf(codeA,maskA,codeB,maskB)
    print value

def testFindEyelidsOnImageAtPath(path):
    image = imread(path, IMREAD_GRAYSCALE)
    irisP.showImage(image,"Original Image")
    irisP.findEyelidsInImage(image,True)

def testUsageOfFourier():

    #imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg", IMREAD_GRAYSCALE)
    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/1.jpg", IMREAD_GRAYSCALE)

    value = dataCod.CV2_fourierTransformOf(imageA, True)

    data = dataCod.CV2_invertFourierTransformOf(value)

def testSaveOfCodAndMask():
    image = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg", IMREAD_GRAYSCALE)

    values = irisR.codAndMaskOfIrisImage(image)

    code = values[0]
    mask = values[1]

    np.save("/Users/joseLucas/Desktop/Python Projects/code_1",code,False,False)


def testLoadOfCodAndMask():
    image = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg", IMREAD_GRAYSCALE)

    values = irisR.codAndMaskOfIrisImage(image)

    code = values[0]
    mask = values[1]

    loadedCode = np.load("/Users/joseLucas/Desktop/Python Projects/code_1.npy",None,False,False)

#-------------------------

def main():
    print "ola DEV-MAIN"


    ###### Pupil
    #pupilV3()
    ###### Iris
    iris()
    #eyelids()

    #testUsageOfFourier()
    #testValidation()
    #testSaveOfCodAndMask()
    #testLoadOfCodAndMask()
main()



