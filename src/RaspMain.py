import IrisProcessing as irisP
import PiCameraHelper as camHelper


piTempFolderDirPath = '/home/pi/Desktop/FromPiCamera/Temp'
piDBFolderDirPath = '/home/pi/Desktop/FromPiCamera/DB'
piTestImagesPath = '/home/pi/Desktop/Images/iris'


def iris():
    ##### Iris


    # Initial
          irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L01.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R01.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L02.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R02.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L03.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R03.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L04.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R04.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R05.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L05.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R06.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L06.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R07.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L07.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L08.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R08.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L09.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R09.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001R10.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/S1001L10.jpg")
    #
    # #others
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/1.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/2.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/3.jpg")#with canny
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/4.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/5.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/6.jpg")
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/7.jpg")#not working
    #     irisP.segmentIrisOnImageAtPath("/Users/joseLucas/Desktop/Python Projects/Images/iris/others/8.jpg")#not working



def testMain():
    iris()


def raspMain():

    camHelper.defineResolution(320,280)

    #put image to gray scale
    image = camHelper.takePicture(showProcess=False)

    irisP.showImage(image,"Picture from picamera :)")

    irisP.segmentIrisOnImage(image)

    print "asd"


raspMain()