from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu ( )
make_coffee = CoffeeMaker ( )
pro_coins = MoneyMachine ( )

'''my code'''
#print(f"You order {find.name} drink. It'll cost ${find.cost} and need {find.ingredients}.")
#print(make_coffee.is_resource_sufficient(find))
is_on= True 
while is_on:
    chosen_drink = input (f"what drink would you like {menu.get_items ( )}\n>>")
    find = menu.find_drink (chosen_drink)    
    if chosen_drink== 'report':
        make_coffee.report()
        pro_coins.report()
    elif make_coffee.is_resource_sufficient (find)and pro_coins.make_payment (find.cost):
        make_coffee.make_coffee(find)
    else:
        is_on= False
        
'''solution'''        
# is_on= True
# while is_on:
#     option= menu.get_items()
#     choice= input(f"What would u like {option} ")
#     if choice=='off':
#         is_on=False
#     elif choice=='report':
#         make_coffee.report()
#         pro_coins.report()
#     else:
#         drink= menu.find_drink(choice)
#         if make_coffee.is_resource_sufficient(drink) and pro_coins.make_payment(drink.cost):
#             make_coffee.make_coffee(drink)
            