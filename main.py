#from fastapi import FastAPI
# import uvicorn


# app = FastAPI(openapi_version="3.0.0")

# @app.get("/")
# def func():
#     return 'hello world'


# if __name__ == "__main__":
#   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

class BankAccount:
    def __init__(self, owner, balance):
        self.__balance = balance
        self.__owner = owner
        self.__history = []
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Сумма должна быть больше 0")
        self.__balance += amount
        self.__history.append(f"Пополнение на {amount} руб.")
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Сумма должна быть больше 0")
        if self.__balance < amount:
            raise ValueError("Недостаточно средств на счете")
        self.__balance -= amount
        self.__history.append(f"Снятие на {amount} руб.")
    @property
    def balance (self):
        return self.__balance
    
    @property
    def owner (self):
        return self.__owner
    
    def get_history (self):
        return self.__history.copy()

account = BankAccount("Дима", 1000)

account.deposit(500)
account.withdraw(200)

print(account.balance)       # 1300
print(account.owner)         # Дима
print(account.get_history()) 

# Попробуй сломать:
account.withdraw(5000)       # должна быть ошибка — денег не хватает
#account.deposit(-100)        # должна быть ошибка — сумма отрицательная
#print(account.balance)       
