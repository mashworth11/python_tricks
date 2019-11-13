#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program is a way of corroborating, and a reference for, some of the things
I learnt from the Python Tricks book about functional programming. Things included
are listed below.

Effective functions: First class functions, decorators, *args and **kwargs, 
function argument unpacking. 
"""
import pprint

## Python's functions are first-class citizens! This means that they can be... ##
def yell(string):
    return string.upper()

# passed to variable
bark = yell

# stored in data structures
funcs = [bark, str.lower, str.capitalize]

# passed to other processes (functions)
def greet(yell):
    greeting = yell('Hello, I like Pythons with cheese on top')
    print(greeting)
    
# nested from other functions
# here we purposely don't referenced text so as show lexical closures in the 
# next example. 
def say_something_weird(text):
    def yell_it(t): 
        return t.upper()
    return yell_it(text)

# returned from other functions whilst capturing the parents local state
def get_speak_func(text, vol):
    def whisper_it():
        return text.upper() + 'sss-sss-sss'
    def yell_it():
        return text.lower() + '!!!!!'
    if vol < 0.5:
        return whisper_it
    else:
        return yell_it


## *args and **kwargs ##
def mmm_pie(text, *args, **kwargs):
    """
    e.g. mmm_pie('stuff for a pie recipe', 'oven', 'spoon', 'microphone', eggs=20, apples=1000)
    """
    print(text.capitalize())
    if args:
        print('\nHere are the items you will need:')
        print(*args, sep = ', ')
    if kwargs:
        print('\nHere are the ingredients you will need:')
        pprint.pprint(kwargs)
    
## decorators ##
def uppercase(func): # define decorator
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase # 'wrap' your function, and what get's returned is the wrapper function
def greet():
    return 'Bellllo!'

# greet()    
    
    
    
    
    
    
    
    
    
    
    
    