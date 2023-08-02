import math
price = int(input("enter stock price"))
net = int(input("enter net asseets"))
shares = int(input("enter number of shares"))

class PBR:
    def __init__(self, name, price, net,shares):
        self.name = name
    def calc(self, price, net, shares):
        bps = net / shares
        pbr = math.floor( price / bps) 
        print(pbr)

instance = PBR("innitial",price,net,shares)
instance.calc(price,net,shares) 