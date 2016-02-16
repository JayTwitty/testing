
from currency_converter import usd_to_euro
from currency_converter import euro_to_usd
from currency_converter import usd_to_many

assert usd_to_euro(1) == "0.9 EUR"
assert usd_to_euro(8) == "7.2 EUR"
assert usd_to_euro("a") == print("You must enter a USD value to convert...")

assert euro_to_usd(1) == "1.11 USD"
assert euro_to_usd(8) == "8.88 USD"
assert euro_to_usd("a") == print("You must enter a EURO value to convert...")


assert usd_to_many([5]) == ["5 USD converts to", '4 EUR', "3 GBP", '342 INR']
assert usd_to_many([5, 10]) == ["5 USD converts to", '4 EUR', "3 GBP", '342 INR', "10 USD converts to", '9 EUR', "7 GBP", '684 INR']
assert usd_to_many([5, "a"]) ==  ["5 USD converts to", '4 EUR', "3 GBP", '342 INR'], print("You must enter a USD value to convert...")