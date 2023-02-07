def main():
    word = input("")
    convert(word)


def convert(text):
    for i in text:
        if i == ":":
            i = i[:-1:]

        if i == ")" :
            print("🙂",end="")
        elif i == "(":
            print("🙁",end="")

        else:
            print(i,end="")
    print("")


main()