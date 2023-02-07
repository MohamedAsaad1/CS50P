dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
new = 0
while True:
    try:
        item = input("Item:").title().strip()
        if item in dict:
            new = new + float(dict[item])
            print(f"Total: ${new}",end ="0")
            print("")

    except EOFError:
        print("")
        break


