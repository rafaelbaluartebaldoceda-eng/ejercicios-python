class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amount,description=""):
        self.ledger.append({'amount': amount, 'description': description })
    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    def transfer(self,amount,other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    def check_funds(self,amount):
        if amount>self.get_balance():
            return False
        else:
            return True
    def __str__(self):
        title=self.name.center(30,"*")
        items=""
        for item in self.ledger:
            linea=f"{item['description'][:23]:<23}{item['amount']:>7.2f}"
            items+=linea+"\n"
        total=f"Total: {self.get_balance()}"
        return title+"\n" + items + total
def create_spend_chart(categories):
    spent = []
    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_spent += item['amount']
        spent.append(total_spent)
    
    total = sum(spent)
    percentages = [(s / total * 100) // 10 * 10 for s in spent]
    chart = "Percentage spent by category\n"
    for nivel in range(100, -1, -10):
        row = str(nivel).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= nivel:
                row += "o  "
            else:
                row += "   "
        chart += row + "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        row = "     "
        for category in categories:
            if i < len(category.name):
                row += category.name[i] + "  "
            else:
                row += "   "
        chart += row + "\n"
    
    return chart.rstrip("\n")