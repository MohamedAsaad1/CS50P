import re



def main():
    print(validate(input("IPv4 Address: ").strip()))



def validate(ip):
    if valid := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        if int(valid.group(1)) <= 255 and int(valid.group(2)) <= 255  and int(valid.group(3))<= 255  and int(valid.group(4))<= 255:
           return True
    return False




if __name__ == "__main__":
    main()