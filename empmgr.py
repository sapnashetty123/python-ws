from employee import Employee
'''emp1=Employee(1,"sunny"," M.Tech ", 56000," CS")
emp2=Employee(2,"bunny"," M.Tech ",56000," IS")
emp1.show_info()
emp1.incre_salary(2000)
emp1.show_info()        #since emp salary is instant variable only specified emp salary is changed if class variable all salary will be changed
emp2.show_info()'''

lst_emp=[]

def load_emp():
    with open("emp.txt") as f:
        fdata=f.readlines()
        for data in fdata:
            edata=data.strip("\n").split(",")
            empno=int(edata[0])
            name=edata[1]
            qual=edata[2]
            salary=int(edata[3])
            d_name=edata[4]
            emp=Employee(empno,name,qual,salary,d_name)
            lst_emp.append(emp)
    print(f"total emp count: {len(lst_emp)}")

def showDep():
    dname=set(map(lambda emp:emp.d_name,lst_emp))
    for name in dname:
        print(name)

def showAllQual():
    quals=set(map(lambda emp:emp.qual,lst_emp))
    for qual in  quals:
        print(qual)

def maxSalEmp():
    sal=list(map(lambda x:x.salary,lst_emp))
    max1=max(sal)
    nameemp=list(filter(lambda x:x.salary == max1,lst_emp ))
    for name in nameemp:
         name.show_info()

def showEmpCountByDeptName():
    dname=set(map(lambda emp:emp.d_name,lst_emp))
    for name in dname:
        

def showTotalSalByDeptName():
    pass

def showEmpCountByQual():
    pass

load_emp()
showDep()
showAllQual()
maxSalEmp()