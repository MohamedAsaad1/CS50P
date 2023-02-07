from fuel import convert, gauge
import pytest
def main():
    test_string()
    test_Division()
    test_correct()



def test_string():
     with pytest.raises(ValueError):
        convert("cat/dog")
        convert("one/two")
def test_Division():
     with pytest.raises(ZeroDivisionError):
         convert("1/0")
         convert("4/1")

def test_correct():
     assert convert("1/4") == 25
     assert convert("3/4") == 75
     assert convert("4/4") == 100
     assert convert("0/1") == 0

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"














if __name__ == "__main__":
    main()