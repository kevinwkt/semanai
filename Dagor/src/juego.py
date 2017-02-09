#!/usr/bin/env python
# coding: utf-8

from dagor import JuegoD10, JugadorD10Estrategico, \
    JugadorD10Interactivo, JugadorD10Aleatorio
from dagor import JuegoSuperGato, JugadorSuperGatoAleatorio, \
    JugadorSuperGatoInteractivo, JugadorSuperGatoEstrategico
from dagor import JuegoOrugas, JugadorOrugasAleatorio, JugadorOrugasInteractivo

def jd10():
    c = JuegoD10(
        JugadorD10Aleatorio('Izquierda'), 
        JugadorD10Estrategico('Derecha'))
    c.inicia(veces=100, delta_max=0)
    #c.inicia()

def jsg():
    c = JuegoSuperGato(
        JugadorSuperGatoAleatorio('Alfa'),
        JugadorSuperGatoEstrategico('Beta'),
        3, 4)
    print(c.inicia(veces=100, delta_max=0))
    
def jor():
    c = JuegoOrugas(
        JugadorOrugasAleatorio('C3PO'),
        JugadorOrugasInteractivo('R2D2'),
        5, 5)
    print(c.inicia(100, delta_max=1))
    
jsg()
