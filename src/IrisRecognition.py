# This file contains the methods that check if some iris image is a valid one and cadastrate a new one


import IrisProcessing as irisP
import DataCodification as dataCod
import operator
import numpy as np


# https://docs.python.org/2/library/operator.html
# Teste de indenependencia proposto por Daugman
# Distancia de Hamming(Hamming Distance)
#mais proximo de zero maior a possibilidade de serem iguais
#Ex hd < 0.5 (mesma iris) hd > 0.5 (iris diferente)

#This method determines using the Distance of Hamming the independency of two normalized and codificated iris images
def testIndependencyOf(codeA,maskA,codeB,maskB):
    rows = codeA.shape[0]
    cols = codeA.shape[1]
    #hd2 = (operator.xor(codeA,codeB) & maskA & maskB)/(maskA & maskB)
    #hd3 = (operator.xor(codeA.sum(),codeB.sum()) & maskA.sum() & maskB.sum())/(maskA.sum() & maskB.sum())
    hd = 0
    #old way (working)
    # for row in range(0,rows):
    #     for col in range(0,cols):
    #         for i in range(0,1):
    #             a = codeA[row][col][i]
    #             b = codeB[row][col][i]
    #             ma = maskA[row][col][i]
    #             mb = maskB[row][col][i]
    #             hd += (operator.xor(a,b) & ma & mb)/(ma & mb)

    #improved way (working)
    for row in range(0,rows):
        for col in range(0,cols/2):
            for i in range(0,1):
                a = codeA[row][col][i]
                b = codeB[row][col][i]
                ma = maskA[row][col][i]
                mb = maskB[row][col][i]
                hd += (operator.xor(a,b) & ma & mb)/(ma & mb)

                delta = (cols/2) + col
                a = codeA[row][delta][i]
                b = codeB[row][delta][i]
                ma = maskA[row][delta][i]
                mb = maskB[row][delta][i]
                hd += (operator.xor(a,b) & ma & mb)/(ma & mb)


    return hd/10000.0




#Esse metodo fara a verificacao se a imagem capturada e uma imagem de iris valida ou nao
#Apos gerar o codigo e mascara da imagem capturada esse metodo lera todos os arquivos com iris salvas comparando-as usando
#o metodo testIndependencyOf
#Esse metodo tem como output true ou false para indicar se e uma iris valida ou nao
def isItAValidIrisImage(irisImage):

    data = codAndMaskOfIrisImage(irisImage)

    #After getting codeA and maskA we need to pass for all saved images and try to find some one that is compatible
    #Remenbar to execute it on more than one thread
    # for each code and mask loaded from server call this methods
    # testIndependencyOf(codeA,maskA,codeB,maskB)
    return True

#Esse metodo pega uma imagem de iris e tenta, pois se nao encontrar a iris ou pupila nao sera possivel, gerar o codigo
# da iris na imagem e sua respectiva mascara
#Esse metodo retorna uma tupla (codigo, mascara) da imagem passada como parametro
def codAndMaskOfIrisImage(irisImage):

    pupilCircle = irisP.findPupilInImage(irisImage,True)
    blackedPupilImage = irisP.drawCirclesOnImage(irisImage.copy(),[pupilCircle],True)
    irisCircle = irisP.findIrisInImage(blackedPupilImage,pupilCircle,True)
    #eyeImage, pupilCircle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    codeA = dataCod.codificateIrisData(irisImage,pupilCircle,irisCircle,40,0,True)
    maskA = np.ones((codeA.shape[0],codeA.shape[1],2),np.uint8)
    return (codeA,maskA)


#Esse metodo salva uma nova imagem de iris
#Primeiramente ele tentara gera o codigo e a mascara para a imagem passada
#e depois salvara os dados
#Esse metodo possui como output True ou False para indicar se o processo foi realizado com sucesso ou nao
def saveIrisOfImage(irisImage):
    data = codAndMaskOfIrisImage(irisImage)

    #parte de salvar

    return True