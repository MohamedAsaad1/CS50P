import sys
import csv
# mian function
def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    x, y , z = reader()
    writer(x,y,z)

def reader():
    lis1 = []
    lis2 = []
    lis3 = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for line in reader:
                name1,name2= line["name"].split(",")
                lis1.append(name1)
                lis2.append(name2)
                lis3.append(line["house"])
        return lis1 ,lis2 ,lis3
    except:
        raise FileNotFoundError("Could not read 1.csv")

def writer(lis1,lis2,lis3):
    try:
        with open(sys.argv[2] ,"w") as f:
            writer = csv.DictWriter(f, fieldnames=["first","last","house"])
            writer.writeheader()
            for line in range(len(lis1)):
                writer.writerow({"first":lis2[line].strip(),"last":lis1[line].strip(),"house":lis3[line].rstrip()})
    except:
        raise FileNotFoundError("Could not read 1.csv")

if __name__ == "__main__":
    main()