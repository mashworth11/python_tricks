#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:08:14 2019

Python tricks: patterns for cleaner python (asserts, string interpolation, underscores
and dunders), looping and iteration (generators), classes and OOP (__repr__), 
dictionary tricks 
"""
import numpy as np

class basic_bot(object):
    def __init__(self, name, age):
        assert len(name) < 10, 'Name toooo long for a basic bot'
        self.name = name 
        self.__type = 'basic'
        self.age = age
        self._ability = f'{self.name} of bot type {self.__type} can only move'
        self.location = np.zeros(2)
        
    def __repr__(self):
        '''
        __repr__ function adds an unambiguous way of inpsecting a class
        '''
        return (f'{self.__class__.__name__}({self.name!r}, {self.age!r})')
        
    def move(self):
        self.location += np.array([np.random.random(), np.random.random()])
        return None
    
    
 
        
        
    
