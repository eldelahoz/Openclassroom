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

# Répète 20 fois
"""i = 0
while i < 20:
    sys.stdout.write("1")
    sys.stdout.flush()
    attente = 0.2
    attente += random.randint(1, 60) / 100
    # attente est à présent entre 0.2 et 0.8
    time.sleep(attente)
    i += 1
    """
'''
Approche parallèle

Maintenant, nous allons créer deux threads qui vont s'exécuter ensemble : le premier affichera des 1 sur l'écran, tandis
que le second affichera des 2. Lancé en même temps, vous devriez voir plus clairement la façon dont ils s'exécutent.

'''
class Afficheur(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""
    
    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre
        
    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1
            
# Création de Thread
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
    
# Création de Deuxieme Thread
deuxiem_thread1 = Deuxieme_Afficheur("canard")
deuxiem_thread2 = Deuxieme_Afficheur("TORTUE")


# LANCEMENT DES DEUXIEME THREAD
deuxiem_thread1.start()
deuxiem_thread2.start()

# Attend que les threads se terminent
deuxiem_thread1.join()
deuxiem_thread2.join()

