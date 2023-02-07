cosat  = 50
while cosat > 0:
    print("Amount Due:",cosat)
    owen = int(input("Insert Coin:"))
    if owen  in [25,10,5]:
        cosat -= owen

print("Change Owed:",abs(cosat))







