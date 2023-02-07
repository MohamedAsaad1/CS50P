Months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        All = input("Date:").strip()
        M, D, Y = All.split("/")
        if M .isnumeric():
            if int(M) <= 12 and int(D) <=31:
                print(f"{Y}-{M.zfill(2)}-{D.zfill(2)}")
                break
    except:
        try:
            MM, DD, YY = All.split(" ")
            DDD = DD.replace(",","")
            if MM in Months and int(DDD) <=31:
                print(f"{YY}-{Months.index(MM)+1:02}-{DDD.zfill(2)}")
                break
        except:
            pass









