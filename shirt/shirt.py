import sys
from  PIL import ImageOps
import os
from PIL import Image

def main():
#check the all the argv invalid input
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif "." not in sys.argv[1] and sys.argv[2]:
        sys.exit("Invalid input")

#get extension from argv 1 and 2

    _ , extension1 = os.path.splitext(sys.argv[1])
    _ , extension2 = os.path.splitext(sys.argv[2])
    if  extension1 != extension2:
        sys.exit("Input and output have different extensions")

# Open Front Image
    shirt = Image.open('shirt.png')
    size = shirt.size
# Open Background Image
    background = Image.open(sys.argv[1])
    background = ImageOps.fit(background, size)
    background.paste(shirt,shirt)
    background.save(sys.argv[2])

main()