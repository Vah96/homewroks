#
# 1. Եկեք ստեղծենք հաճախորդի բանկային հաշվի կլաս.
#     - ունի 4 instance attribute-ներ՝ id, name, balance, currency, որոնք read-only են (հնարավոր չլինի ուղիղ ձևով փոխել)
#     - որպես class attribute տարբեր դրամային արժույթների համար ունենալ փոխանակման գործակիցներ
#     - ունի երեք մեթոդներ, credit, debit և transferTo
#     - credit - ավելացնել բալանսը տրված չափով
#     - debit - եթե հաշվի վրա բավարար գումար կա, նվազեցնել հաշվի գումարը տրված չափով
#     - transferTo - տրված չափով գումարը փոխանցել մեկ այլ բանկային հաշվի, հավի առնել currency-ն
#     - սահմանել __str__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա հաշվի մնացորդը դոլարով


class ReadOnlyProperty(Exception):

    def __init__(self, message="it is read only property"):
        self.message = message

    def __str__(self):
        return self.message


class Account:

    currencies = {"AMD": 480, "EUR": 0.9, "RUB": 105}
    ids = []

    def __init__(self, id, name, balance, currency):
        if currency != "USD" and currency not in self.currencies.keys():
            raise ValueError(f"Wrong currency: '{currency}'")
        if id in self.ids:
            raise ValueError(f"Duplicate ID: '{id}'. Use another ...")
        else:
            self.ids.append(id)
        self.__id = id
        self.__name = name
        self.__balance = balance
        self.__currency = currency

    def __str__(self):
        if self.currency != "USD":
            balance = round(self.balance / self.currencies[self.currency], 2)
        else:
            balance = self.balance
        return f"Your balance is {balance}$(USD)"

    def __int__(self):
        if self.currency != "USD":
            balance = round(self.balance / self.currencies[self.currency], 2)
        else:
            balance = self.balance
        return int(balance)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, val):
        raise ReadOnlyProperty

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        raise ReadOnlyProperty

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, val):
        raise ReadOnlyProperty

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, val):
        raise ReadOnlyProperty

    def credit(self, val):
        self.__balance += val

    def debit(self, val, validate=True):
        if validate and self.check_enough_balance(val) is False:
            raise ValueError("The amount in the account is not enough to complete the 'debit' functionality")
        else:
            self.__balance -= val

    def transfer_to(self, other_account, val, validate=True):
        if validate and self.check_enough_balance(val) is False:
            raise ValueError("The amount in the account is not enough to complete the 'transfer_to' functionalityy")
        else:
            self.__balance -= val
        if self.__currency == other_account.__currency:
            balance = val
        elif other_account.__currency == "USD":
            balance = val / self.currencies[self.__currency]
        elif self.__currency == "USD":
            balance = val * self.currencies[other_account.__currency]
        else:
            self_val_usd = val / self.currencies[self.__currency]
            balance = self_val_usd * self.currencies[other_account.__currency]

        other_account.__balance += balance

    def check_enough_balance(self, val):
        return self.__balance >= val


account1 = Account(1, "User1", 5, "USD")
account2 = Account(2, "User2", 4800, "AMD")
# account1.credit(1000)
# account1.debit(3000)
# print(account1)
# print(account2)
# account2.transfer_to(account1, 1200)
account1.transfer_to(account2, 3)
# print(account1)
# print(account2)


# 2. Օգտագործելով Account կլասը, ստեղծել SavingsAccount(ավանդային հաշիվ) և CurrentAccount(ընթացիկ հաշիվ) կլասներ։
#     - ավանդային հաշիվը բանկային հաշվի ատրիբուտներից բացի պետք է ունենա նաև interest(տոկոսադրույք) և մեթոդ որով
#     կավելանա հաճախորդի հաշիվը տոկոսադրույքի չափով։
#     - ընթացիկ հաշիվը բանկային հաշվի ատրիբուտներից բացի պետք է ունենա overdraft limit ատրիբուտ
#     - ընթացիկ հաշվի բալասը կարող է մինուս արժեքներ ընդունել overdraft limit-ի չափով
#     - կարիքի դեպքում սուպերկլասի մեթոդները կարող են override արվել
#     - սահմանել հաշիվների իրար գումարումը, եթե նրանք նույն տիպի են


class SavingsAccount(Account):

    def __init__(self, id, name, balance, currency, interest=10):
        super().__init__(id, name, balance, currency)
        self.interest = interest

    def __add__(self, second_account):
        if not isinstance(second_account, SavingsAccount):
            raise TypeError("Type error...")
        if self.currency == second_account.currency:
            balance = self.balance + second_account.balance
        elif second_account.currency == "USD":
            balance = second_account.balance + self.balance / self.currencies[self.currency]
        elif self.currency == "USD":
            balance = self.balance + second_account.balance / self.currencies[second_account.currency]
        else:
            self_val_usd = self.balance / self.currencies[self.currency]
            second_account_val_usd = second_account.balance / self.currencies[second_account.currency]
            balance = self_val_usd + second_account_val_usd

        return f"Balance: {balance}$(USD)"

    def work_interest(self):
        interest_value = self.balance * self.interest / 100
        self.credit(interest_value)


savingsAccount1 = SavingsAccount(20, "User1", 100, "USD")
savingsAccount2 = SavingsAccount(21, "User1", 2400, "AMD")
savingsAccount3 = SavingsAccount(22, "User1", 1050, "RUB")
# print(savingsAccount1)
# print(savingsAccount2)
# savingsAccount2.transfer_to(savingsAccount1, 1920)
# print(savingsAccount1)
# print(savingsAccount2)
# print(savingsAccount1 + savingsAccount2)
# print(savingsAccount2 + savingsAccount1)


