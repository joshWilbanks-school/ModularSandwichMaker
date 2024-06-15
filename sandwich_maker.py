
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients) -> bool:
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if ingredients.get(ingredient) > self.machine_resources.get(ingredient):
                print(f"Sorry there is not enough {ingredient}.")
                return False

        return True


    def make_sandwich(self, sandwich_size, order_ingredients: dict):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

        for ingredient in order_ingredients:
            amount = order_ingredients.get(ingredient)
            self.machine_resources[ingredient] -= amount

        print(f"{sandwich_size} sandwich is ready. Bon appetit!")