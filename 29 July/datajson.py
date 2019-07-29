import json
data_list = [
    {"id":1001,"wname":"Python","year":2019,"status":1,"company":"heraizen"},
    {"id":1002,"wname":"Web","year":2018,"status":1,"company":"Spaneos"}
    
]
try:
    with open ("ws.json","w",newline='') as file:
        json.dump(data_list,file,indent=4)
except Exception as e:
    print(str(e))