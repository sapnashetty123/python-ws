class Employee:

    def __init__(self,empno,name,qual,salary,d_name):
        self.empno = empno
        self.name = name
        self.qual = qual
        self.salary = salary
        self.d_name = d_name

    def show_info(self):
        print(f"{self.empno}-{self.name}-{self.qual}-{self.salary}-{self.d_name}")

    def incre_salary(self,inc_amt):
        self.salary += inc_amt
        print(f"{self.name}-salary after increment:{self.salary}")