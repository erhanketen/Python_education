import requests
import sys

api_key = "**************"

api_connection = "https://data.fixer.io/api/latest?access_key="+api_key

response = requests.get(api_connection)

json_data = response.json()


first_rate = input("Enter The First Rate: ")
second_rate = input("Enter The Second Rate: ")

try:
    rate1 = json_data["rates"][first_rate]
    rate2 = json_data["rates"][second_rate]
except KeyError:
    sys.stderr.write("Invalid Rate")
    sys.stderr.flush()
    sys.exit(1)

try:
    amount = int(input("Enter The Amount: "))
except ValueError:
    sys.stderr.write("The Amount must be an Integer")
    sys.stderr.flush()
    sys.exit(1)

print((rate1 / rate2) * amount )








