from plates import is_valid
def main():
    test_punctuation()
    test_isend_char()
    test_one_char()
    test_lenth_6()
    test_valid()
    test_midis_0()
    test_final()



def test_punctuation():
    assert is_valid("PI3.14") == False
def test_isend_char():
    assert is_valid("CS50P") == False
def test_one_char():
    assert is_valid("H") == False
def test_lenth_6():
    assert is_valid("OUTATIME") == False
def test_valid():
    assert is_valid("CS50") == True
def test_midis_0():
    assert is_valid("CS05") == False
def test_final():
    assert is_valid("50") == False










if __name__ == "__main__":
    main()