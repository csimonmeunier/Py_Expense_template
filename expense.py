from PyInquirer import prompt
import csv
import json

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

def get_users_checked():
    users = []
    with open("./users.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            users.append({
                "name": row[0],
                "checked": True
            })
    return users

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_users()
    },
    {
        "type":"checkbox",
        "name":"involved",
        "message":"New Expense - Involved: ",
        "choices": get_users_checked(),
    },
]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    if infos["spender"] not in infos['involved']:
        infos['involved'].append(infos["spender"])
    spendings = {}
    for user in infos["involved"]:
        if (user == infos["spender"]):
            try:
                spendings[user] = int(infos["amount"])
            except:
                try:
                    spendings[user] = float(infos["amount"])
                except:
                    print("Invalid amount")
                    return False
        else:
            spendings[user] = 0
    file = open('./users_status.json', 'r+')
    users_expenses = json.load(file)
    users_expenses.append(spendings)
    file.seek(0)
    json.dump(users_expenses, file)
    file.truncate()
    file.close()
    f = open('./expense_report.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(infos.values())
    f.close()
    return True
