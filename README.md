## How to test
By default, there is no expense and 5 users stored in the app.

### Test instructions
- Start the app
- New expense
    - 50
    - Test
    - Select a user, [ENTER]
    - Unselect some users with [SPACE] ?, [ENTER]
- Show Status
- Select a line with ```"User" owes "Amount" to "User"```
- Show status (this line is now ```"User owes nothing"```)
- New user
    - Test
- Show status

> :warning: Forgot to update the user list at each new_expense() function call. Restart the app to have the new user in the list for choosing sender and involved users

## Todo-list

- [X] A new expense can be added (Mandatory expense information : Amount, label, Spender)
- [X] Expense registry is stored in an external file on an appropriate format for persistency (CSV is fine, any other relevant format would be cool)
- [X] A new user can be created (Mandatory user information : Name)
- [X] Users are stored in an external file for persistency
- [X] When adding a new expense, Spender should be chosen among existing users
- [X] An expense can be divided between several existing users. By default, total amount of the expense will be evenly split between all involved users and spender should automatically be checked as involved in the expense
- [X] New mandatory expense information : People involved in the expense

- [X] A status report can be accessed from the main menu, synthesizing who owes who. Every user must appear only once in the report, so you must synthesize reimbursements. 
Exemple: 3 Users :
- User1 owes 34,56€ to User2
- User2 owes nothing
- User3 owes 14,72€ to User2
- [X] Add the possibility to mark a debt as payed from the status report 
- [ ] Think of new ways of spliting the expense (Percentage / person, Amount / person, anything that makes sense)
- [X] User Input Validation : Throw an error if an expense amount is not a number, and so on ..
- [ ] All implemented features should have relevant test cases
    - If I just have to run your test suite to check project quality and features : Automatic bonus
- [ ] Bonus : Improve your app in any way you want : More features, fancy report, any good idea will be rewarded
