from datetime import date
import sys
import inflect

class Seasons:
    def __init__(self,Y):
        self.Y = Y
    def __str__(self):
        x = inflect.engine().number_to_words(self.Y*1440,andword="")
        return f"{x.capitalize()} minutes"
    @classmethod
    def _date(cls):
         try:
             All = input("Date of Birth:").strip().split("-")
             final = str(abs(date(int(All[0]),int(All[1]),int(All[2]))-date.today())).split(" ")
             return cls(int(final[0]))
         except:
             sys.exit("Invalid date")

def main():
    x = Seasons._date()
    print(x)









if __name__ == "__main__":
    main()