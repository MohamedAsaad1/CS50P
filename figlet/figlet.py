import sys
from pyfiglet import figlet_format

try:
        fon = sys.argv[2].strip()
        figlet_format("CS",font = fon)
except:
        exit("Invalid usage")

if  len(sys.argv) == 2 or sys.argv[1]  not in ["-f","--font"]  :
    sys.exit("Invalid usage")
    
InP = input("Input:")
if len(sys.argv) >= 2:
    print(figlet_format(InP,font= sys.argv[2].strip()))
    sys.exit()

print(figlet_format(InP))

