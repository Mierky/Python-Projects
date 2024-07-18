class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        # Header
        title = f"{self.name:*^30}\n"

        # Ledger entries
        items = ''
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            # Only take the first 23 characters of the description, if it's longer
            description = item['description'][:23]
            # Ensure the formatting is correct
            items += f"{description:<23}{amount:>7}\n"

        # Total balance
        total = f"Total: {self.get_balance():.2f}"

        return title + items + total


def create_spend_chart(categories):
    total_spent = 0
    spent_per_category = []

    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spent_per_category.append((category.name, spent))
        total_spent += spent

    # Calculate percentage spent per category
    percentages = [(name, (spent / total_spent) * 100) for name, spent in spent_per_category]

    # Format the chart
    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for name, percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    # Find the longest category name
    max_len = max(len(category.name) for category in categories)

    # Format the category names vertically
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))