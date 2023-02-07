import sys

def main():
    #check is argv is 2 and all test of argv
    counter = 0
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif  len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if "txt" in sys.argv[1]  :
        print("Not a Python file")
        sys.exit(1)
# count the lines
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    pass
                elif line.lstrip():
                    counter +=1
            print(counter)
    except:
        raise FileNotFoundError("File does not exist")










main()