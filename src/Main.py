# -*- coding: utf-8 -*-
import IrisRecognition as irisR
import RPi.GPIO as GPIO
import time
import savefile as savefile
import os, os.path
import numpy as np
from cv2 import imread
from cv2 import IMREAD_GRAYSCALE
from threading import Thread
from picamera import PiCamera

#Módulo Camera
camera = PiCamera()
camera.rotation = 180
camera.resolution = (320, 288)


#Onde ficará salvo a codificação e a máscara da imagem
DIR = '/home/pi/Desktop/pictures/cadastradas'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#botão de tirar foto
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#entrar no modo de cadastro
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#LED azul
GPIO.setup(17,GPIO.OUT)
#LED amarelo
GPIO.setup(27,GPIO.OUT)

#LED RGB VERDE
GPIO.setup(26,GPIO.OUT)

#LED RGB VERMELHO
GPIO.setup(19,GPIO.OUT)


stop_flag = True

def offRGB():
    GPIO.output(26,0)
    GPIO.output(19,0)

def acendeRGB(cor):
    if(cor == "verde"):
        GPIO.output(26,1)
        GPIO.output(19,0)
    else:
        GPIO.output(19,1)
        GPIO.output(26,0)
    

#Método para alternar os leds simulando o carregamento
def modoProcessamento():
    while True:
        if (stop_flag == False):
            GPIO.output(17,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(17,GPIO.LOW)
            GPIO.output(27,GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(27,GPIO.LOW)
        if (stop_flag == True):
            GPIO.output(17,GPIO.HIGH)
            GPIO.output(27,GPIO.HIGH)

#Método para deixar os leds sempre ligados simulando o fim do processamento
def modoFimDeProcessamento():
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)


def main():
    global stop_flag
    th=Thread(target=modoProcessamento, args=())
    th.start()
    camera.start_preview()
    offRGB()
    while True:

        modo_validacao = GPIO.input(23)
        modo_cadastro = GPIO.input(18)

        #Aqui entrará quando for para validar uma íris
        #Irá bater a foto, codificar e mascarar
        #Fazer a comparação com cada arquivo do banco de dados
        #Se o output for menor ou igual a 0.5 led RGB verde (liberado)
        #Se o output for maior que 0.5 led rgb vermelho (bloqueado)
        if(modo_validacao == False):
            try:
                #numero de arquivos dentro do banco
                number = ((len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))/2)

                #print("entrou no modo de validação")
                stop_flag = False
                
                #vamos supor que a imagem tirada foi essa:
                #time.sleep(0.3)
                print("nova foto")
                camera.capture('/home/pi/Desktop/pictures/temp/imagem' + str(number) + ".jpg" )
                time.sleep(3)
                camera.stop_preview()
                foto = "/home/pi/Desktop/pictures/temp/imagem" + str(number) + ".jpg"
                #foto = '/home/pi/Desktop/Images/iris/S1001L06.jpg'
                image = imread(foto, IMREAD_GRAYSCALE)

                #codificação e máscara da foto
                codAndMask = irisR.codAndMaskOfIrisImage(image)
                codIris = codAndMask[0]
                maskIris = codAndMask[1]

                #Agora iremos fazer a comparação com cada arquivo do banco de dados
                #laço para verificar cada arquivo (código e máscara)

                for i in range(number):
                    diretorioCode = DIR + '/code' + str(i+1) + ".npy"
                    diretorioMask = DIR + '/mask' + str(i+1) + ".npy"
                    arquivoIrisCode = np.load(diretorioCode, None)
                    arquivoIrisMask = np.load(diretorioMask, None)

                    #testa a independência
                    independencia = irisR.testIndependencyOf(codIris, maskIris,arquivoIrisCode,arquivoIrisMask)
                    #independencia = independencia - 0.3
                    print(float(independencia))
                    if (float(independencia) <= 0.6):
                        stop_flag = True
                        print("ACESSO LIBERADO: VERDE")
                        acendeRGB("verde")
                        time.sleep(5)
                        offRGB()
                        break

                    if (float(independencia) > 0.6):
                        stop_flag = True
                        print("ACESSO BLOQUEADO: LED VERMELHO")
                        acendeRGB("vermelho")
                        time.sleep(5)
                        offRGB()

                stop_flag = True
                time.sleep(0.2)
            except Exception, e:
                stop_flag = True
                acendeRGB("vermelho")
                time.sleep(5)
                offRGB()
                print e

        #Aqui entrará quando apertar no botão de modo cadastro
        #Deverá bater a foto e salvar a máscara e a codificação no banco de dados
        if(modo_cadastro == False):
            try:
                number = ((len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))/2)+1
                
                print("entrou no modo de cadastro")
                #acende e apaga leds
                stop_flag = False
                
                #vamos supor que a imagem tirada foi essa:
                #time.sleep(0.3)
                print("nova foto")
                camera.capture('/home/pi/Desktop/pictures/temp/imagem' + str(number) + ".jpg" )
                time.sleep(3)
                camera.stop_preview()
                foto = "/home/pi/Desktop/pictures/temp/imagem" + str(number) + ".jpg"
                #foto = '/home/pi/Desktop/Images/iris/S1001L01.jpg'
                image = imread(foto, IMREAD_GRAYSCALE)

                #codificação e máscara da foto
                codAndMask = irisR.codAndMaskOfIrisImage(image)     

                #salva no arquivo de imagens cadastrasas
                diretorioCode = DIR + '/code' + str(number)
                diretorioMask = DIR + '/mask' + str(number)
                np.save(diretorioCode,codAndMask[0])
                np.save(diretorioMask,codAndMask[1])
                
                #leds acesos
                stop_flag = True
                time.sleep(0.2)
                acendeRGB("verde")
                time.sleep(5)
                offRGB()

            except Exception, e:
                stop_flag = True
                acendeRGB("vermelho")
                time.sleep(5)
                offRGB()
                print e
            

main()




