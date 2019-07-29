import csv
class Stock:
    def __init__(self,name,symbol,exchange,price):
        self.name = name
        self.symbol = symbol
        self.exchange  = exchange
        self.price = price
    def __str__(self):
        return f"{self.name},{self.symbol},{self.exchange},{self.price}"

def clean_init_get_stocks():
    stock_lst= []
    
    try:
        with open("stock_price.csv") as f:
            data = csv.reader(f,delimiter=",")
            
            line =0
            for d in data:
                if line == 0:
                    line +=1
                    continue
                stock_lst.append(Stock(*d))
        
        for s in stock_lst:
            if "K" in s.price:
                s.price = float(s.price.strip().replace("K",""))*1000
            else:
                s.price = float(s.price)
            print(s)
    except Exception as e:
        print(' {} ,value {!r}'.format(e.args[0],e))
    return stock_lst


def show_stock_by_price(price):
    st_lst = clean_init_get_stocks()
    f = filter(lambda x: x.price <= price,st_lst)
    if f:
        show_stock_info(list(f)) 
    else:
        print("no stock found:")

'''def max_min_stock_price():
    st_lst = clean_init_get_stocks()'''

def show_stock_info(lst):
    for l in lst:
        print(l)

price =int(input("enter the price"))
show_stock_by_price(price)

