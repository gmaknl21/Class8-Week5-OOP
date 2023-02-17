import random
class Client:
    bonus = 300
    interest_rate = 1.05
    num_client = 0
    total_balance = 0

    def __init__(self, name, surname, balance, children_number=0, gender='uncertain'):
        self.name = name
        self.surname = surname
        self.balance = balance
        self.email = f'{name.lower()}.{surname}@gmail.com'
        self.gender = gender
        self.account_number = (f"ABN{random.randint(1000000000,9999999999)}")
        self.children_number = children_number
        Client.num_client += 1
        Client.total_balance += balance

        if children_number > 0:
            self.add_child_bonus()

    def add_deposit(self, amount):
        self.balance += amount
        Client.total_balance += amount
        return (f'Your balance is updated , {self.balance}')

    def withdraw_deposit(self, amount):
        self.balance -= amount
        Client.total_balance -= amount
        return(f"Your balance is updated,  {self.balance}")

    def payment_rent(self):
        self.balance -= self.rent
        return(f'Your rent is paid , {self.balance}')

    def send_money(self, receiver_account_number, amount):
        if self.balance < amount:
            return 'balance is not enough'
        else:
            client_object = [obj for obj in globals().values() if isinstance(
                obj, Client) and obj.account_number == receiver_account_number]
            if len(client_object) == 0:
                print('client not found')
            else:
                reciever_object = client_object[0]
                reciever_object.balance += amount
                self.balance -= amount

    def add_child_bonus(self):
        self.add_deposit(self.children_number * Client.bonus)

    def add_interest(self):
        self.balance *= Client.interest_rate

    @classmethod
    def average_balacance(cls):
        if cls.num_client == 0:
            return 0
        else:
            return cls.total_balance / cls.num_client
class Premium_Client(Client):
    def __init__(self, name, surname, balance, loyalty_point, children_number=0, gender='uncertain'):
        super().__init__(name, surname, balance, children_number, gender)
        self.loyalty_point = loyalty_point
    def add_deposit(self, amount):
        super().add_deposit(amount)
        loyalty_point_earned = amount / 2
        self.loyalty_point += loyalty_point_earned
        if self.loyalty_point >= 1000:
            vip_level = 'gold' if self.loyalty_point >= 500 else 'silver' if self.loyalty_point >= 200 else 'bronze'
            vip_client = VipClient(self.name, self.surname, self.balance, self.loyalty_point, vip_level)
            del self.__dict__
            return vip_client
        if self.loyalty_point > 1000:
            self.balance += 50
            self.loyalty_point -= 50
            return f"Congratulations! You've earned {loyalty_point_earned} loyalty points and received a bonus of {amount}. New balance: {self.balance}"
    def __del__(self):
        self.name = None
        self.surname = None
        self.balance = None
        self.gender = None
        self.account_number = None
        self.children_number = None
        self.loyalty_point = None
class VipClient(Premium_Client):
    def __init__(self, name, surname, balance, loyalty_point, vip_level):
        super().__init__(name, surname, balance, loyalty_point)
        self.vip_level = vip_level
    def add_deposit(self, amount):
        if self.vip_level == 'gold':
            amount *= 1.03
        elif self.vip_level == 'silver':
            amount *= 1.02
        elif self.vip_level == 'bronze':
            amount *= 1.01
        super().add_deposit(amount)
        return f"Amount after VIP bonus: {amount}"
    def send_money(self, receiver_account_number, amount):
        client_object = [obj for obj in globals().values() if isinstance(
            obj, Client) and obj.account_number == receiver_account_number]
        if len(client_object) == 0:
            return 'Receiver client not found'
        else:
            receiver_object = client_object[0]
            super().send_money(receiver_account_number, amount)
            return f"Money sent to {receiver_object.name} {receiver_object.surname}"
pclt1 = Premium_Client('Danial', 'Melmav', 15000, 0)
pclt2 = Premium_Client('Girmay', 'Araya', 40000000, 0)
# Deposits to pclt1 and pclt2
pclt1.add_deposit(100)
pclt2.add_deposit(200)
# Output after Deposits  Balance 
print('Current balance :', pclt1.balance)
print('Current balance :', pclt2.balance)
# pclt1 is sending 5000 to pclt2 whose account number is pclt2.account_number.
pclt1.send_money(pclt2.account_number, 5)
print(f"Blance Account Number:{pclt2.account_number}:", pclt2.balance)
# loyalty_point
print(f"Loyalty Point {pclt1.account_number} :", pclt1.loyalty_point)
print(f"Loyalty Point {pclt2.account_number} :", pclt2.loyalty_point)





