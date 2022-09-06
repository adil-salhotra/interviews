import pytest 
import fib

def test_fibonacci():
    assert fib.fibonacci(9) == 34

def test_fibonacci_memo():
    assert fib.fibonacci_memo(9) == 34

def test_fibonacci_tab():
    assert fib.fibonacci_tab(9) == 34