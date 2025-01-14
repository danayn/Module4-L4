# Method to add an expense to the category

def add_expense(self, amount):
    if(amount <= self.budget):
        self.budget = self.budget - amount
        print(f'${amount:.2f} is your expense! Your new balance is: ${self.budget:.2f}!')
    else:
        print("The expense amount is greater than the budget!")
