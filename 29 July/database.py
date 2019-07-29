data_list = [
    {"id":1001,"wname":"Python","year":2019,"status":1,"company":"heraizen"},
    {"id":1002,"wname":"Web","year":2018,"status":1,"company":"Spaneos"}
    
]
try:
    with open ("ws.txt","w") as file:
        for d in data_list:
            line = f'{d["id"]},{d["wname"]},{d["year"]},{d["status"]},{d["company"]}\n'
            file.write(line)
except Exception as e:
    print(str(e))
