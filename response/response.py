from validator_collection import checkers
def main():
    if checkers.is_email(input("What's your email address?").strip()):
        print("Valid")
        exit(0)

    print("Invalid")
main()