# Create function that returns the name and balance of cash on an account in a list
# The output should be: "Igor", "203004099.2"

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:

#  - from account_number
#  - to account_number
#  - amount to transfer

# Print "404 - account not found" if any of the account numbers don't exist

# After printing the "accounts" it should look like:
# accounts = [
# [{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
# { 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204099571.23 },
# { 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1354100.0 }]

accounts = [{'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2},
            {'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23},
            {'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0}]


def get_name_and_balance(customer_list, acc_number):
    for customer in customer_list:
        if customer['account_number'] == acc_number:
            print('404 - account not found')
        if customer['account_number'] == acc_number:
            print(customer['client_name'], customer['balance'])


get_name_and_balance(accounts, 11234543)


def transfer_amount(acc_num1, acc_num2, amount):
    new = []
    for customer in accounts:
        new.append(customer['account_number'])
    if acc_num2 not in new or acc_num1 not in new:
        print('404 - account not found')
    else:
        for i in accounts:
            for k, v in i.items():
                if i['account_number'] == acc_num1:
                    i['balance'] -= amount
                    break
                if i['account_number'] == acc_num2:
                    i['balance'] += amount
                    break


transfer_amount(43546731, 23456311, 500.0)
print(accounts)
