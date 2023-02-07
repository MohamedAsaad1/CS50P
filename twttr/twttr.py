def shorten(tweet):
    if tweet.isdigit():
        return ""
    lis = []
    for twe in tweet:
        if not twe.lower() in ["a","i","o","u","e"] :
            lis.append(twe)
    return "".join(lis)


def main():
    tweet = input("Input:").strip()
    print(shorten(tweet))



if __name__ == "__main__":
    main()





