class Budget:
    ''' An app to keep track of your spending '''

    def __init__(self, categorie):
        # Constroctor for the Budget class
        self.categorie = categorie
        self._amount_balance = 0

    def balance(self):
        # Returns the remanining balance
        print(("Your current Budget balance for {} is N{}.".format(self.categorie,
                                                                   self._amount_balance)).center(100))

    def transfer(self, catego, amount):
        # To transfer money to another budget category
        if amount > self._amount_balance:
            return "You can't Transfer more than the amount you have in your account."
        else:
            self._amount_balance = self._amount_balance - amount
            print()
            print(("N{} has been transfered to {} Budget.".format(
                amount, catego.categorie)).center(100))
        catego._amount_balance = catego._amount_balance + amount
        print()
        print(("Your new Budget balance for {} is N{}.".format(
            self.categorie, self._amount_balance)).center(100))
        print("*"*100)

    def add_money(self, amount):
        assert type(
            amount) == int and amount > 0, "The amount must be a number greater than zero."
        self._amount_balance = self._amount_balance + amount
        print()
        print((" N{} has been added to your {} Budget.".format(
            amount, self.categorie)).center(100))
        print("^"*100)
        print(("Your new Budget balance for {} is N{}.".format(
            self.categorie, self._amount_balance)).center(100))
        print("*"*100)


# Some category instances based on the Budget class
budget_food = Budget("Food")
budget_cloth = Budget("Cloth")
budget_house = Budget("House")
budget_tp = Budget("Transportation")
budget_wife = Budget("Marriage")

budget_food.add_money(20000)  # Add 20k to the food Budget
budget_cloth.add_money(50000)  # Add 50k to Cloth budget
budget_house.add_money(500000)  # add 500k to the House Budget

# Transfer 4500 from the Cloth Budget to the Transportation Budget
budget_cloth.transfer(budget_tp, 4500)
# Transfer 20k from the Cloth Budget to the Marriage Budget
budget_cloth.transfer(budget_wife, 20000)
# Add more 200k for the wife. increasing Marriage budget from 20k to 220k
budget_wife.add_money(200000)

# Print the current balance of all the Budget categories using the balance method
print()
budget_food.balance()
budget_cloth.balance()
budget_house.balance()
budget_tp.balance()
budget_wife.balance()
