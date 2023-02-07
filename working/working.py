import re




def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if capture := re.search(r"(\d*):?(\d*) (PM|AM) to (\d*):?(\d*) (PM|AM)",s):
        if int(capture.group(1)) <= 12 and capture.group(2) != "60" and int(capture.group(4)) <= 12 and capture.group(5) != "60":
            final = first(capture.group(1), capture.group(2), capture.group(3))+" to "+first(capture.group(4), capture.group(5), capture.group(6))
            return final

    raise ValueError("Error")


def first(x, y, kind):
    if kind == "AM" and x == "12":
        x = "00"+":"
        if y == "":
            return x +"00"
        return x + y
    elif kind == "AM":
        if y == "":
            x = f"{int(x):02}:00"
            return x
        return f"{int(x):02}:{y}"
    elif kind == "PM" and x == "12":
        if y == "":
            return "12"+":"+ "00"
        x ="12"+":"+ y
        return x
    else:
        if y == "":
            return f"{int(x)+12}:00"
        x = f"{int(x)+12}:{y}"
        return x




if __name__ == "__main__":
    main()