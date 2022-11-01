import unittest
from pizza import Pepperoni, Margherita, Hawaiian, Pizza
from click.testing import CliRunner
from cli import menu


real_menu = '''Menu:
Pepperoni 🍕: tomato sauce, mozzarella, pepperoni
Margherita 🧀: tomato sauce, mozarella, tomatoes
Hawaiian 🍍: tomato sauce, mozarella, chicken, pineapples
'''


class TestPizzas(unittest.TestCase):

    def test_pepperoni(self):
        pep_dict = Pepperoni().dict()
        expected = {'Pepperoni': ['tomato sauce', 'mozzarella', 'pepperoni']}
        self.assertEqual(pep_dict, expected)

    def test_margherita(self):
        mar_dict = Margherita().dict()
        expected = {'Margherita': ['tomato sauce', 'mozarella', 'tomatoes']}
        self.assertEqual(mar_dict, expected)

    def test_hawaiian(self):
        haw_dict = Hawaiian().dict()
        expected = {'Hawaiian': ['tomato sauce', 'mozarella', 'chicken',
                                 'pineapples']}
        self.assertEqual(haw_dict, expected)


class TestMainPizzaClass(unittest.TestCase):

    def test_pizza(self):
        pizza = Pizza(['cheese', 'sauce'])
        expected = {'Pizza': ['cheese', 'sauce']}
        self.assertEqual(pizza.dict(), expected)

    def test_pizza_size(self):
        pizza = Pizza(['cheese', 'sauce'], 'XL')
        self.assertEqual(pizza.size, 'XL')

    def test_pizza_size_invalid(self):
        with self.assertRaises(ValueError):
            Pizza(['cheese', 'sauce'], 'XXL')


class TestEquality(unittest.TestCase):

    def test_pizza_equality(self):
        pizza1 = Pizza(['cheese', 'sauce'])
        pizza2 = Pizza(['cheese', 'sauce'])
        self.assertEqual(pizza1, pizza2)

    def test_pizza_equality_different_size(self):
        pizza1 = Pizza(['cheese', 'sauce'], 'XL')
        pizza2 = Pizza(['cheese', 'sauce'], 'L')
        self.assertNotEqual(pizza1, pizza2)

    def test_pizza_equality_different_toppings(self):
        pizza1 = Pizza(['cheese', 'sauce'])
        pizza2 = Pizza(['cheese', 'sauce', 'tomatoes'])
        self.assertNotEqual(pizza1, pizza2)

    def test_pizza_equality_different_type(self):
        self.assertNotEqual(Pizza(['cheese', 'sauce']), Pepperoni())


class TestMenu(unittest.TestCase):

    def test_menu(self):
        runner = CliRunner()
        result = runner.invoke(menu)
        self.assertEqual(result.output, real_menu)
        self.assertEqual(result.exit_code, 0)
