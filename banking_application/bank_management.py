import uuid
import json


class BankManagementSystem:
    """manage bank account"""

    def create_account(self, new_bank):
        """Create a new account and save the customer's details.
        Args:
        new_bank (dict): Account details to be added. """

        new_bank["Account Number"] = int(str(uuid.uuid4().int)[:12])
        new_bank["Status"] = "active"
        with open("bank.txt", "a") as file:
            file.write(json.dumps(new_bank) + "\n")
        print("________!!CONGRATULATIONS!!____________")
        print("________Account Created Successfully_____")
        print("______Account Details________")
        print(new_bank)
        print("")

    def view_account_details(self, account_number):
        """Display account details for the given account number.
        Args:
        account_number (int): Account number to search for."""

        found = False
        with open("bank.txt", "r") as file:
            for line in file:
                if not line.strip():
                    continue
                account = json.loads(line)
                if str(account.get("Account Number")) == str(account_number):
                    print("Account Details:")
                    print(account)
                    found = True
                    break
        if not found:
            print(" _____Account Does Not Exist!______ ")

    def deposit_money(self, amount_to_deposit, account_number):
        """Deposit money into the specified account.
        Args:
            amount_to_deposit (int): Amount to deposit.
            account_number (int): Account number to deposit into."""

        current_balance = 0
        found = False
        update_content = []
        if int(amount_to_deposit) > 0:
            with open("bank.txt", "r") as file:
                for line in file:
                    if line.strip():
                        account = json.loads(line)
                        if str(account.get(str("Account Number"))) == str(account_number):
                            account["Balance"] += amount_to_deposit
                            current_balance = account["Balance"]
                            found = True
                            update_content.append(account)
                        else:
                            update_content.append(account)
        else:
            print("_______Enter Valid Value_______")
            return
        if not found:
            print("______Account not found._______")
            return
        else:
            with open("bank.txt", "w") as file:
                for i in update_content:
                    file.write(json.dumps(i) + "\n")
            print("______!!Credit Alert!!_____")
            print(f"________Your Account Is Credited By Amount {amount_to_deposit}_______")
            print(f"_________Your Current Balance Is {current_balance}___________")

    def withdraw_money(self, amount_to_withdraw, account_number):
        """Withdraw the given amount from the specified account.

    Args:
        amount_to_withdraw (int): Amount to withdraw.
        account_number (int): Account number to withdraw from.
    """

        found = False
        content = []
        current_balance = 0
        with open("bank.txt", "r") as file:
            for line in file:
                if line.strip():
                    account = json.loads(line)
                    if str(account.get(str("Account Number"))) == str(account_number):
                        if int(account.get("Balance")) >= int(amount_to_withdraw):
                            found = True
                            account["Balance"] -= amount_to_withdraw
                            current_balance = account["Balance"]
                            content.append(account)
                        else:
                            found = True
                            print(f"Insufficient balance: only {account['Balance']} Rs. available.")
                            return
                    content.append(account)
        if not found:
            print("__________This Account Does Not Exist___________")
        else:
            with open("bank.txt", "w") as file:
                for i in content:
                    file.write(json.dumps(i) + "\n")
            print("_________!!Debit Alert!!__________")
            print(f"____Your Account Is Debited By Amount {amount_to_withdraw}______")
            print(f"_______Your Current Balance Is {current_balance}_________")

    def update_account_details(self, account_number):
        """Update the customer's details for the specified account.
        Args:
            account_number (int): Account number to update."""

        content = []
        found = False
        with open("bank.txt", "r") as file:
            for line in file:
                if line.strip():
                    account = json.loads(line)
                    
                    if str(account.get(str("Account Number"))) == str(account_number):
                        found = True
                        print("____Your Account Details Are______")
                        for key, value in account.items():
                            print(f"{key} : {value}")
                        while True:
                            edit_num = input("Enter New Phone Number: ")

                            if edit_num.isdigit() and len(edit_num) == 10:
                                account["Phone Number"] = edit_num
                                break
                            elif len(edit_num) < 10:
                                print("Invalid Phone Number. Please enter exactly 10 digits.") 
                        edit_name = input("Enter Name: ")
                        if edit_name:
                            account["Name"] = edit_name
                        
                        content.append(account)
                    else:
                        content.append(account)
        if not found:
            print("_______This Account Does Not Exist_________")
            return
        else:
            with open("bank.txt", "w") as file:
                for i in content:
                    file.write(json.dumps(i) + "\n")
            print("_____Details Updated Succesfully_______")

    def transfer_money(self, owner_account_number, receiver_account_number, amount_to_transfer):
        """Transfer money from one account to another.
        Args:
            owner_account_number (int): Sender's account number.
            receiver_account_number (int): Receiver's account number.
            amount_to_transfer (int): Amount to transfer."""

        content = []
        owner_found = False
        rcvr_found = False

        with open("bank.txt", "r") as file:
            for line in file:
                if line.strip():
                    account = json.loads(line)
                    if str(account.get(str("Account Number"))) == str(owner_account_number):
                        if int(account.get("Balance")) >= int(amount_to_transfer):
                            owner_found = True
                            account["Balance"] -= amount_to_transfer
                        elif int(account.get("Balance")) < int(amount_to_transfer):
                            owner_found = True 
                            print("Insufficient Balance!")
                            return
                        content.append(account)
                    elif str(account.get(str("Account Number"))) == str(receiver_account_number):
                        rcvr_found = True
                        account["Balance"] += amount_to_transfer
                        content.append(account)
                    else:
                        content.append(account)
        if not rcvr_found:
            print("  ")
            print("___Can Not Transfer As This Account Does Not Exist___")
            print(" ")
        elif not owner_found:
            print(" ")
            print("____You Don't Have This Account Enter Valid Account Number____")
            print(" ")
        else:
            with open("bank.txt", "w") as file:
                for i in content:
                    file.write(json.dumps(i) + "\n")
            print(f"______Done Transaction Of {amount_to_transfer} Rs:- ______")
    
    def deactivate_account(self, account_number):
        """Deactivate the specified bank account.
        Args:
            account_number (int): Account number to deactivate."""

        content = []
        found = False
        with open("bank.txt", "r") as file:
            for line in file:
                if line.strip():
                    account = json.loads(line)
                    if str(account.get(str("Account Number"))) == str(account_number):
                        found = True
                        account["Status"] = "Inactive"
                        account["Balance"] = 0
                        content.append(account)
                    else:
                        content.append(account)
        if not found:
            print("______Can Not Close This Account As Account Does Not Exist_____")
        else:
            with open("bank.txt", "w") as file:
                for i in content:
                    file.write(json.dumps(i) + "\n")  
            print("____Account Closed Succesfully_____")

    def account_exist(self, account_number):
        """ Check whether the account exist or not.
        Args:
         account_number (int): account number to check"""
        with open("bank.txt", "r") as file:
           for line in file:
                if line.strip():
                    account = json.loads(line)
                    if str(account.get(str("Account Number"))) == str(account_number):
                        return True
        return False


