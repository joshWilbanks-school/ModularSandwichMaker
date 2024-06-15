class Cashier:
    def __init__(self):
        pass

    def process_coins(self) -> float:
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("how many large dollars?: ") or 0)
        half_dollars = int(input("how many half dollars?: ") or 0)
        quarters = int(input("how many quarters?: ") or 0)
        nickels = int(input("how many nickels?: ") or 0)
        return dollars + half_dollars * .5 + quarters * .25 + nickels * .05

    def transaction_result(self, coins, cost) -> bool:
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            return False

        change = coins - cost
        if change > 0:
            print(f"Here is ${change} in change.")

        return True
