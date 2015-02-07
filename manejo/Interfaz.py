#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 07/02/2015

@author: jorge
'''

import Tkinter as tk
import ImageTk
import tkFileDialog
import manejo.Manejo as man
import trabajos.p0 as p0

__IMAGEFOLDER__ = "./imagenes/"

class Interfaz:
    '''
    classdocs
    '''


    def __init__(self, interfaz,width=500, height=500):
        '''
        Constructor
        '''
        self.__interfaz = interfaz
        
        self.__COLOR = {"verde" : "#476042" ,"rojo" : "#FF3300","amarillo" : "#FFFF00"}
        self.__width, self.__height = width,height
        
        self.__frameCanvas = tk.Frame(interfaz)
        self.__generarBarraMenu(interfaz)        
        self.__generarCanvas(width,height) 
        self.__generarBarraAyuda(interfaz)
        
        self.__menu.grid(column=0,row=0)
        self.__frameCanvas.grid(column=0,row=1)
        self.__barraAyuda.grid(column=0,row=2)  
        
        self.__archivoAbierto = False  
        self.__coordenadaA, self.__coordenadaB = None, None
        
        self.__manejo = man.Manejo()
    
    """
    Genera el contenido de la barra de menu y asigna funciones a eventos de ratón
    """
    def __generarBarraMenu(self,parent):
        self.__menu = tk.Frame(master=parent)
        
        
        bOpenImagen = tk.Button(self.__menu,text="Abrir Imagen",command=self.__abrirFichero)    
        bIntelligentScissors = tk.Button(self.__menu,text="Tijeras inteligentes",command=self.__tijeras) 
        bSalir = tk.Button(self.__menu,text="Salir", command=self.__salir)
        
        bOpenImagen.grid(row=0,column=0) 
        bIntelligentScissors.grid(row=0,column=1)
        bSalir.grid(row=0,column=2)     
        
    """
    Genera el lienzo que cargará las imágenes
    
    """
    def __generarCanvas(self,width,height):
        self.__canvas = tk.Canvas(self.__frameCanvas, bg="black", width=width, height=height) 
        self.__canvas.grid(row = 0, column = 0)
        self.__canvas.bind("<Button-1>", self.__tijeras)
        
    """
    Genera el frame correspondiente a la barra inferior
    """
    def __generarBarraAyuda(self,parent):
        self.__barraAyuda = tk.Frame(parent)
        self.__textoAyuda = tk.StringVar()
        etiquetaAyuda = tk.Label(self.__barraAyuda,textvariable=self.__textoAyuda)
        etiquetaAyuda.grid(row=0,column=0)
        
    """
    Muestra un dialogo de apertura de ficheros
    """
    def __abrirFichero(self):
       
        options = {}
        options['filetypes'] = [('Imagenes jpg', '.jpg'),('Imagenes png', '.png'),('Imagenes bmp', '.bmp'),('Imagenes ppm', '.ppm')]
        archivo =  tkFileDialog.askopenfilename(**options)
        if (len(archivo) != 0):
            imagen = ImageTk.PhotoImage(file=archivo) 
            self.__width, self.__height = imagen.width(),imagen.height()
            self.__canvas.config(height=self.__height,width = self.__width)
            
            self.__photoimage = imagen
            self.__canvas.create_image(self.__width/2, self.__height/2, image=self.__photoimage) 
            
            self.__rutaArchivo = archivo
            self.__archivoAbierto = True
            self.__tijeras()
        
    def __tijeras(self,event = None):
        if not self.__archivoAbierto:
            self.__textoAyuda.set("Debe abrir primero una imagen")
            return
        if event == None:
            self.__textoAyuda.set("Seleccione puntos de la imagen")
            return
        
        if self.__coordenadaA == None:
            self.__coordenadaA = event.y,event.x
            self.__textoAyuda.set("Seleccione el siguiente punto de la imagen")
        else:           
            self.__coordenadaB = event.y,event.x
            self.__textoAyuda.set("Espere...")            
            imagen = p0.leeImagen(self.__rutaArchivo, 0)            
            self.__manejo.addImagen(imagen)            
            self.__manejo.intelligentScissor(self.__coordenadaA, self.__coordenadaB)
            self.__textoAyuda.set("Seleccione el siguiente punto de la imagen")
            self.__coordenadaA = self.__coordenadaB
        
        
    """
    Abandona la aplicación
    """
    def __salir(self):
        exit(0)
        raise SystemExit