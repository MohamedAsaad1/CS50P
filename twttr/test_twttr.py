from twttr import shorten
def main():
    test_vowel()
    test_capitalized()
    test_lower()
    test_Numbers()
    test_punctuation()



def test_vowel():
    assert shorten("Twitter") == "Twttr"
def test_capitalized():
    assert shorten("AIOUE") == ""
def test_lower():
    assert shorten("aioue") == ""
def test_Numbers():
    assert shorten("CS50") == "CS50"
def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"








if __name__ == "__main__":
    main()