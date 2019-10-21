#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:08:14 2019

Python tricks: patterns for cleaner code (asserts, string interpolation, underscores
and dunders), looping and iteration (generators), classes and OOP (__repr__), 
dictionary tricks 

# python_tricks
Repo for making code snippets of cool python tricks, to try and improve programming skills. robots_py and funky_functions.py are based on notes from the Python tricks book by Dan Bader.

# robots.py
Incorporates OOP with tricks to write cleaner code (asserts, string interpolation, underscores and dunders), looping and iteration (generators), classes and OOP (__repr__), dictionary tricks 
"""
import numpy as np

class basic_bot(object):
    def __init__(self, name, age):
        assert len(name) < 10, 'Name toooo long for a basic bot' # assertion for unexpected error
        self.name = name 
        self.__type = 'basic' # dunder protects 'type' variable values between classes
        self.age = age
        self._ability = f'{self.name} of bot type {self.__type} can only move' # under, private variable convention
        self.location = np.zeros(2)
        
    def __repr__(self): 
        '''
        __repr__ function adds an unambiguous way of inpsecting a class
        '''
        return (f'{self.__class__.__name__}({self.name!r}, {self.age!r})') # string interpolation
        
    def move(self):
        self.location += np.array([np.random.random(), np.random.random()])
        return None
    
class librarian_bot(basic_bot):
    def __init__(self, name, age):
        super().__init__(name, age) # super function required for calling constructor, methods and properties of parent class
        self.__type = 'librarian'
        self._ability = f'{self.name} of bot type {self.__type} can move and make a library'
    
    @staticmethod      # shtatic method
    def create_library(no_of_books):
        '''
        Method to create a library of books of varying lengths
        '''
        library = {}
        for i in range(no_of_books):
            # An alternative to library.update({'book'+str(i):np.random.randint(1,1001)})
            library = dict(library, **{'book'+str(i):np.random.randint(1,1001)}) # dictionary unpacking using **
        return library
        
class sorting_bot(basic_bot):
    def __init__(self):
        super
 
        
        
    
