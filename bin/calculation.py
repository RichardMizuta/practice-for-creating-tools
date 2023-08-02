import math
price = int(input("enter stock price"))
net = int(input("enter net profit"))
shares = int(input("enter number of shares"))

class PER:
    def __init__(self, name, price, net,shares):
        self.name = name
    def calc(self, price, net, shares):
        esp = net / shares
        per = math.floor(price /esp) 
        print(per)

instance = PER("innitial",price,net,shares)
instance.calc(price,net,shares) 