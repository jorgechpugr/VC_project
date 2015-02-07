# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 14:10:35 2014

@author: Jorge Chamorro Padial

75569660-D
jorgechp@correo.ugr.es

PRACTICA-0
"""

import cv2
import numpy as np


# EJERCICIO 1
#
# Escribir una función que lea una imagen en niveles de gris o en
# color ( im=leeimagen(filename, flagColor))
#
def leeImagen(filename, flagColor):
    return cv2.imread(filename,flagColor)


# EJERCICIO 2
#
# Escribir una función que visualice una imagen (pintaI(im))
# 
#
def pintaI(im,text='EJERCICIO_2'):
    cv2.imshow(text,im)


# EJERCICIO 3
#
# Escribir una función que visualice varias imágenes a la vez:
# pintaMI(vim). (vim será una secuencia de imágenes) ¿Qué pasa
# si las imágenes no son todas del mismo tipo: (nivel de gris, color,
# blanco-negro)?
#
# RESPUESTA
# Las imagenes de diferente tipo tienen estructuras diferentes en memoria, por lo tanto, necesitarían
# algoritmos diferentes para ser tratadas. Es necesario que todas la imagenes sean del mismo tipo
# para facilitar el desarrollo y aplicación de filtros
# 
# En la función pintaMI se han definido dos formas de realizar el ejercicio: mediante el uso de regiones de interés
# o bien, tratando las matrices manualmente realizando una concatenación de imágenes sobre una misma matriz
#
def pintaMI(vim):
    
    numImages = len(vim)
    puntero = 0
    sumatorioFilas = 0
    maxColumnas = 0  
    modo = -2
    #Unificar imagenes
    for imagen in range(numImages):
        #Extracción de canales de la imagen
        canales = len(vim[imagen].shape)
        
        #Todas las imagenes deben convertirse al mismo tipo para trabajar con ellas, es posible:
        # a) Convertir todas a RGB
        # b) Convertir todas a escala de grises
        # c) Convertir todas a RGB con canal alpha
        # 
        # Para esta práctica, todas se han convertido a escala de grises, aunque realizar conversiones
        # a otro tipo de imagen es trivial, utilizando la función cv2.cvtColor(imagen, modo_conversion
        #)
        
        if modo == -2:
            modo = canales
            
        if modo != canales:
            if modo == 2:                
                vim[imagen] = cv2.split(vim[imagen])[1] #Esta es una forma de obtener un solo canal, el verde                
                #vim[imagen] = cv2.cvtColor(vim[imagen],cv2.COLOR_RGB2GRAY) #Esta es otra manera
               
            else:
                vim[imagen] = cv2.cvtColor(vim[imagen],cv2.COLOR_GRAY2RGB)
            

    
    #Busca la imagen con mayor ancho/columnas.
    for imagen in range(numImages):
        columnas = len(vim[imagen][0])
        
        if columnas > maxColumnas:
            maxColumnas = columnas
            imagenResultante = vim[imagen]
            puntero = imagen
            
        sumatorioFilas += len(vim[imagen])
    
    #Se crea una matriz y se concatenan las diferentes imagenes
    #Otra forma de hacer podría ser estableciendo ROIs
    for imagen in range(numImages):
        if imagen != puntero:
            imagenActual = vim[imagen]
            
            if len(imagenActual[0]) == maxColumnas:            
                imagenAjustada = np.concatenate((imagenResultante,imagenActual))
            else:        
                filas = len(imagenActual)
                imagenF = cv2.resize(imagenActual,(maxColumnas,filas))                
                imagenAjustada = np.concatenate((imagenResultante,imagenF))
                
            imagenResultante = imagenAjustada
            
    # http://www.netaro.info/techinfo/OpenCV/opencv094-man/ref/OpenCVRef_BasicFuncs.htm#decl_cvSetImageROI          
    # En la dirección anterior explican el funcionamiento de todas las funciones para trabajar con ROIs en Opencv
    if modo == 2:
        imagenResultanteROIs = cv2.cv.CreateMat(sumatorioFilas,maxColumnas, cv2.CV_8UC1)        
    else:
        imagenResultanteROIs = cv2.cv.CreateMat(sumatorioFilas,maxColumnas, cv2.CV_8UC3)     
    
    contadorFilas = 0
    
    for imagen in range(numImages):
        numColumnas = len(vim[imagen][0])
        numFilas =    len(vim[imagen])

        
        roi = imagenResultanteROIs[contadorFilas:numFilas+contadorFilas,0:numColumnas]

        
        contadorFilas += numFilas
        
        # La documentación de opencv dice:
        # Use fromarray() to convert numpy arrays to CvMat or cvMatND
        #
        
        im = cv2.cv.fromarray(vim[imagen])

        
        cv2.cv.Copy(im,roi)
        
        
        

    cv2.imshow('EJERCICIO_3_A',np.asarray(imagenResultanteROIs))
    cv2.imshow('EJERCICIO_3_B',imagenResultante)
    
    
        
# EJERCICIO 4
# Escribir una función que modifique el valor en una imagen de una
# lista de coordenadas de píxeles.
#
# Si no se especifica como argumento una lista de coordenadas de píxeles
# se aplica la transformación a todos los pixeles de la imagen
# La transformación consiste en invertir el color de la imagen
        
def transformImage(img,coord = -1):
    if coord != -1:
        numCoords = len(coord)    
        
        for i in range(numCoords):        
            x = coord[i][0]
            y = coord[i][1]
            img[x][y] = 255 - img[x][y]
    else:
        numFilas = len(img)
        numColumnas = len(img[0])
        
        for i in range(numFilas):
            for j in range(numColumnas):
                img[i][j] = 255 - img[i][j]
            

def cerrar():
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#EJECUCIÓN
if __name__ == '__main__':

    listaImagenes = []
    
    coordenadas = [ 
        [0, 1], [40, 2], [0, 3], [0, 4], 
        [0, 2], [40, 3], [1, 3], [1, 5], 
        [0, 3], [40, 4], [2, 3], [2, 6], 
        [0, 4], [40, 5], [3, 3], [3, 7], 
        [0, 5], [40, 6], [4, 3], [4, 8], 
        [0, 6], [40, 7], [5, 3], [5, 9]     
    
    ]
    
    
    
    #Diferentes tipos
    imagen1 = leeImagen('imagenes/dog.jpeg',cv2.IMREAD_COLOR)
    imagen2 = leeImagen('imagenes/tiger.jpg',cv2.IMREAD_COLOR) 
    imagen3 = leeImagen('imagenes/hamster.jpg',cv2.IMREAD_GRAYSCALE)
    imagen4 = leeImagen('imagenes/lynx.jpeg',cv2.IMREAD_UNCHANGED)
    
    listaImagenes.append(imagen1)
    listaImagenes.append(imagen2)
    listaImagenes.append(imagen3)
    listaImagenes.append(imagen4)
    
    pintaI(imagen1)
    pintaMI(listaImagenes)
    
    transformImage(imagen1,coordenadas)
    transformImage(imagen2)
    
    cv2.imshow('EJERCICIO_4_A',imagen1)
    cv2.imshow('EJERCICIO_4_B',imagen2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()