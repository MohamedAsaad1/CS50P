from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(0)
        jar = Jar(1.5)
    jar = Jar(4)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        jar = Jar(4)
        jar.deposit(1)
        jar.deposit(4)
    ja = Jar(4)
    ja.deposit(2)
    ja.deposit(1)
    ja.deposit(1)

def test_withdraw():
    with pytest.raises(ValueError):
        jar = Jar(4)
        jar.withdraw(1)
    with pytest.raises(ValueError):
        ja = Jar(4)
        ja.deposit(1)
        ja.deposit(2)
        jar.withdraw(4)
    j = Jar(4)
    j.deposit(1)
    j.deposit(2)
    j.withdraw(2)




