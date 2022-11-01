import click
from pizza import Pizza, Pepperoni, Margherita, Hawaiian
from decors import log


@log('🍳 cooking took {} seconds')
def bake(pizza):
    '''Bake a pizza'''


@log('🚲 delivery took {} seconds')
def delivery_order():
    '''Deliver the pizza'''


@log('🏠 pickup took {} seconds')
def pickup_order():
    '''The customer took the pizza'''


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True, help='Add delivery')
@click.option('--pickup', default=False, is_flag=True, help='Add pickup')
@click.argument('pizza', nargs=-1, required=True)
def order(pizza: str, delivery: bool, pickup: bool):

    if pizza[0] not in [pizza_.__name__ for pizza_ in Pizza.__subclasses__()]:
        print('Choose a pizza from the menu')
        print('You can see the menu by typing using the command: menu')
    else:

        if pizza[0] == 'Pepperoni':
            ordered_pizza = Pepperoni()
        elif pizza[0] == 'Margherita':
            ordered_pizza = Margherita()
        elif pizza[0] == 'Hawaiian':
            ordered_pizza = Hawaiian()

        bake(ordered_pizza)

        if delivery:
            print('We will deliver as fast as possible!')
            delivery_order()
        if pickup:
            print('We will prepare your pizza as fast as possible!')
            pickup_order()

        print('Bon appetit!')


@cli.command()
def menu():
    print('Menu:')
    for pizza_ in Pizza.__subclasses__():
        print(pizza_())


if __name__ == '__main__':
    cli()
