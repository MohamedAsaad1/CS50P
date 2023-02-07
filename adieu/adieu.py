import inflect

p = inflect.engine()
list_words = ["Adieu, adieu"]
words = ["Adieu, adieu, to Liesl and Friedrich"]
while True:
    try:
        name = input("Name:").strip()
        list_words.append(name)
    except EOFError:
        if name == "Liesl":
            print(",".join(list_words).replace("Liesl", " to Liesl "))
            break
        elif name == "Friedrich":
            print("".join(words))
            break
        else:
            print(p.join(list_words).replace(";", ",").replace("Liesl", "to Liesl"))
            break
All problems are overgit config --local github.user