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
def iris(baseDir):
##### Iris
## Picamera

    validateImageAtPah(baseDir+"/iris/picamera/d-1.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/e-1.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/d-2.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/e-2.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/d-3.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/e-3.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/d-4.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/e-4.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/d-5.jpg")
#    validateImageAtPah(baseDir+"/iris/picamera/e-5.jpg")





#Initial
#     validateImageAtPah(baseDir+"/iris/S1001L01.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R01.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L02.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R02.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L03.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R03.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L04.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R04.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R05.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L05.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R06.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L06.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R07.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L07.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L08.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R08.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L09.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R09.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001R10.jpg")
#     validateImageAtPah(baseDir+"/iris/S1001L10.jpg")
#
# #others
#     validateImageAtPah("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/1.jpg")
#     validateImageAtPah(baseDir+"/iris/others/2.jpg")
#     validateImageAtPah(baseDir+"/iris/others/3.jpg")#with canny
#     validateImageAtPah(baseDir+"/iris/others/4.jpg")
#     validateImageAtPah(baseDir+"/iris/others/5.jpg")
#     validateImageAtPah(baseDir+"/iris/others/6.jpg")
#     validateImageAtPah(baseDir+"/iris/others/7.jpg")#not working
#     validateImageAtPah(baseDir+"/iris/others/8.jpg")#not working
#     validateImageAtPah(baseDir+"/iris/others/9.jpg")
#     validateImageAtPah(baseDir+"/iris/others/10.jpg")#not working
#     validateImageAtPah(baseDir+"/iris/others/11.jpg")
#     validateImageAtPah(baseDir+"/iris/others/12.jpg")
#     validateImageAtPah(baseDir+"/iris/others/13.jpg")
#     validateImageAtPah(baseDir+"/iris/others/14.jpg")



def eyelids(baseDir):
## Picamera
    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/d-1.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/e-1.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/d-2.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/e-2.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/d-3.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/e-3.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/d-4.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/e-4.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/d-5.jpg")
#    testFindEyelidsOnImageAtPath(baseDir+"/iris/picamera/e-5.jpg")

#Initial
#     testFindEyelidsOnImageAtPath(baseDir+"/iris/S1001L01.jpg")
#     testFindEyelidsOnImageAtPath(baseDir+"/iris/S1001R01.jpg")
#     testFindEyelidsOnImageAtPath(baseDir+"/iris/S1001L02.jpg")
#     testFindEyelidsOnImageAtPath(baseDir+"/iris/S1001R02.jpg")
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

    #irisP.segmentationOfPupil(image,True)
    pupilCircle = irisP.segmentationOfPupilPiCam(image,True)
    blackedPupilImage = irisP.drawCirclesOnImage(image.copy(),[pupilCircle],True)
    irisCircle = irisP.findIrisInImage(blackedPupilImage,pupilCircle,True)

    return True





#--------------------------Test methods
import numpy as np
def testValidation():
    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L02.jpg", IMREAD_GRAYSCALE)
    pupilCircleA = irisP.findPupilInImage(imageA,False)
    blackedPupilImageA = irisP.drawCirclesOnImage(imageA.copy(),[pupilCircleA],True)
    irisCircleA = irisP.findIrisInImage(blackedPupilImageA,pupilCircleA,True)
    #eyeImage, pupilCircle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):

    normImgA = dataCod.RSM_NormIrisRegion(imageA,pupilCircleA,irisCircleA,20,0)
    codeA = dataCod.codificateNormImg(normImgA,True)#dataCod.codificateIrisData(imageA,pupilCircleA,irisCircleA,45,0,True)

    #maskNormImgA = irisP.maskOfNorImg(normImgA,True)
    #maskA = dataCod.codificateNormImg(maskNormImgA,True)
    maskA = irisP.maskOfNormImg(normImgA,True)
    #maskA = np.ones((codeA.shape[0],codeA.shape[1]),np.uint8)
    #maskA = np.zeros((codeA.shape[0],codeA.shape[1]),np.uint8)

    imageB = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R01.jpg", IMREAD_GRAYSCALE)
    pupilCircleB = irisP.findPupilInImage(imageB,False)
    blackedPupilImageB = irisP.drawCirclesOnImage(imageB.copy(), [pupilCircleB], True)
    irisCircleB = irisP.findIrisInImage(blackedPupilImageB, pupilCircleB, True)
    # eyeImage, pupilCircsle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):

    normImgB = dataCod.RSM_NormIrisRegion(imageB, pupilCircleB, irisCircleB, 20, 0)
    codeB = dataCod.codificateNormImg(normImgB,True)  # dataCod.codificateIrisData(imageB, pupilCircleB, irisCircleB, 45, 0, True)

    #maskNormImgB = irisP.maskOfNorImg(normImgB, True)
    #maskB = dataCod.codificateNormImg(maskNormImgB, True)
    maskB = irisP.maskOfNormImg(normImgB, True)
    #maskB = np.ones((codeA.shape[0],codeA.shape[1]),np.uint8)
    #maskB = np.zeros((codeA.shape[0],codeA.shape[1]),np.uint8)

    value = irisR.testIndependencyOf(codeA,maskA,codeB,maskB)

    isSame = value < 0.42

    print value



