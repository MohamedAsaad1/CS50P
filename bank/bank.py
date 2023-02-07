def main():
    greet = input("Greeting:")
    print(f"${value(greet)}")

def value(greet):
    greet = greet.lower().strip()
    if "hello" in greet :
        return 0
    elif greet[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()


