def main():
    Ti = input("what time is it ?")
    convert(Ti)


def convert(time):
    hours, minutes = time.split(":")
    hour = float(hours)
    min = float(minutes)
    if hour >= 7 and hour <= 8:
        print("breakfast time ")
    elif hour >= 12 and hour <= 13:
        print("lunch time")
    elif hour >= 18 and hour <= 19:
        print("dinner time")
    else:
        print("No Meal")





if __name__ == "__main__":
    main()