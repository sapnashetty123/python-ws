from openpyxl import Workbook
wb = Workbook()
sheet = wb.active
data = [
    ('id','wname','year','status','company'),
    (1001,"Python",2019,1,"heraizen"),
    (1002,"Web",2018,1,"Spaneos")
]
for row in data:
    sheet.append(row)
wb.save("ws.xlsx")