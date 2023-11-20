class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23} {item['amount']:7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [sum(item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories]
    total_spent = sum(spendings)
    percentages = [int(spending / total_spent * 100) for spending in spendings]

    for i in range(100, -1, -10):
        chart += f"{i:3}| {''.join(['o' if percentage >= i else ' ' for percentage in percentages])}  \n"
    chart += "    ----------\n"

    max_len = max(len(category.category) for category in categories)
    for i in range(max_len):
        chart += "     " + '  '.join(category.category[i] if i < len(category.category) else ' ' for category in categories) + "  \n"

    return chart.strip()


# Example usage:
food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")
transfer_status = food.transfer(50, clothing)

print(food)
print(clothing)
print(create_spend_chart([food, clothing]))
