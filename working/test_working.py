from working import convert
import pytest

def main():
    test_right()



def test_right():
    assert convert("9:00 AM to 5:00 PM") =="09:00 to 17:00"
def test_wrong():
     with pytest.raises(ValueError):
         convert("cat")





if __name__ == "__mian__":
    main()
