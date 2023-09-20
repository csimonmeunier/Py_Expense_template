from collections import defaultdict
from PyInquirer import prompt
import json
import csv
import re

def get_users():
    users = []
    with open("./users.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            users.append({
                "name": row[0],
                "checked": False
            })
    return users

def calculate_balance(group_expenses):
    balance = {}
    for d in group_expenses:
        amount = 0
        sender = ""
        involved = []
        for name, paid,  in d.items():
            if (paid > 0):
                amount = paid
                sender = name
            else:
                involved.append(name)
        for name in involved:
            if (name not in balance):
                balance[name] = {}
            if (sender not in balance[name]):
                balance[name][sender] = 0
            balance[name][sender] += round((amount / (len(involved) + 1)), 2)
    return balance


def get_expenses():
    value = []
    file = open('./users_status.json', 'r')
    group_expenses = json.load(file)
    file.close()
    balance = calculate_balance(group_expenses)
    users = get_users()
    managed_users = {}
    for user, involved in balance.items():
        managed_users[user] = True
        edited = False
        for user_to, amount in involved.items():
            current_amount = amount
            for user_search, involved in balance.items():
                if (user_search == user_to):
                    for from_user, amount_to_give in involved.items():
                        if from_user == user:
                            current_amount -= amount_to_give
            if (current_amount > 0):
                value.append({
                    "name": f"{user} owes {str(current_amount).replace('.', ',')}€ to {user_to}"
                })
                edited = True
        if (not edited):
            value.append({
                "name": f"{user} owes nothing"
            })
    for user in users:
        if (user['name'] not in managed_users):
            value.append({
                "name": f"{user['name']} owes nothing"
            })
        
    return value

def status():
    expense_questions = [
        {
            "type": "list",
            "name": "payed",
            "message": "Select debts to pay:",
            "choices": get_expenses()
        }
    ]
    infos = prompt(expense_questions)
    result = re.search("^([a-zA-Z\ ]+)\ owes\ ([0-9,]*)€ to\ ([a-zA-Z\ ]+)$", infos["payed"])
    if (result == None):
        return
    expense = {
        result.group(1): float(result.group(2).replace(',', '.')) * 2,
        result.group(3): 0
    }
    file = open('./users_status.json', 'r+')
    users_expenses = json.load(file)
    users_expenses.append(expense)
    file.seek(0)
    json.dump(users_expenses, file)
    file.truncate()
    file.close()
