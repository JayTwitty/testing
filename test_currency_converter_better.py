
import unittest

from currency_converter import usd_to_euro
from currency_converter import euro_to_usd
from currency_converter import usd_to_many

class UsdToEuroTestCase(unittest.TestCase):

    def test_usd_to_euro_converter(self):
        # assert usd_to_euro(1) == "0.9 EUR"

        self.assertEqual(usd_to_euro(1), "0.9 EUR")

    def test_usd_to_euro_converter_again(self):
        # assert usd_to_euro(8) == "7.2 EUR"

        self.assertEqual(usd_to_euro(8), "7.2 EUR")

class EuroToUsdTestCase(unittest.TestCase):

    def test_euro_to_usd_converter(self):
        # assert euro_to_usd(1) == "1.11 USD"

        self.assertEqual(euro_to_usd(1), "1.11 USD")

    def test_euro_to_usd_converter_again(self):
        # assert euro_to_usd(8) == "8.88 USD"

        self.assertEqual(euro_to_usd(8), "8.88 USD")

class UsdtoManyTestCase(unittest.TestCase):

    def test_usd_to_many_converter_for_one_value_in_the_list(self):
        # assert usd_to_many([5]) == ["5 USD converts to", '4 EUR', "3 GBP", '342 INR']
        self.assertEqual(usd_to_many([5]), ["5 USD converts to", '4 EUR', '3 GBP', '342 INR'])

        # assert usd_to_many([5, 10]) == ["5 USD converts to", '4 EUR', "3 GBP", '342 INR', "10 USD converts to", '9 EUR', "7 GBP", '684 INR']


        # assert usd_to_many([5, "a"]) ==  ["5 USD converts to", '4 EUR', "3 GBP", '342 INR'], print("You must enter a USD value to convert...")

