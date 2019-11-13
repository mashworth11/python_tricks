#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program is a way of corroborating, and a reference for, some of the things
I learnt from the Python Tricks book. Things included are listed below. The program
itself is based on a robot and it's derivatives, that can do (pretty random)
menial tasks.  

Python tricks: patterns for cleaner code (asserts, string interpolation, underscores
and dunders), looping and iteration (generators), classes and OOP (inheritance and 
__repr__), dictionary tricks

# python_tricks
Repo for making code snippets of cool python tricks, to try and improve programming skills. robots_py and funky_functions.py are based on notes from the Python tricks book by Dan Bader.

# robots.py
Incorporates OOP with tricks to write cleaner code (asserts, string interpolation, underscores and dunders), looping and iteration (generators), classes and OOP (__repr__), dictionary tricks 
"""
import numpy as np
import collections

## asserts, dunders, string interpolation, __repr__ ##
class basic_bot(object):
    def __init__(self, name, age):
        assert len(name) < 10, 'Name toooo long for a basic bot' # assertion for unexpected error
        self.name = name 
        self.__type = 'basic' # dunder protects 'type' variable values between classes
        self.age = age
        self.ability = f'{self.name} of bot type {self.__type} can only move' 
        self.location = np.zeros(2)
        
    def __repr__(self): 
        """
        __repr__ method adds an unambiguous way of inpsecting a class
        """
        return (f'{self.__class__.__name__}({self.name!r}, {self.age!r})') # string interpolation
        
    def move(self):
        """
        Method to move to a robot
        """
        self.location += np.array([np.random.random(), np.random.random()])
        return None

## inheritance with super(), static method, and dictionary unpacking ##
class librarian_bot(basic_bot):
    def __init__(self, name, age):
        super().__init__(name, age) # super function required for calling constructor, methods and properties of parent class
        self.__type = 'librarian'
        self.ability = f'{self.name} of bot type {self.__type} can move' + \
                          ' and make a library of books of varying lengths'
    
    @staticmethod      # shhhtatic method
    def create_library(no_of_books):
        """
        Method to create a library of books of varying lengths
        """
        library = {}
        for i in range(no_of_books):
            # An alternative to library.update({'book'+str(i):np.random.randint(1,1001)})
            library = dict(library, **{'book'+str(i):np.random.randint(1,1001)}) # dictionary unpacking using **
        return library

## default dictionary values i.e. .get(), ask for user input(), assert, ##
## and dictionary udpate ##
class book_worm_bot(basic_bot):
    def __init__(self, name, age, library_dict):
        super().__init__(name, age)
        self.__type = 'book worm'
        self.ability = f'{self.name} of bot type {self.__type} can move' + \
                        ' and choose a book from a library'
        self.library_dict = library_dict
                        
    def choose_a_book(self, book_name):
        """
        Method to choose a book from the library, return a default value if
        it's not there, and ask for user input on whether you'd like to add it
        to the library.
        """
        if self.library_dict.get(book_name, None) == None:
            answer = input('Would you like to add this book to the library? ')
            if (answer == 'Yes') or (answer == 'Y') or (answer == 'y'):
                how_long = int(input('How long is the book? '))
                assert how_long < 1000, 'Sorry, this library only accepts books under 1000 pgs.'
                self.library_dict.update({book_name: how_long})
                return self.library_dict
            else:
                print('Ok, no problemo, have a nice day!')
        else:
            print(f'Here is {book_name} that you requested, it is'
                  f' {self.library_dict[book_name]} pages long.') # f needs to be on each line
        
## dictionary sorting by book length, return a sorted dict ##
class sorting_bot(basic_bot):
    def __init__(self, name, age, library_dict):
        super().__init__(name, age)
        self.__type = 'sorting'
        self.ability = f'{self.name} of bot type {self.__type} can move' + \
                        ' and choose a book from a library'
        self.library_dict = library_dict       
        
    def sort_by_booklength(self):
        """
        Method to sort the library by book length
        """
        sorted_lib = sorted(self.library_dict.items(), key = lambda x: x[1])
        return collections.OrderedDict(sorted_lib)
 
## private property naming convention, and __str__ method ##
class speaking_bot(basic_bot):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__type = 'speaking'
        self.ability = f'{self.name} of bot type {self.__type} can move' + \
                        ' and can repeat user input'
        self._sentence = input(f'Hi, my name is {self.name}, and I just looove'
                                 ' to speak. Please give me something to say: ')
                
    def __str__(self):
        """
        __str__ method adds some kind of textual information
        """
        return self._sentence
        
## generators and generator expressions, iterator chain ##
class generator_bot(basic_bot):
    def __init__(self, name, age, sentence):
        super().__init__(name, age)
        self.__type = 'generator'
        self.ability = f'{self.name} of bot type {self.__type} can move' + \
                        ' and can repeat user input'
        self.gen_obj = (sentence for i in range(5)) # generator expression
    
    # create a series of static generator methods that can be used as part of 
    # an iterator chain
    @staticmethod # this needs to come first
    def integers():
        """
        Method to create an integer generator
        """
        for i in range(1,9):
            yield i
    
    @staticmethod     
    def squared(seq):
        """
        Method to create an integer generator
        """
        for i in seq:
            yield i*i
    
    @staticmethod
    def halved(seq):
        """
        Method to create an integer generator
        """
        for i in seq:
            yield i/2
    
    @staticmethod        
    def add_10(seq):
        """
        Method to create an integer generator
        """
        for i in seq:
            yield i + 10
        
        
    # e.g. chain = halved(add_10(squared(integers())))
        
        
        
        
        
        
        
        
        
        
        
        





    
    
