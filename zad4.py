class BankAccount:
    def __init__(self):
        self._balance = 0
        self._transactions = []

    def deposit(self, money):
        if money > 0:
            self._balance += money
            self._transactions.append(f"Пополнение: +{money}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, money):
        if 0 < money <= self._balance:
            self._balance -= money
            self._transactions.append(f"Снятие: -{money}")
        else:
            print("Недостаточно средств или неверная сумма.")

    @property
    def balance(self):
        return self._balance

    def show_transactions(self):
        print("История транзакций:")
        for b in self._transactions:
            print(b)


if __name__ == "__main__":

    account = BankAccount()


    print(f"Начальный баланс: {account.balance} руб.")


    print("\nПополнение на 1500 руб.")
    account.deposit(1500)
    print(f"Текущий баланс: {account.balance} руб.")


    print("\nПопытка пополнения на -200 руб.")
    account.deposit(-200)


    print("\nСнятие 700 руб.")
    account.withdraw(700)
    print(f"Текущий баланс: {account.balance} руб.")


    print("\nПопытка снятия 1000 руб.")
    account.withdraw(1000)


    print("\nПопытка снятия -500 руб.")
    account.withdraw(-500)


    print("\nИтоговая информация:")
    print(f"Текущий баланс: {account.balance} руб.")
    account.show_transactions()