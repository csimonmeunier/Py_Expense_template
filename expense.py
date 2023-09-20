from PyInquirer import prompt
import csv

users = []

with open("./users.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    users.append(row[0])

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
        "choices": users
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    # Write in a CSV the content of the expense
    # The infos looks like that: {'amount': '30', 'label': 'Salut', 'spender': 'Coucou'}
    f = open('./expense_report.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(infos.values())
    f.close()
    return True
