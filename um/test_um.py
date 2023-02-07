from um import count

def main():
    test_correct()
    test_wrong()


def test_correct():
    assert count("Um, thanks for the album") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1


def test_wrong():
    assert count("ymum") == 0
    assert count("fgum") == 0




if __name__ == "__main__":
    main()
