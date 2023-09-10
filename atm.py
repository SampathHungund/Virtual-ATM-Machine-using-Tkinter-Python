import tkinter as tk
from tkinter import messagebox


account_data = {
    '123456': {'name': 'Vineet Kumar', 'balance': 1000000 , 'pin': '1234'}
}

def check_balance():
    account_number = account_number_entry.get()
    pin = pin_entry.get()

    if account_number in account_data:
        if pin == account_data[account_number]['pin']:
            balance = account_data[account_number]['balance']
            messagebox.showinfo('Balance', f'Your balance is: Rs {balance}')
        else:
            messagebox.showerror('Error', 'Incorrect PIN')
    else:
        messagebox.showerror('Error', 'Account not found')

def withdraw():
    account_number = account_number_entry.get()
    pin = pin_entry.get()
    amount = float(amount_entry.get())

    if account_number in account_data:
        if pin == account_data[account_number]['pin']:
            balance = account_data[account_number]['balance']
            if amount <= balance:
                account_data[account_number]['balance'] -= amount
                messagebox.showinfo('Success', f'Withdrawn: Rs {amount}\nNew balance: Rs {balance - amount}')
            else:
                messagebox.showerror('Error', 'Insufficient Money')
        else:
            messagebox.showerror('Error', 'Incorrect PIN')
    else:
        messagebox.showerror('Error' , 'Account not found')

def deposit():
    account_number = account_number_entry.get()
    pin = pin_entry.get()
    amount = float(amount_entry.get())

    if account_number in account_data:
        if pin == account_data[account_number]['pin']:
            account_data[account_number]['balance'] += amount
            balance = account_data[account_number]['balance']
            messagebox.showinfo('Success', f'Deposited: ${amount}\nNew balance: ${balance}')
        else:
            messagebox.showerror('Error', 'Incorrect PIN')
    else:
        messagebox.showerror('Error', 'Account not found')


root = tk.Tk()
root.title('ATM Machine')
root.geometry('400x400')
root.configure(bg='black')

account_label = tk.Label(root, text='Account Number:')
account_label.pack()

account_number_entry = tk.Entry(root)
account_number_entry.pack()

pin_label = tk.Label(root, text='PIN:')
pin_label.pack()

pin_entry = tk.Entry(root, show='*')
pin_entry.pack()

check_balance_button = tk.Button(root, text='Check Balance', command=check_balance)
check_balance_button.pack()

transaction_label = tk.Label(root, text='Transaction Amount:')
transaction_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

withdraw_button = tk.Button(root, text='Withdraw', command=withdraw)
withdraw_button.pack()

deposit_button = tk.Button(root, text='Deposit', command=deposit)
deposit_button.pack()

root.mainloop()
