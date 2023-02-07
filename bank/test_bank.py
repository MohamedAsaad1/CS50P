from bank import value

def main():
    test_1()
    test_2()
    test_3()



def test_1():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hello, Newman ") == 0
def test_2():
    assert value("Hey") == 20
    assert value("hey") == 20
    assert value("How you doing? ") == 20
    assert value("How's it going?") == 20

def test_3():
    assert value("What's happening?") == 100
    assert value("what's up?") == 100
    assert value("What's up?") == 100







if __name__ == "__main__":
    main()