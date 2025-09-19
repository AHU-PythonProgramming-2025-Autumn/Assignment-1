import pytest
from src.hello import say_hello

def test_say_hello_alice():
    assert say_hello("Alice") == "Hello, Alice!"

def test_say_hello_bob():
    assert say_hello("Bob") == "Hello, Bob!"