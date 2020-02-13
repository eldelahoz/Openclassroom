#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Created on 29 janv. 2020

@author: oeil
'''
import time
import random
import sys
from threading import Thread
from multiprocessing import RLock

''' Example
print("Avant le sleep...")
time.sleep(3)
print("Apres le sleep...")
'''

# R�p�te 20 fois
"""i = 0
while i < 20:
    sys.stdout.write("1")
    sys.stdout.flush()
    attente = 0.2
    attente += random.randint(1, 60) / 100
    # attente est � pr�sent entre 0.2 et 0.8
    time.sleep(attente)
    i += 1
    """
'''
Approche parall�le

Maintenant, nous allons cr�er deux threads qui vont s'ex�cuter ensemble : le premier affichera des 1 sur l'�cran, tandis
que le second affichera des 2. Lanc� en m�me temps, vous devriez voir plus clairement la fa�on dont ils s'ex�cutent.

'''
class Afficheur(Thread):
    """Thread charg� simplement d'afficher une lettre dans la console."""
    
    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre
        
    def run(self):
        """Code � ex�cuter pendant l'ex�cution du thread."""
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1
            
# Cr�ation de Thread
thread_1 = Afficheur("1")
thread_2 = Afficheur("2")
# Lancement des threads
thread_1.start()
thread_2.start()
# Attend que les threads se terminent
thread_1.join()
thread_2.join()

verrou = RLock()


class Deuxieme_Afficheur(Thread):
    
    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot
    
    def run(self):
        i = 0
        while i < 5:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1
    
# Cr�ation de Deuxieme Thread
deuxiem_thread1 = Deuxieme_Afficheur("canard")
deuxiem_thread2 = Deuxieme_Afficheur("TORTUE")


# LANCEMENT DES DEUXIEME THREAD
deuxiem_thread1.start()
deuxiem_thread2.start()

# Attend que les threads se terminent
deuxiem_thread1.join()
deuxiem_thread2.join()

