camel = input("camelCase:")
if camel.islower():
    print(camel)

for c in camel:
    if c.islower():
        print(c,end="")
    else:
        print("_"+ c.lower(),end="")
print()

# elif c.isupper(): print("_"+c.lower(),end="")
#print("_"+ c.lower(),end="")