'''
Q3 - Dhana Laxmi Trading Company
Develop an application to keep track of share transaction of individual customer. At any time customer 
can’t have more than 5 company shares. Data need to be stored are share name (like ‘A’, ‘B’ etc) purchase 
price and number units bought. To purchase new share, if already 5 shares are present, oldest share is to 
be sold. While selling, current price of share has to be specified. Provide functions for purchasing share, 
selling share and make_estimation(). make_estimation() returns numeric value which is the difference 
between purchase and selling price of all shares in hand.
'''

class Share:
    def __init__(self,name) :
        self.price_now = 0
        self.name = name
        self.price_when_bought=0
        self.units = 0
        self.stock_name=('A','B','C','D','E','F','G','H')
        self.stock_price=(100,80,25,36,14,28,97,65)

        

    def buying(self,units=1):
        self.price_when_bought=self.price_now
        self.units=units
    
    def selling(self,units,price_now):
        if self.units==0:
            return print("No stocks present")
        if units>self.units:
            print("No of units u have is ", self.units," and not ", units)

        self.units = self.units-units

        return self.units*self.price_now
    
    def make_estimation(self,price_now):
        print("Current estimation of your stock is: ",self.price_now*self.unit - self.price_when_bought*self.units)


class customer:
    def __init__(self,money):

        # self.stock_name=('A','B','C','D','E','F','G','H')
        self.count=0

        self.stock_name=[]
        self.prices=[]
        self.units=[]
        self.money = money
    
    def display(self):
        for i in range(self.count):
            print("Stock Name: ",self.stock_name[i],"Stock units:",self.units[i],"stock price bought: ",self.prices[i])

        print("Current Amount in Hand: ", self.money)

    def buy(self,Stock_name,units,price):
        if price*units>self.money:
            print("You dont have that much money")
            return
        if Stock_name not in self.stock_name:
            if self.count==5:
                self.stock_name.pop(0)
                
                # self.units.pop(0)
                self.money=self.money+self.prices.pop(0)*self.units.pop(0)

                self.stock_name.append(Stock_name)
                self.units.append(units)
                self.prices.append(price)
                self.money=self.money-price*units
                print("stock inserted by removeing first inserted stock")
                
            if self.count<5:
                self.stock_name.append(Stock_name)
                self.units.append(units)
                self.prices.append(price)
                self.count+=1
                self.money=self.money-price*units
                print("stock inserted")
        else:
            name_index=self.stock_name.index(Stock_name)
            self.units[name_index]=self.units[name_index]+units
            self.money=self.money-price*units
            self.count+=1

    def sell(self,Stock_name,units,curr_price):
        if Stock_name in self.stock_name:
        
            to_deleate_index=self.stock_name.index(Stock_name)

            if units>self.units[to_deleate_index]: return print("units more than the size u have")
            self.units[to_deleate_index]=self.units[to_deleate_index]-units
            self.money=self.money+units*curr_price
        else:
            print("stock not present")
            return
        if self.units[to_deleate_index]==0:
            self.stock_name.pop(to_deleate_index)
            self.prices.pop(to_deleate_index)
            self.units.pop(to_deleate_index)
            self.count-=1

    def make_estimation(self,stock_name,price_now):
        index_stock=self.stock_name.index(stock_name)
        return price_now*self.units[index_stock]-self.prices[index_stock]*self.units[index_stock]
        


Jack = customer(1000)
Jack.buy("apple",5,100)
Jack.buy("google",3,60)
Jack.display()

Jack.buy("apple",5,100)
Jack.buy("google",3,60)
Jack.buy("Tata",1,32)
Jack.buy("tesla",2,40)
Jack.display()
Jack.buy("jocky",1,32)
Jack.buy("tesla",2,40)
Jack.buy("Tata",1,32)
Jack.buy("tesla",2,40)
Jack.buy("redbus",5,2)
Jack.display()
Jack.sell("Tata",1,32)
Jack.sell("tesla",2,40)
Jack.sell("redbus",5,2)
Jack.display()
Jack.sell("roja",1,1)
Jack.sell("king",2,2)
Jack.sell("son",5,3)
Jack.display()
Jack.buy("roja",1,1)
Jack.buy("king",2,2)
Jack.buy("son",5,3)
Jack.display()

Jack.display()

















    # A = Share('A')
    # A.price_now = 100
    # B = Share()
    # B.price_now = 90
    # C = Share()
    # C.price_now = 60
    # D = Share()
    # D.price_now = 20
    # E = Share()
    # E.price_now = 75
    # F = Share()
    # F.price_now = 10
    # G = Share()
    # G.price_now = 78
    # H = Share()
    # H.price_now = 50   
