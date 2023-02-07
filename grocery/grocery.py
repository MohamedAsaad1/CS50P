dict = {}
while True:
    try:
        item = input().upper()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    except EOFError:
        for i in sorted(dict.keys()):
            print(dict[i],i)
        break
