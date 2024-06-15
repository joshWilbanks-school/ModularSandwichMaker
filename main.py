import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    loop = True

    while loop:

        user_input = input("What would you like? (small / medium / large / off / report): ")
        user_input = user_input.lower()
        size = None

        if user_input == "off":
            break

        elif user_input == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources.get("bread")} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources.get("ham")} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources.get("cheese")} pound(s)")
            continue

        elif user_input == "small":
            size = "small"

        elif user_input == "medium":
            size = "medium"

        elif user_input == "large":
            size = "large"
        else:
            print("Please only input one of the above listed words.")
            continue

        recipe = recipes.get(size)

        enough_resources = sandwich_maker_instance.check_resources(recipe.get("ingredients"))
        if not enough_resources:
            continue

        print("Please insert coins.\n")
        coins = cashier_instance.process_coins()

        transaction_result = cashier_instance.transaction_result(coins, recipe.get("cost"))

        if not transaction_result:
            print("Sorry, that's not enough money. Money refunded.")
            continue

        sandwich_maker_instance.make_sandwich(size, recipe.get("ingredients"))

if __name__=="__main__":
    main()
