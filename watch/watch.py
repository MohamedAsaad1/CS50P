import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):

    if  shorter := re.search(r"src=\"https*://[www]*\.*youtube.com/embed/(\w*\n*\w*)\"",s):
        return "https://youtu.be/"+shorter.group(1).strip()

if __name__ == "__main__":
    main()