class CurrentAccount(Account):

    def __init__(self, id, name, balance, currency, overdraft_limit):
        super().__init__(id, name, balance, currency)
        self.overdraft_limit = overdraft_limit

    def __int__(self):
        balance = self.balance + self.overdraft_limit
        if self.currency != "USD":
            balance = round(balance / self.currencies[self.currency], 2)
        return int(balance)

    def debit(self, val):
        if self.balance + self.overdraft_limit >= val:
            super().debit(val, False)
        else:
            raise ValueError("The amount in the account is not enough to complete the 'debit' functionality")

    def transfer_to(self, other_account, val):
        if self.balance + self.overdraft_limit >= val:
            super().transfer_to(other_account, val, False)
        else:
            raise ValueError("The amount in the account is not enough to complete the 'debit' functionality")


currentAccount1 = CurrentAccount(40, "User1", 15, "USD", 10)
currentAccount2 = CurrentAccount(41, "User1", 7200, "AMD", 2400)
currentAccount3 = CurrentAccount(42, "User1", 1575, "RUB", 525)

# currentAccount2.transfer_to(currentAccount1, 9120)
# print(currentAccount1)
# currentAccount1.debit(12)
# currentAccount1.debit(10)
# print(currentAccount1)


# 3. Ստեղծել Person կլաս, որը կունենա երկու instance attribute՝ name և ssn(հանրային ծառայությունների համարանիշ) int տիպի
#     - սահմանել __str__ մեթոդը։ Այս մեթոդը մեզ ցույց կտա մարդու անունը
#     - սահմանել __hash__ մեթոդը։ Այս մեթոդը պետք է վերադարձնի մարդու հանրային ծառայությունների համարանիշը


class Person:

    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __str__(self):
        return f"Person name: {self.name}"

    def __hash__(self):
        return self.ssn


person1 = Person("Person1", 1234512345)
person2 = Person("Person2", 3456734567)
person3 = Person("Person3", 5678956789)


# 4. Ստեղծել Bank կլաս, որի instance-ը իր մեջ կարող է պարունակել տարբեր տիպի բանկային հաշիվներ և որոնք կապված են որոշակի
#     անձանց հետ։ Մեկ անձը կարող է ունենալ մեկից ավելի հաշիվներ։
#     - հաշիվների ցուցակը կարող ենք պահել dictionary-ի մեջ
#     - բանկը պետք է ունենա մեթոդներ փոփոխելու համար հաշիվների բալանսը, օգտագործելով բանկային հաշիվների մեթոդները
#     - եթե հաշիվը overdraft-ում է, բանկը կարող է նամակ գրել հաշվին հապակցված անձին։
#     - բանկը պետք է հնարավորություն ունենա ssn-ի միջոցով ստուգել անձի բոլոր հաշիվների ընդհանուր գումարը՝
#     դոլարային արժույթով


class Bank:

    __accounts: object

    def __init__(self, accounts):
        self.__accounts = accounts

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, val):
        raise ReadOnlyProperty

    def credit(self, ssn, account_type, val):
        if ssn not in self.accounts.keys():
            raise ValueError("ssn not found ...")
        if account_type not in self.accounts[ssn].keys():
            raise ValueError(f"{account_type} not found ...")
        self.accounts[ssn][account_type].credit(val)

    def debit(self, ssn, account_type, val):
        if ssn not in self.accounts.keys():
            raise ValueError("ssn not found ...")
        if account_type not in self.accounts[ssn].keys():
            raise ValueError(f"{account_type} not found ...")
        self.accounts[ssn][account_type].debit(val)

    def transfer_to(self, from_ssn, to_ssn, account_type, val):
        self.accounts[from_ssn][account_type].transfer_to(self.accounts[to_ssn][account_type], val)

    def get_full_balance(self, ssn):
        return f"Full balance: {int(self.accounts[ssn]['current']) + int(self.accounts[ssn]['savings'])}$(USD)"


lst = {
    hash(person1): {"savings": savingsAccount1, "current": currentAccount1},
    hash(person2): {"savings": savingsAccount2, "current":  currentAccount2},
    hash(person3): {"savings": savingsAccount3, "current":  currentAccount3}
}
bank = Bank(lst)

# check Credit functionality
# print('\ncheck Credit functionality')
#
# print(bank.accounts[hash(person1)]['savings'])
# print(bank.accounts[hash(person1)]['current'])
# bank.credit(hash(person1), 'savings', 50)
# bank.credit(hash(person1), 'current', 20)
# print(bank.accounts[hash(person1)]['savings'])
# print(bank.accounts[hash(person1)]['current'])
#
# # check Debit functionality
# print('\ncheck Debit functionality')
#
# print(bank.accounts[hash(person2)]['savings'])
# print(bank.accounts[hash(person2)]['current'])
# bank.debit(hash(person2), 'savings', 50)
# bank.debit(hash(person2), 'current', 20)
# print(bank.accounts[hash(person2)]['savings'])
# print(bank.accounts[hash(person2)]['current'])
#
# # check Transfer_to functionality
# print('\ncheck Transfer_to functionality for current account')
#
print(bank.accounts[hash(person1)]['current'])
print(bank.accounts[hash(person2)]['current'])
currentAccount2.transfer_to(currentAccount1, 9120)
print(bank.accounts[hash(person1)]['current'])
print(bank.accounts[hash(person2)]['current'])
#
# print('\ncheck Transfer_to functionality for savings account')
#
print(bank.accounts[hash(person1)]['savings'])
print(bank.accounts[hash(person2)]['savings'])
bank.transfer_to(hash(person1), hash(person2), 'savings', 50)
print(bank.accounts[hash(person1)]['savings'])
print(bank.accounts[hash(person2)]['savings'])

print(bank.get_full_balance(hash(person1)))



