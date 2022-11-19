class ROI():
    def __init__(self, name):
        self.name = name

# Add income into specified name of user
    def add_income(self):
        self.income = int(input("What is your total montly rental income? :$"))


# Add expenses based on variables such as: tax, insurance, utilities, HOA, lawn, vacancy, repairs, copex, property management, and mortage.
    def add_expenses(self):
        self.expenses = {}
        self.expenses['tax'] = int(input("What are your monthly taxes on the property? :$"))
        self.expenses['insurance'] = int(input("How much are you paying in insurance? :$"))
        self.expenses['utilities'] = int(input("How much do you typically spend on utilities each month? This can include: electric, water, sewage, garbage, and gas. :$"))
        self.expenses['HOA'] = int(input("How much does the property's HOA cost? :$"))
        self.expenses['lawn/snow'] = int(input("How much do you spend on lawn/snow care? :$"))
        self.expenses['vacancy'] = int(input("How much money do you put into vacancy? :$"))
        self.expenses['repairs'] = int(input("How much money do you put into repairs? :$"))
        self.expenses['CopEx'] = int(input("How money do you put into CopEx? :$"))
        self.expenses['property management'] = int(input("How much do you pay your property manager a month? :$"))
        self.expenses['mortage'] = int(input("How much is the mortage each month? :$"))

        # self.tax = int(input("What are your monthly taxes on the property?"))
        # self.expenses['tax'] = self.tax

# Calculate cash flow by using: income - expense
    def cash_flow(self):
        self.cash_flow_total = self.income - sum(self.expenses.values())
        print(input(f"${self.cash_flow_total} is your CASH FLOW on the month!"))

# Add in down payment, closing cost, repair budget, and misc expenses
    def total_investment(self):
        self.investment = {}
        self.investment['down_payment'] = int(input("What was your initial down payment on the property? :$"))
        self.investment['closing_cost'] = int(input("What was the closing cost of the contract? :$"))
        self.investment['repair_cost'] = int(input("How much did you spend in repairing the property? :$"))
        self.investment['misc'] = int(input("Were there any other expenses in the initial purchasing of the property? :$"))


# Take cash flow divided by fixed number of months(12)
    def annual_cash_flow(self):
        self.annual_cash_flow_total = self.cash_flow_total * 12
        print(f"${self.annual_cash_flow_total} is your annual cash flow yearly!")

# Take the annual cash flow divided by the total investment
# "{:.2%}" = the amount of decimals you would like to include in the answer
    def Cash_on_Cash_ROI(self):
        self.Cash_on_Cash_ROI_calculation = self.annual_cash_flow_total / sum(self.investment.values())
        self.percentage_ROI = "{:.2%}".format(self.Cash_on_Cash_ROI_calculation)
        print(f"${self.percentage_ROI} is your CASH on CASH Return On Investment for this property!")


# Script for questionaire
# Driver / most prompts will fall under here...
    def main(self):
        self.add_income()
        self.add_expenses()
        self.cash_flow()
        self.total_investment()
        self.annual_cash_flow()
        self.Cash_on_Cash_ROI()


Test_trial = ROI('Test')
Test_trial.main()
