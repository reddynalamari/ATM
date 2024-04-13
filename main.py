'''
Project: ATM
Author : Nalamari Shashidhar Reddy
Started Date: 04/09/2023
Completed Date: 13/02/2024
'''

import customtkinter as tk
from tkinter import messagebox as mb
from database import *
root = tk.CTk()
root.title("Shashidhar's ATM")
root.config(width=900, height=500)
root.resizable(False, False)

class app:
    def __init__(self):
        self.frame1f()

    def frame1f(self):
        try:
            self.frame2.destroy()
        except:
            pass

        self.frame1 = tk.CTkFrame(master=root, fg_color="#639ED2", height=382, width=696)
        self.frame1.place(x=10, y=10)

        main_lable = tk.CTkLabel(master=self.frame1, text="ATM", \
                                 font=("Helvetica", 50, "bold"), fg_color="#639ED2", text_color="#B50029")
        main_lable.place(x=300, y=15)

        self.acc_number_entry = tk.CTkEntry(master=self.frame1)
        self.acc_number_entry.place(x=282, y=125)
        acc_num_label = tk.CTkLabel(master=self.frame1, text="ACCOUNT NUMBER", \
                                    font=("Helvetica", 18, "bold"), fg_color="#639ED2", text_color="#085D00")
        acc_num_label.place(x=265, y=165)

        self.pin_entry = tk.CTkEntry(master=self.frame1)
        self.pin_entry.place(x=282, y=220)
        pin_label = tk.CTkLabel(master=self.frame1, text="PIN NUMBER", \
                                font=("Helvetica", 18, "bold"), fg_color="#639ED2", text_color="#085D00")
        pin_label.place(x=300, y=260)

        login_button = tk.CTkButton(text="LOG-IN", master=self.frame1, command=self.validate_account, fg_color="#4CAF50")
        login_button.place(x=282, y=325)

    def frame2f(self):
        try:
            self.frame1.destroy()
        except:
            pass
        self.frame2 = tk.CTkFrame(master=root, fg_color="#639ED2", height=382, width=696)
        self.frame2.place(x=10, y=10)
        self.logout_button = tk.CTkButton(text="LOG-OUT", master=self.frame2, \
                                          command=self.frame1f, fg_color="#FF5733", font=("Helvetica", 13, "bold"))
        self.logout_button.place(x=15, y=15)

        # Add transaction buttons and functionalities here
        balance_button = tk.CTkButton(text="Check Balance", master=self.frame2, command=self.check_balance, fg_color="#4CAF50")
        balance_button.place(x=15, y=70)
        withdraw_button = tk.CTkButton(text="Withdraw", master=self.frame2, command=self.withdraw, fg_color="#4CAF50")
        withdraw_button.place(x=15, y=120)
        deposit_button = tk.CTkButton(text="Deposit", master=self.frame2, command=self.deposit, fg_color="#4CAF50")
        deposit_button.place(x=15, y=170)

    def validate_account(self):
        acc_num = self.acc_number_entry.get()
        pin_num = self.pin_entry.get()
        # You should implement account validation logic here based on your database
        # For this example, we'll assume a simple dictionary-based account validation
        valid_accounts = {
            '123': '123',
            '987654': '5678'
        }
        if acc_num in valid_accounts and pin_num == valid_accounts[acc_num]:
            self.frame2f()
        else:
            mb.showerror("Invalid Account", "Invalid account number or PIN")

    def check_balance(self):
        # Implement the logic to check the account balance here
        # You can retrieve the account balance from your database
        mb.showinfo("Account Balance", "Your balance is $1000")  # Placeholder balance

    def withdraw(self):
        # Implement the logic to perform a withdrawal here
        # Deduct the amount from the account balance in your database
        mb.showinfo("Withdrawal", "Withdrawal successful")  # Placeholder message

    def deposit(self):
        # Implement the logic to perform a deposit here
        # Add the amount to the account balance in your database
        mb.showinfo("Deposit", "Deposit successful")  # Placeholder message

a = app()
root.mainloop()
