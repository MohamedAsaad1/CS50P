import sys
import csv
from tabulate import tabulate
lis = []
be = ['Regular Pizza','Small','Large']
def main():
    #check is argv is 2 and all test of argv
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif  len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if "csv" not in sys.argv[1]  :
        print("Not a CSV file")
        sys.exit(1)
# count the lines
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for line in reader:
                lis.append(line)
            print(tabulate(lis , headers='keys',tablefmt="grid"))

    except:
        raise FileNotFoundError("File does not exist")


main()