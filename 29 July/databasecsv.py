import csv
data_list = [
    {"id":1001,"wname":"Python","year":2019,"status":1,"company":"heraizen"},
    {"id":1002,"wname":"Web","year":2018,"status":1,"company":"Spaneos"}
    
]
try:
    with open ("ws.csv","w",newline='') as file:
        heading = ["id","wname","year","status","company"]
        obj = csv.DictWriter(file,fieldnames=heading)
        obj.writeheader()
        obj.writerows(data_list)
except Exception as e:
    print(str(e))