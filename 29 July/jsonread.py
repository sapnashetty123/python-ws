import json
try:
    with open ("ws.json","r") as file:
        ws_lst = json.load(file)
        for w in ws_lst:
            print(f"Id:{w['id']} Name:{w['wname']} Year:{w['year']} Status:{w['status']} Company:{w['company']}")
except Exception as e:
    print(str(e))