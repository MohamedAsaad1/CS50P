def main():
    word = input("")
    space(word)


def space(text):
    for i in text:
        if i == " ":
            print("...",end="")
        else:
            print(i,end="")
    print("")


main()