# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import savefile as savefile
import os, os.path

DIR = '/home/pi/Desktop/pictures/cadastradas'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#BOTAO DE TIRAR FOTO
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#BOTAO DE ENTRAR NO MODO CADASTRO
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#LED AZUL
GPIO.setup(17,GPIO.OUT)
#LED AMARELO
GPIO.setup(27,GPIO.OUT)

#METODO PARA LED AZUL E AMARELO FICAREM SE ALTERNANDO
#PARA SIMULAR O CARREGAMENTO DO PROCESSO
def modoProcessamento():
    GPIO.output(17,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(27,GPIO.LOW)

#METODO PARA DEIXAR OS DOIS LEDS ACESOS
#PARA SIMULAR O FIM DO PROCESSO DE CODIFICACAO
def modoFimDeProcessamento():
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)


while True:

    tira_foto = GPIO.input(18)
    modo_cadastro = GPIO.input(23)
    
    if(modo_cadastro == False):
        print("entrou no modo de cadastro")
        time.sleep(0.2)

    if(tira_foto == False):
        print("tirou uma foto")
        modoProcessamento()
        number = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        savefile.salvaImagemCodificada('iris' + str(number), 'esta imagem foi codificada por um evento no botao')
        time.sleep(0.2)         
