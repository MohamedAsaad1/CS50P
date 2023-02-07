import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


"""def is_valid(s):
    s = s.strip()
    for le in s:
        if le in string.punctuation :
            return False
    center = round (len(s) / 2)
    if len(s) < 2 or len(s) > 6 or s[0:2].isnumeric():
        return False
    elif s.isalpha():
        return True
    elif s[center] == "0":
        return False
    elif s[len(s) - 1].isnumeric():
        return True
if __name__ == "__main__":
    main()
#anthor solution
"""
def is_valid(s):
    for c in s:
        if c in ["!",".","?",' ']:
            return False
    middle = s[len(s)//2]
    if s[:2].isnumeric() or middle == '0':
        return False
    elif len(s)-1 > 6 or len(s)-1 < 2:
        return False
    elif middle.isnumeric() and s[-1].isalpha():
        return False
    else:
        return True




if __name__ == "__main__":
    main()















