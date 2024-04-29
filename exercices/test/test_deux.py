from exercices.src.fonction_simple import *
import pytest

def test_un():
    assert add(1,2) == 3

def test_deux():
    assert divide(30,3) == 10

from random import uniform


# Test introduction:

def add(a,b):
    return a+b


def divide(a,b):
    return a/b

def add_integer(a,b):
    if isinstance(a,int) and isinstance(b,int):    
        return a+b
    else:
        raise(TypeError("Parameters should be integers"))

def alea_uniform(a,b):
    return uniform(a,b)