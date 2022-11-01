from config import acceptable_sizes, emojis


class Pizza:
    '''Main class for pizzas.
    Each type of pizza is inherited from this class.'''

    def __init__(self, toppings, size=None):
        self.toppings = toppings
        if size:
            if size in acceptable_sizes:
                self.size = size
            else:
                acceptable_sizes_str = ", ".join(acceptable_sizes)
                raise ValueError(f'Сhoose from: {acceptable_sizes_str}')
        else:
            self.size = None

    def __eq__(self, other):
        return self.size == other.size \
            and self.toppings == other.toppings \
            and self.__class__.__name__ == other.__class__.__name__

    def dict(self):
        return {self.__class__.__name__: self.toppings}


class PizzaMixin:
    '''Mixin for nice output of pizza'''

    def __repr__(self):
        pizza_name = self.__class__.__name__
        pizza_emote = emojis[pizza_name]
        ingredients = ', '.join(self.toppings)

        return f'{pizza_name} {pizza_emote}: {ingredients}'

# classes of pizzes we have in menu


class Pepperoni(Pizza, PizzaMixin):

    def __init__(self):
        super().__init__(self)
        self.toppings = ['tomato sauce', 'mozzarella', 'pepperoni']


class Margherita(Pizza, PizzaMixin):

    def __init__(self):
        super().__init__(self)
        self.toppings = ['tomato sauce', 'mozarella', 'tomatoes']


class Hawaiian(Pizza, PizzaMixin):

    def __init__(self):
        super().__init__(self)
        self.toppings = ['tomato sauce', 'mozarella', 'chicken', 'pineapples']
