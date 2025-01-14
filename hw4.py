#Assignments: Python OOP Principles
'''
1. Encapsulation in Personal Budget Management

Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, 
focusing on the use of private attributes and getters and setters.

Problem Statement: You are required to build a Personal Budget Management application. 
The application will manage budget categories like food, entertainment, utilities, etc., 
ensuring that budget details remain private and are accessed or modified through public methods.

Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for 
category name and allocated budget. - Initialize these attributes in the constructor.

- Expected Outcome: A `BudgetCategory` class capable of storing category details securely. --- DONE

Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name 
and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

- Expected Outcome: Methods that allow controlled access and modification of the private attributes, 
with validation checks in place. --- DONE

Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget 
accordingly. - Validate the expense amount before making deductions from the budget.

Expected Outcome: Ability to track expenses per category and update the remaining budget safely. --- DONE

Task 4: Display Budget Details Create a method to display the details of a budget category, 
including the name, allocated budget, and remaining budget after expenses.

Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

Code Examples:

class BudgetCategory:
    # Constructor and private attributes
    # ...

    # Getters and setters for category name and budget
    # ...

    def add_expense(self, amount):
        # Method to add an expense to the category
        # ...

    def display_category_summary(self):
        # Method to display the budget category details
        # ...

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()


'''

class BudgetCategory:

    # Constructor and private attributes
    # constructor method with attributes such as the category name and budget. 
    def __init__(self, category_name, budget=0.0, initial_budget=0.0):
        self.category_name = category_name
        self.budget = budget
        self.initial_budget = budget
    # ...


    # Getters and setters for category name and budget
    # ...
    def get_budget(self):
        #print(f'This is the Getter Method. The Category Name is: {self.category_name},and The Budget is: {self.budget}')
        #print()
        return self.budget
    def get_category_name(self):
        return self.category_name

    #def setter(self):
    def set_budget(self, budget):
      if(budget >= 0):
        self.budget = budget

    def set_category_name(self, name):
        self.category_name = name

    # Method to add an expense to the category

    def add_expense(self, amount):
       if(amount <= self.budget):
            self.budget = self.budget - amount
            print(f'${amount:.2f} is your expense! Your new budget is: ${self.budget:.2f}!')
       else:
            print("The expense amount is greater than the budget!")
 
    # Method to display the budget category details
    def display_category_summary(self):
        print(f'This is the Category Summary. The Category Name is: {self.category_name}, The Allocated budget is: {self.initial_budget}, and The Remaining Budget is: {self.budget}')


    
food_category = BudgetCategory("Food", 500)
print()
food_category.add_expense(100)
print()
food_category.display_category_summary()
print()