def testValidationPiCam():
    normalizationHeight = 20.0

    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/d-2.jpg", IMREAD_GRAYSCALE)
    pupilCircleA = irisP.segmentationOfPupilPiCam(imageA,False)
    blackedPupilImageA = irisP.drawCirclesOnImage(imageA.copy(),[pupilCircleA],False)
    irisCircleA = irisP.findIrisInImage(blackedPupilImageA,pupilCircleA,True)
    #eyeImage, pupilCircle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = Falseq):

    normImgA = dataCod.RSM_NormIrisRegion(imageA,pupilCircleA,irisCircleA,normalizationHeight,0)
    codeA = dataCod.codificateNormImg(normImgA,True)#dataCod.codificateIrisData(imageA,pupilCircleA,irisCircleA,45,0,True)

    #maskNormImgA = irisP.maskOfNorImg(normImgA,True)
    #maskA = dataCod.codificateNormImg(maskNormImgA,True)
    #maskA = np.ones((codeA.shape[0],codeA.shape[1],2),np.uint8)

    maskA =  irisP.maskOfNormImg(normImgA,True)
    #maskA = np.zeros((codeA.shape[0],codeA.shape[1]),np.uint8)
    #maskA = np.ones((codeA.shape[0],codeA.shape[1]),np.uint8)

    #imageB = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L04.jpg", IMREAD_GRAYSCALE)
    imageB = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/d-5.jpg", IMREAD_GRAYSCALE)#e-2 wrong
    pupilCircleB = irisP.segmentationOfPupilPiCam(imageB, False)
    blackedPupilImageB = irisP.drawCirclesOnImage(imageB.copy(), [pupilCircleB], False)
    irisCircleB = irisP.findIrisInImage(blackedPupilImageB, pupilCircleB, True)
    # eyeImage, pupilCircsle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    normImgB = dataCod.RSM_NormIrisRegion(imageB,pupilCircleB,irisCircleB,normalizationHeight,0)
    codeB = dataCod.codificateNormImg(normImgB,True)#dataCod.codificateIrisData(imageB, pupilCircleB, irisCircleB, 45, 0, True)


    #maskNormImgB = irisP.maskOfNorImg(normImgB,True)
    #maskB = dataCod.codificateNormImg(maskNormImgB,True)
    #maskB = np.ones((codeA.shape[0],codeA.shape[1],2),np.uint8)

    maskB =  irisP.maskOfNormImg(normImgB,True)
    #maskB = np.zeros((codeA.shape[0],codeA.shape[1]),np.uint8)
    #maskB = np.ones((codeA.shape[0],codeA.shape[1]),np.uint8)

    # codeAL = np.array([[[1,2],[3,4],[5,6],[7,8]],[[1,2],[3,4],[5,6],[7,8]]])#codeA
    # codeBL = np.array([[[1,2],[3,4],[5,6],[7,8]],[[1,2],[3,4],[5,6],[7,8]]])#codeB
    # codeAR = np.array([[[1,2],[3,4],[5,6],[7,8]],[[1,2],[3,4],[5,6],[7,8]]])#codeA
    # codeBR = np.array([[[1,2],[3,4],[5,6],[7,8]],[[1,2],[3,4],[5,6],[7,8]]])#codeB

    value = irisR.testIndependencyOf(codeA,maskA,codeB,maskB)

    isSame = value < 0.56
    print value


