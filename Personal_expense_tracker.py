expense_list =[]
class Expense:
    def add_expense(self):
        self.web = {}
        self.expense_ID = int(input("Enter Expense ID = "))
        self.amount = float(input("Enter Amount = "))
        self.description = input("Enter Description = ")
        self.category = input("Enter Category = ")
        self.date = input("Enter Your Date = ")
        if self.amount>0 :
            self.web["expense_ID"] = self.expense_ID
            self.web["amount"] = self.amount
            self.web["description"] = self.description
            self.web["category"] = self.category
            self.web["date"] = self.date
            expense_list.append(self.web)
            print("Expense added Successfully!")
            
    def view_expense(self):
        if expense_list==[]:
            print("There are no expense at this time!!")
            print("======================================================")
        else :    
            for i in expense_list:
                print(f"expense ID = {i["expense_ID"]}")
                print(f"amount = {i["amount"]}")
                print(f"description = {i["description"]}")
                print(f"category = {i["category"]}")
                print(f"date = {i["date"]}")
                print("____________________________________________________________________________")
                print("All Expense Displayed Successfully!!")
            
    def update_expense(self):
        if expense_list==[]:
            print("There are no expense at this time!!")
            print("=====================================================")
        else :
            c = 0
            self.log = {}
            self.a = int(input("Enter your expense_ID = "))
            for i in expense_list:
                if i["expense_ID"]==self.a :
                    self.expense_ID = int(input("Enter Expense ID = "))
                    self.amount = float(input("Enter Amount = "))
                    self.description = input("Enter Description = ")
                    self.category = input("Enter Category = ")
                    self.date = input("Enter Your Date = ")
                    if self.amount>0 :
                        self.log["expense_ID"] = self.expense_ID
                        self.log["amount"] = self.amount
                        self.log["description"] = self.description
                        self.log["category"] = self.category
                        self.log["date"] = self.date
                        expense_list[c] = self.log
                        print("Expense Updated Successfully!!") 
                c = c+1
            else :
                print("Expense ID Not Found!")
            
    def remove_expense(self):
        if expense_list==[]:
            print("There are no expense at this time!!")
            print("===================================================")
        else :
            self.b = int(input("Enter your expense_ID = "))
            for i in expense_list:
                if i["expense_ID"]==self.b :
                    expense_list.remove(i)
            
    def search_expense(self):
        if expense_list==[]:
            print("There are no expense at this time!!")
            print("==============================================")
        else :
            self.c = int(input("Enter your expense_ID = "))
            for i in expense_list:
                if i["expense_ID"]==self.c :
                    print(f"expense_ID = {i["expense_ID"]}")
                    print(f"amount = {i["amount"]}")
                    print(f"description = {i["description"]}")
                    print(f"category = {i["category"]}")
                    print(f"date = {i["date"]}")
                    
    def sort_expense(self):
        pass
    def Statictis_expense(self):
        c = 0
        for i in expense_list:
            c = c+i["amount"]
        print(f"Total expense is {c}")
        print("======================================")

print("Welcome To Personal Expense Tracker")
while True :    
    print("1.Add a new expense")
    print("2.View all expenses")
    print("3.Update an existing expense")
    print("4.Delete an expense")
    print("5.search for an expense")
    print("6.Display expenses sorted by date or amount")
    print("7.Display Statictis")
    print("8.Exit")
    
    choice = int(input("Enter the choice = "))
    print("____________________________________________________________________________")
    if choice==1:
        try :
            e1 = Expense()
            e1.add_expense()    
            print(expense_list)
        except :
            print("You Haved Entered Invalid Datatype!")
    elif choice==2:
        e2 = Expense()
        e2.view_expense()
    elif choice==3:
        try :
            e3 = Expense()
            e3.update_expense()
            print(expense_list)
        except :
            print("You Haved Entered Invalid Datatype!")
    elif choice==4:
        try :
            e4 = Expense()
            e4.remove_expense()
            print(expense_list)
        except :
            print("You Haved Entered Invalid Datatype!")
    elif choice==5:
        try :
            e5 = Expense()
            e5.search_expense()
        except :
            print("You Haved Entered Invalid Datatype!")
    elif choice==6:
        try :
            e6 = Expense()
            e6.sort_expense()
        except :
            print("You Haved Entered Invalid Datatype!")
    elif choice==7:
        try :
            e7 = Expense()
            e7.Statictis_expense()
        except :
            print("You Haved Entered Invalid Datatype!")
    elif choice==8:
        print("Thank You For using Personal Expense Tracker!")
        print("Byee!!")
        break
    else :
        print("Invalid Output !Enter Proper Choice.")