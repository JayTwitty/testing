
from currency_converter import usd_to_euro
from currency_converter import euro_to_usd

assert usd_to_euro(1) == "0.9 EUR"
assert euro_to_usd(1) == "1.11 USD"
assert usd_to_euro(8) == "7.2 EUR"
assert euro_to_usd(8) == "8.88 USD"