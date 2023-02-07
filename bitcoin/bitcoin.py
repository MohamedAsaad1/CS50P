import requests
import sys
if len(sys.argv) != 2 :
    print("Missing command-line argument")
    sys.exit()
elif sys.argv[1].isalpha():
    print("Command-line argument is not a number")
    sys.exit()

try:

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    results = response.json()
    Rate_Bit = float(results["bpi"]["USD"]["rate"].replace(",",""))
    amount =  Rate_Bit * float(sys.argv[1])
    print(f"${amount:,.4f}")

except requests.RequestException:
    exit()