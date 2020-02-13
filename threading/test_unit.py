#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Created on 27 janv. 2020

@author: oeil
'''
import random
import unittest
# De petit examples de module random
"""
liste = ["chat", "chien", "renard", "serpent", "cheval", "parapluie"]
print(random.choice(liste))
random.shuffle(liste)
print(liste)
liste2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(random.sample(liste2, 5))

print(random.sample(range(1000), 10))
"""
# Structure de base d'un test unitaire
class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""
    
    def setUp(self):
        """Initilisation des tests"""
        self.liste = list(range(10))
    
    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, self.liste)
    
    
    # Test de la fonction random.shuffle

    # Autres méthodes de test
    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)        
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)), msg="Mon dieux")

    # Test de la fonction random.sample
    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)
        
        # self.assertRaises(ValueError, random.sample, liste, 20)
        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)
