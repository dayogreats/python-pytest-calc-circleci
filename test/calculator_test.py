import pytest
import cal.calculator

def test_somethingfunny():
    #setup
    #execercise
    #Assert/Validate
    assert True == True

def test_add():
    assert cal.calculator.add(2, 2) == 4

def test_subtract():
    assert cal.calculator.subtract(2, 2) == 0

def test_multiply():
    assert cal.calculator.multiply(2, 2) == 4