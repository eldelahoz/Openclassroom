#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Created on 12 févr. 2020

@author: oeil
'''
from threading import Thread as Th
import time


def process_one():
    i = 0
    while i < 3:
        print("ooooooooooo")
        time.sleep(0.2)
        i += 1
        
def process_deux():
    i = 0
    while i < 3:
        print("xxxxxxxxxxx")
        time.sleep(0.3)
        i += 1
        
        
th1 = Th(target=process_one)
th2 = Th(target=process_deux)

th1.start()
th2.start()

th1.join()
th2.join()

print("Fin de Programe")