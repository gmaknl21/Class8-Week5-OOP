# Class8-Week5-OOP

### 1) Create Vip class which inheritances from Client.
  * you will have 3 vip level in VIP class . gold ,silver,bronz.
  * if you are vip client , when you add_deposit for gold  0.03 silver 0.02 and bronz 0.01 get more money each transaction.
  * You can not create VIP client like vclient=VipClient('omer','uygur','1000') etc.Vip client requirement this :
  * if premium client collect more than 1000 loyalty point in total then that client will be Vip Client. (hint : You will create vip client inside of premiumclient method using premium client attributes.)
  * One you create Vip client using premium client attributes you can use this function for clean premium client object or attributes :
```
def _del_(self):
        self.name = None
        self.surname = None
        self.balance = None
        self.gender = None
        self.account_number = None
        self.children_number = None
        self.loyalty_point = None
```
* Lastly you should able to send money from vip client to normal client(VIP client and premium client are still part of client class)

### 2) Create roughly UML diagram and Use case for our classes.Doesnt have to follow all rules . It will just give to you an idea.
