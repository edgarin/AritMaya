#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys, random
import pygame
pygame.init()
import gui
from gui import *
import defaultStyle
from MayCLabel import MayCLabel


class AritMaya():
    
    def __init__(self):
        self.run = True
        self.screen = pygame.display.set_mode((640,480),0,32)
        defaultStyle.init(gui)
        self.desktop = gui.Desktop()
        self.GUI()
        self.AritMayaCiclo()
    
    def GUI(self):
        self.screen.fill((0,0,0))
        self.buttonsalir = Button(position=(480,450),parent=self.desktop,text="Salir")
        self.buttonsalir.onClick = self.buttonsalir_onClick
        self.txtResultado = TextBox(position=(200,360),size=(200,0),text="",parent=self.desktop)
        self.pregunta, self.respuesta = self.obtener_datos()
        self.lblPregunta = MayCLabel(self.screen,str(self.pregunta),"lblIngresadas",(145,50),"blanco")
        self.lblPregunta.Insertar()
        self.lblMensajeResultado = MayCLabel(self.screen,str(self.respuesta),"lblResultado",(300,250),"blanco")
        self.lblMensajeResultado.Insertar()
        self.btn = Button(position = (240,400),parent =self.desktop, text = "Ok")
        self.btn.onClick = self.evento_click        
                
    def obtener_datos(self):
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        pregunta = ""
        respuesta = 0
        randomoperacion = random.randint(0,3)
        if randomoperacion == 0:
            pregunta = "¿Cuánto es %s + %s?" % (num1,num2)
            respuesta = num1+num2 
        if randomoperacion == 1:
            pregunta = "¿Cuánto es %s - %s?" % (num1,num2)
            respuesta = num1-num2
        if randomoperacion == 2:
            pregunta = "¿Cuánto es %s x %s?" % (num1,num2)
            respuesta = num1*num2
        if randomoperacion == 3:
            pregunta = "¿Cuánto es %s / %s?" % (num1,num2)
            respuesta = num1/num2
        return pregunta, respuesta

    def Reiniciar(self):    
        self.screen.fill((0,0,0))
        self.txtResultado.Text=""
        self.pregunta, self.respuesta = self.obtener_datos()
        self.lblPregunta.Text((str(self.pregunta)))
        self.lblMensajeResultado.Text(str((self.respuesta)))
        
    def comprobar(self,respuesta):
        if respuesta == str(self.respuesta):
            self.Reiniciar()
            self.lblMensajeResultado.Text("Correcto")
        else:
            self.lblMensajeResultado.Text("Fallaste")
    
    def evento_click(self,widget):
        Ingresado = self.txtResultado.text
        self.comprobar(Ingresado)
    
    def buttonsalir_onClick(self, widget):
        sys.exit()
    
    def AritMayaCiclo(self):
        while self.run:
            for e in gui.setEvents(pygame.event.get()):
                if e.type == pygame.QUIT:
                    self.run = False
                if self.txtResultado.enter == True:
                    self.evento_click(self.txtResultado)
                    self.txtResultado.enter = False
            self.desktop.update()
            self.desktop.draw()
            pygame.display.update()
        
AritMaya()
        
#while run:
#    for e in gui.setEvents(pygame.event.get()):
#        if e.type == pygame.QUIT:
#            run = False      
#    desktop.update()
#    desktop.draw()
#    pygame.display.update()