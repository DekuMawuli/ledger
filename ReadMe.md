# LEDGER API
## Auth & Registration routes
* localhost:port/users/login/ - Data must be in json
`{"username": "", "password": ""}`

* To Set Authorization header, use **Bearer** instead of Token

* localhost:port/users/register/ - Data must be in json 
fields needed => **['first_name', 'last_name', 'username', 'email', 'password']**


## Accounts
Route ------------ VERB ----------- RESULT
* `/api/accounts/` - **GET** - Get User Accounts
* `/api/accounts/` - **POST** - Add Account
* `/api/accounts/<int:pk>/` - **GET/PUT/DELETE** - Read/Update/Delete
* `/api/accounts/<int:pk>/balance/` - **GET** - Get An Account's Balance
* `/api/accounts/balance/` - **GET** - Get Total Balance of User Accounts
* `/api/accounts/transaction/` - **GET** - Shows All Transactions Done on the account (Credit/Debit)
* `/api/accounts/transaction/` - **POST** - Debit or Credit User Account

## Internal Transfers
This routes caters for transfers from one account to another in a user's accounts
* `/api/internal-transfer/` - **GET** - Gets all internal transactions done on a user's account
* `/api/internal-transfer/` - **POST** - Transfer money to from account A to account B of user
* `/api/internal-transfer/<int:pk>/` - **GET/DELETE** - Read/Delete an Internal Transaction


## External Transfers
This routes caters for transfers from one account  of a user to an account of another user
* `/api/external-transfer/` - **GET** - Gets all external transactions done on a user's account
* `/api/external-transfer/` - **POST** - Transfer money to from account A to account B of user
* `/api/external-transfer/<int:pk>/` - **GET/DELETE** - Read/Delete an Internal Transaction


### Thank you (Mawuli Kofivi)