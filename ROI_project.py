class ROI():
    def __init__(self, name):
        self.name = name

# Add income into specified name of user
    def add_income(self):
        # self.income = int(input("What is your total montly rental income? :$"))
        while True:
            try:
                self.income = int(input("What is your total montly rental income? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")


# Add expenses based on variables such as: tax, insurance, utilities, HOA, lawn, vacancy, repairs, copex, property management, and mortage.
    def add_expenses(self):
        self.expenses = {}
        values = self.expenses.values()
        keys = self.expenses.keys()

        # self.expenses['tax'] = int(input("What are your monthly taxes on the property? :$"))
        while True:
            try:
                self.expenses['tax'] = int(input("What are your monthly taxes on the property? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")
        
        # self.expenses['insurance'] = int(input("How much are you paying in insurance? :$"))
        while True:
            try:
                self.expenses['insurance'] = int(input("How much are you paying in insurance? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.expenses['utilities'] = int(input("How much do you typically spend on utilities each month? This can include: electric, water, sewage, garbage, and gas. :$"))
        while True:
            try:
                self.expenses['utilities'] = int(input("How much do you typically spend on utilities each month? This can include: electric, water, sewage, garbage, and gas. :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.expenses['HOA'] = int(input("How much does the property's HOA cost? :$"))
        while True:
            try:
                self.expenses['HOA'] = int(input("How much does the property's HOA cost? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.expenses['lawn/snow'] = int(input("How much do you spend on lawn/snow care? :$"))
        while True:
            try:
                self.expenses['lawn/snow'] = int(input("How much do you spend on lawn/snow care? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.expenses['vacancy'] = int(input("How much money do you put into vacancy? :$"))
        while True:
            try:
                self.expenses['vacancy'] = int(input("How much money do you put into vacancy? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.expenses['repairs'] = int(input("How much money do you put into repairs? :$"))
        while True:
            try:
                self.expenses['repairs'] = int(input("How much money do you put into repairs? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.expenses['CopEx'] = int(input("How money do you put into CopEx? :$"))
        while True:
            try:
                self.expenses['CopEx'] = int(input("How money do you put into CopEx? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.expenses['property management'] = int(input("How much do you pay your property manager a month? :$"))
        while True:
            try:
                self.expenses['property_management'] = int(input("How much do you pay your property manager a month? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")
        
        # self.expenses['mortage'] = int(input("How much is the mortage each month? :$"))
        while True:
            try:
                self.expenses['mortage'] = int(input("How much is the mortage each month? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        self.expenses_total = sum(self.expenses.values())
        # self.tax = int(input("What are your monthly taxes on the property?"))
        # self.expenses['tax'] = self.tax

# Calculate cash flow by using: income - expense
    def cash_flow(self):
        self.cash_flow_total = self.income - self.expenses_total
        print(input(f"${self.cash_flow_total} is your CASH FLOW on the month!\n\tPress Enter to Continue!"))

# Add in down payment, closing cost, repair budget, and misc expenses
    def total_investment(self):
        self.investment = {}
        # self.investment['down_payment'] = int(input("What was your initial down payment on the property? :$"))
        while True:
            try:
                self.investment['down_payment'] = int(input("What was your initial down payment on the property? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.investment['closing_cost'] = int(input("What was the closing cost of the contract? :$"))
        while True:
            try:
                self.investment['closing_cost'] = int(input("What was the closing cost of the contract? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.investment['repair_cost'] = int(input("How much did you spend in repairing the property? :$"))
        while True:
            try:
                self.investment['repair_cost'] = int(input("How much did you spend in repairing the property? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")

        # self.investment['misc'] = int(input("Were there any other expenses in the initial purchasing of the property? :$"))
        while True:
            try:
                self.investment['misc'] = int(input("Were there any other expenses in the initial purchasing of the property? :$"))
                break
            except ValueError:
                print("Invalid response. Please enter a financial number.")


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

    def person(self, first_name, last_name, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address


# Script for questionaire
# Driver / most prompts will fall under here...
    def main(self):
        credential_dict = {}

        greetings = input("Welcome ROI Calculator! If you would like to proceed with your calculations... \n\tpress (ENTER). ")
        print("First, we would like to know whom we are working with!")

        credentials = input("Would you like to continue? (y/n) :")
        yes_choices = ['yes', 'y']
        no_choices = ['no', 'n']

        while True:
            if credentials.lower() in yes_choices:
                first_name = input("What is your first name? :").lower()
                last_name = input("What is your last name? :").lower()
                email = input("What would be a good email to contact you with? :").lower()
                address = input("Lastly, what is the address of the property you are looking to calculate? :").lower()
                full_name = first_name + ' ' + last_name
                new_user = (first_name, last_name, address, email)
                credential_dict[new_user] = full_name
                break

            elif credentials.lower() in no_choices:
                print("Thank you foor your time and please come back if you would like your ROI calculated! ")
                quit()
                
            else:
                print("I'm sorry. This is not an accepted answer. Please answer (y/n). :")
                raise self.main()
                
        print(f"Thank you {full_name.title()}, Now to proceed with your ROI calculations. ")
             
        print("First, you will add your rental income.")     
        self.add_income()
        print("Now input the expenses that comes with maintaining the property.")
        self.add_expenses()
        print("With this information, we can now find your monthly CASH flow!")
        self.cash_flow()
        print("How much did you invest into this property? Answer the following prompts: ")
        self.total_investment()
        print("By taking your monthly CASH flow and multiplying it by 12 months in a year, you will get your annual Cash flow!")
        self.annual_cash_flow()
        print("To find your Cash on Cash Return on Investment, we will divide your annual CASH flow by the total amount of investments you made on the property!")
        self.Cash_on_Cash_ROI()
        print("With this information, you can dictate if your investment in this property is benefiting you!")

        # final_options = input("What else can we help you with today?\nCreate new ROI Calculation | Show ROI Calculation | Quit Program")


Test_trial = ROI('Test')
Test_trial.main()