def testValidationMMUDB():
    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/MMU Iris Database/1/left/aeval1.bmp", IMREAD_GRAYSCALE)

    pupilCircleA = irisP.findPupilInImage(imageA,False)
    blackedPupilImageA = irisP.drawCirclesOnImage(imageA.copy(),[pupilCircleA],True)
    irisCircleA = irisP.findIrisInImage(blackedPupilImageA,pupilCircleA,True)

    normImgA = dataCod.RSM_NormIrisRegion(imageA, pupilCircleA, irisCircleA, 20, 0)
    codeA = dataCod.codificateNormImg(normImgA,True)
    maskA = irisP.maskOfNormImg(normImgA, True)

    imageB = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/MMU Iris Database/1/left/aeval2.bmp", IMREAD_GRAYSCALE)

    pupilCircleB = irisP.findPupilInImage(imageB,False)
    blackedPupilImageB = irisP.drawCirclesOnImage(imageB.copy(), [pupilCircleB], True)
    irisCircleB = irisP.findIrisInImage(blackedPupilImageB, pupilCircleB, True)

    normImgB = dataCod.RSM_NormIrisRegion(imageB, pupilCircleB, irisCircleB, 20, 0)
    codeB = dataCod.codificateNormImg(normImgB,True)
    maskB = irisP.maskOfNormImg(normImgB, True)

    value = irisR.testIndependencyOf(codeA,maskA,codeB,maskB)

    isSame = value < 0.42

    print value


def simulateValidationOfImage():
    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/e-2.jpg", IMREAD_GRAYSCALE)
    imageB = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/d-3.jpg", IMREAD_GRAYSCALE)

    try:
        valuesA = irisR.codAndMaskOfIrisImage(imageA)
        valuesB = irisR.codAndMaskOfIrisImage(imageB)
        hd = irisR.testIndependencyOf(valuesA[0],valuesA[1],valuesB[0],valuesB[1])
        return hd < 0.55
    except Exception, e:
        print e
        return False






def testGenerateMask():
    imageA = imread("/Users/joseLucas/Desktop/Python Projects/Images/iris/picamera/e-2.jpg", IMREAD_GRAYSCALE)
    pupilCircleA = irisP.segmentationOfPupilPiCam(imageA,True)
    blackedPupilImageA = irisP.drawCirclesOnImage(imageA.copy(),[pupilCircleA],True)
    irisCircleA = irisP.findIrisInImage(blackedPupilImageA,pupilCircleA,True)
    #eyeImage, pupilCircle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    normImg = dataCod.RSM_NormIrisRegion(imageA,pupilCircleA,irisCircleA,20,0)
    codeA = dataCod.codificateNormImg(normImg,True)

    irisP.maskOfNormImg(normImg,True)

    maskA = np.ones((codeA.shape[0],codeA.shape[1],2),np.uint8)



def testFindEyelidsOnImageAtPath(path):
    image = imread(path, IMREAD_GRAYSCALE)
    irisP.showImage(image,"Original Image")
    irisP.eyeLids(image,True)
    #irisP.verticalCountours(image,True)
    #irisP.horizontalCountours(image,True)

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
    macBaseDir = "/Users/joseLucas/Desktop/Python Projects/Images"
    raspBaseDir = "/home/pi/Desktop/Images"

    ###### Pupil
    #pupilV3()
    ###### Iris
    #iris(macBaseDir)
    #eyelids(macBaseDir)

    #testUsageOfFourier()
    #testValidation()
    #testSaveOfCodAndMask()
    #testLoadOfCodAndMask()
    #testValidationPiCam()
    testValidationMMUDB()
    #testGenerateMask()
    #simulateValidationOfImage()
main()



