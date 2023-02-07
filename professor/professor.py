import random
def main():
    level = get_level()
    count = 0
    i = 0
    score = 0
    while True:
        if count == 10:
            break
        try:
            if  level == 1:
                z = random.randint(0,9)
            elif level == 2:
                z = random.randint(10,99)
            else:
                z = random.randint(100,999)

            x = generate_integer(level)
            print(f"{x} + {z} = ",end="")
            answer = int(input(""))
            if x + z == answer:
                count += 1
                score += 1

            else:
                i=0
                while True:
                    print("EEE")
                    print(f"{x} + {z} = ",end="")
                    answer = int(input(""))
                    if x + z == answer:
                        count += 1
                        score += 1
                        break
                    i += 1
                    if i == 2:
                        count += 1
                        score -= 1
                        print("EEE")
                        print(f"{x} + {z} = {x + z}")
                        break
        except ValueError:
            i= 0
            while True:
                print("EEE")
                print(f"{x} + {z} = ",end="")
                S = input("")
                s = str(x+z)
                i += 1
                if S == s:
                    score += 1
                    count += 1
                    break
                elif i == 2:
                    print("EEE")
                    print(f"{x} + {z} = {x + z}")
                    score -= 1
                    break
    print(f"Score:{score}")
    exit()

def get_level():
    while True :
        try:
            guess = int(input("Level:"))
            if guess >= 1 and guess <=3:
                return guess
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        return x
    elif level == 2:

        x = random.randint(10,99)
        return x
    else:
        x = random.randint(100,1000)
        return x

if __name__ == "__main__":
    main()


