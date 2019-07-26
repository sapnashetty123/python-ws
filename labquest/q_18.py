prod={}
while True:
    def show(prod):
        if len(prod)!= 0:
            for key,val in prod.items():
                print(f"{key}:{val}")
        else:
            print("no element")

    def add(prod):
        prod_id=int(input("Enter the id"))
        prod_name=input("Enter the product name:")
        prod[prod_id]=prod_name

    def search(prod):
        prod_id=int(input("Enter the id to search"))
        if prod.get(prod_id):
            print("{prod_id}:{prod_name}")
        else:
            print("not found")



#add(prod)
show(prod)