bank_management_system = BankManagementSystem()
while True:
    print("________________________")
    print("Welcome to the Bank Management System")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Update Account")
    print("6. Transfer Money")
    print("7. Close Account")
    print("8. Exit")
    print("________________________")


    choice = input("Enter your choice (1-8): ")
    try:
        i = int(choice)
    except ValueError:
        print("Invalid Input. Please Enter Number Between 1 And 6.")
        continue            

    match choice:
        case "1":
            print("___Fill The Details Below__")
            print("___________________________")
           
            while True:
                add_name  = input("Enter Your Name: ").strip().lower()
                if add_name: 
                    break
                print("Input cannot be empty. Please try again.")
            while True:
                add_age = int(input("Enter Your Age: "))
                if add_age and add_age >= 18:
                    break
                elif add_age < 18:
                    print("Age Can Not Be Less Than 18")
                else:
                    print("Input cannot be empty. Please try again.")
            while True:
                add_phone_number = (input("Enter Your 10-Digit Phone Number: "))
                if add_phone_number.isdigit() and len(add_phone_number) == 10:
                    break
                elif len(add_phone_number) < 10 or len(add_phone_number) > 10:
                    print("Invalid Phone Number. Please enter exactly 10 digits.") 
                else:
                    print("Input cannot be empty. Please try again.")
            while True:
                add_balance = int(input("Enter The Amount To Deposit ")) 
                if add_balance > 0:
                    break
                elif add_balance <= 0:
                    print("Enter Value Greater Than Zero")
                else:
                    print("Input cannot be empty. Please try again.")
            new_bank = {
                "Name": add_name,
                "Age": add_age,
                "Phone Number": "+91-" + add_phone_number,  
                "Balance": add_balance
            }
            bank_management_system.create_account(new_bank)
        case "2":
            print("______________________________")
            account_number = input("Enter Account Number: ")
            bank_management_system.view_account_details(account_number)
        case "3":
            print("______________________________")
            account_number = int(input("Enter Account Number: "))
            amount_to_deposit = int(input("Enter The Amount: "))

            bank_management_system.deposit_money(amount_to_deposit, account_number)
        case "4":
            print("______________________________")
            account_number = int(input("Enter Account Number: "))
            amount_to_withdraw = int(input("Enter The Amount: "))

            bank_management_system.withdraw_money(amount_to_withdraw, account_number)
        case "5":
            print("______________________________")
            account_number = int(input("Enter Account Number: "))

            bank_management_system.update_account_details(account_number)
        case "6":
            print("______________________________")
            while True:
                owner_account_number = int(input("Enter Your Account Number: "))
                # c= bank_management_system.account_exist(owner_account_number)
                if bank_management_system.account_exist(owner_account_number):
                    break
                print("Account Does Not Exist. Try Again")
            while True:
                receiver_account_number = int(input("Enter Receiver's Account Number To Transfer: "))
                if bank_management_system.account_exist(receiver_account_number):
                    break
                print("Account Does Not Exist. Try Again")
            
            amount_to_transfer = int(input("Enter The Amount: "))

            bank_management_system.transfer_money(owner_account_number, receiver_account_number, amount_to_transfer)
        case "7":
            print("_______________________________")
            account_number = int(input("Enter Account Number: "))

            bank_management_system.deactivate_account(account_number)
        case "8":
            print("______________________________")
            print("_____Existing The Program_____")
            break