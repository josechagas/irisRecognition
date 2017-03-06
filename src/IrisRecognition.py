# This file contains the methods that check if some iris image is a valid one and cadastrate a new one


import IrisProcessing as irisP
import DataCodification as dataCod
import operator
import numpy as np



def __HammingDistanceOf(codeA,maskA,codeB,maskB):
    rows = codeA.shape[0]
    cols = codeA.shape[1]
    #hd2 = (operator.xor(codeA,codeB) & maskA & maskB)/(maskA & maskB)
    #hd3 = (operator.xor(codeA.sum(),codeB.sum()) & maskA.sum() & maskB.sum())/(maskA.sum() & maskB.sum())
    hd1 = 0
    #old way (working)
    # for row in range(0,rows):
    #     for col in range(0,cols):
    #         for i in range(0,2):
    #             a = codeA[row][col][i]
    #             b = codeB[row][col][i]
    #             ma = maskA[row][col][i]
    #             mb = maskB[row][col][i]
    #             hd += (operator.xor(a,b) & ma & mb)/(ma & mb)
    #improved way (working)
    # for row in range(0,rows):
    #     for col in range(0,cols/2):
    #
    #         for i in range(0,2):
    #             a = codeA[row][col][i]
    #             b = codeB[row][col][i]
    #             ma = maskA[row][col]#[i]
    #             mb = maskB[row][col]#[i]
    #             hd1 += (operator.xor(a,b) & (ma & mb))#/(ma & mb)
    #
    #             delta = (cols/2) + col
    #             a = codeA[row][delta][i]
    #             b = codeB[row][delta][i]
    #             ma = maskA[row][delta]#[i]
    #             mb = maskB[row][delta]#[i]
    #             hd1 += (operator.xor(a,b) & (ma & mb))#/(ma & mb)

    # hd1_maxValue = (codeA.shape[0]*codeA.shape[1]*codeA.shape[2]) - (maskA.shape[0]*maskA.shape[1] - (maskA & maskB).sum())
    # hd = hd1/hd1_maxValue #10000.0
    mask_maxValue = float((maskA & maskB).sum())
    # hdx = hd1/mask_maxValue
    # hdy =hd1/(2*mask_maxValue)

    hdp = np.zeros((maskA.shape[0],maskA.shape[1],2),np.uint8)
    #hdp = np.zeros((maskA.shape[0],maskA.shape[1]),np.uint8)
    for row in range(0,rows):
        hdLine = np.zeros((maskA.shape[1],2),np.uint8)
        #hdLine = np.zeros((maskA.shape[1]),np.uint8)
        for col in range(0,cols/2):
            a = codeA[row][col]
            b = codeB[row][col]
            ma = maskA[row][col]
            mb = maskB[row][col]
            hdLine[col] = operator.xor(a,b)#np.amax(operator.xor(a,b))
            if (ma & mb) == 0: hdLine[col] = [0,0]

            delta = (cols/2) + col
            a = codeA[row][delta]
            b = codeB[row][delta]
            ma = maskA[row][delta]
            mb = maskB[row][delta]
            hdLine[delta] = operator.xor(a, b)
            if (ma & mb) == 0: hdLine[delta] = [0, 0]
        hdp[row] = hdLine

    hdt = hdp.sum()/(2*mask_maxValue)




    #hd2s = (operator.xor(codeA, codeB).sum() & (maskA & maskB).sum()) / float((maskA & maskB).sum())
    hd2s = (operator.xor(codeA, codeB).sum() & (maskA & maskB).sum()) / mask_maxValue
    hd2s2 = (operator.xor(np.reshape(codeA,(45,360*2)), np.reshape(codeB,(45,360*2))).sum() & (maskA & maskB).sum()) / mask_maxValue

    return hdt


# https://docs.python.org/2/library/operator.html
# Teste de indenependencia proposto por Daugman
# Distancia de Hamming(Hamming Distance)
#mais proximo de zero maior a possibilidade de serem iguais
#Ex hd < 0.5 (mesma iris) hd > 0.5 (iris diferente)

#This method determines using the Distance of Hamming the independency of two normalized and codificated iris images
def testIndependencyOf(codeA,maskA,codeB,maskB):
    # left and right shift are executed to give more precision
    codeAL = np.roll(codeA,-2)#left
    maskAL = np.roll(maskA,-2)#left
    #codeBL = np.roll(codeB,-2)#left

    codeAR = np.roll(codeA,2)#right
    maskAR = np.roll(maskA,2)#right
    #codeBR = np.roll(codeB,2)#right

    value = __HammingDistanceOf(codeA,maskA,codeB,maskB)
    valueLeftShift = __HammingDistanceOf(codeAL,maskAL,codeB,maskB)
    valueRightShift = __HammingDistanceOf(codeAR,maskAR,codeB,maskB)

    values = [value,valueLeftShift,valueRightShift]
    average = (value + valueLeftShift + valueRightShift)/3.0
    smallerValue = np.amin(values)

    return smallerValue






#Esse metodo fara a verificacao se a imagem capturada e uma imagem de iris valida ou nao
#Apos gerar o codigo e mascara da imagem capturada esse metodo lera todos os arquivos com iris salvas comparando-as usando
#o metodo testIndependencyOf
#Esse metodo tem como output true ou false para indicar se e uma iris valida ou nao
def isItAValidIrisImage(irisImage,showProcess=False):

    data = codAndMaskOfIrisImage(irisImage,showProcess)

    #After getting codeA and maskA we need to pass for all saved images and try to find some one that is compatible
    #Remenbar to execute it on more than one thread
    # for each code and mask loaded from server call this methods
    # testIndependencyOf(codeA,maskA,codeB,maskB)
    return True

#Esse metodo pega uma imagem de iris e tenta, pois se nao encontrar a iris ou pupila nao sera possivel, gerar o codigo
# da iris na imagem e sua respectiva mascara
#Esse metodo retorna uma tupla (codigo, mascara) da imagem passada como parametro
def codAndMaskOfIrisImage(irisImage,showProcess=False):

    #pupilCircle = irisP.findPupilInImage(irisImage,showProcess) CASIA
    pupilCircle = irisP.findPupilInRaspImage(irisImage,showProcess)

    blackedPupilImage = irisP.drawCirclesOnImage(irisImage.copy(),[pupilCircle],showProcess)
    irisCircle = irisP.findIrisInImage(blackedPupilImage,pupilCircle,showProcess)
    #eyeImage, pupilCircle, irisCircle, numbOfLins = 10, pupilOffset = 0, showProcess = False):
    normImg = dataCod.RSM_NormIrisRegion(irisImage, pupilCircle, irisCircle, 45, 0)
    code = dataCod.codificateNormImg(normImg,showProcess)

    mask = irisP.maskOfNormImg(normImg,showProcess)
    #mask = np.ones((code.shape[0],code.shape[1],2),np.uint8)

    return (code,mask)


#Esse metodo salva uma nova imagem de iris
#Primeiramente ele tentara gera o codigo e a mascara para a imagem passada
#e depois salvara os dados
#Esse metodo possui como output True ou False para indicar se o processo foi realizado com sucesso ou nao
def saveIrisOfImage(irisImage):
    data = codAndMaskOfIrisImage(irisImage)

    #parte de salvar

    return True


dataCod.cache2DLGFilter(45)