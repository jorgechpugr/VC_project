#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 07/02/2015

@author: jorge
'''
import intelligent_scissor.IntelligentScissor as inSciss



class Manejo():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def __start(self):
        ins = inSciss.IntelligentScissor(self.__imagen)
        return ins.liveWire(self.__puntosSemilla[0],self.__ROI)
        
    def addImagen(self, imagen):
        self.__imagen = imagen
        self.__ROI = None
        
    def intelligentScissor(self,cFrom,cTo=None):
        if cTo != None:            
            self.__ROI = (cFrom,cTo)
        self.__puntosSemilla = (cFrom,cTo)
        puntos =  self.__start()
        
        nextPunto = cTo
        camino = []
        while nextPunto != cFrom:
            camino.append(nextPunto)
            nextPunto = puntos[nextPunto]
        camino.append(nextPunto)    
        return camino
        