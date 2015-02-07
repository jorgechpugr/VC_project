#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
Created on 25/01/2015

PROYECTO FINAL DE VISIÓN POR COMPUTADOR

@author: Jorge Chamorro Padial
'''
import os
import intelligent_scissor.IntelligentScissor as inSciss


import trabajos.p0 as p0


if __name__ == '__main__':
    imagesFolder = "./imagenes/"
    
    vaca =  p0.leeImagen(imagesFolder+"cow.jpg", 0)


    ins = inSciss.IntelligentScissor(vaca)
    a = ins.liveWire((134,30))
    
    print "adssad"