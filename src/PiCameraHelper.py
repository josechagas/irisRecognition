from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep

camera = PiCamera()
rawCapture = PiRGBArray(camera)
camera.rotation = 180


def defineResolution(width,height):
    camera.resolution = (width, height)

def showPreview():
    camera.start_preview()
    sleep(10)
    camera.stop_preview()


def takePicture(grayScale=False,showProcess=False):
    if grayScale: camera.color_effects = (128,128)
    if showProcess: camera.start_preview()
    sleep(0.3)
    camera.capture(rawCapture, format="bgr")
    capturedImage = rawCapture.array
    if showProcess: camera.stop_preview()
    return capturedImage


def save(image):
    print "as"
