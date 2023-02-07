import re



def main():
    print(count(input("Text: ").strip()))


def count(s):
    find = re.findall(r"um\W",s,re.IGNORECASE)
    if s == "um":
        return 1
    return len(find)


if __name__ == "__main__":
    main()