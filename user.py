from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    f = open('./users.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(infos.values())
    f.close()