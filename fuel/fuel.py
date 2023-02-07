def main():
     x = input("Fraction:")
     result= convert(x)
     print(result)
     final = gauge(result)
     print(final)




def convert(fraction):
    while True:

        x,y= fraction.split("/")
        g  = int(x)
        v = int(y)
        result = g/v

        if result <= 1:
            return int(result * 100)
        try:
            raise ValueError("Exception 123 raised")
        except:
            raise ZeroDivisionError("Only integers are allowed")





def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()

    """""def main():
     x = input("Fraction:")
     result= convert(x)
     final = gauge(result)
     print(final)




def convert(fraction):
    while True:
        try:
            x,y= fraction.split("/")
            g  = int(x)
            v = int(y)
            result = g/v
            if result <= 1:
                return int(result * 100)
            fraction = input("Fraction:")
        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction:")



def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()"""