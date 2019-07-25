from contact import Contact
from beautifultable import BeautifulTable
class InMemoryImpl:
    contact_list = [] #class variable

    @classmethod
    def addContact(cls):
       name = input("Enter the name:")
       email = input("Enter the email:")
       mobile = input("Enter the mobile:")
       address = input("Enter the address:")
       cls.contact_list.append(Contact(name,email,mobile,address))
       print(f"Contact is addes successfully with name:{name}")

    @classmethod
    def deleteContact(cls):
        name = input("Enter the name:")
        con = cls.get_contact_by_name(name)
        if con:
            cls.contact_list.remove(con)
            print (f"Contact {name} deleted successfully....")
            InMemoryImpl._paint(cls.contact_list)
        else:
            print("data not found")
        

    @classmethod
    def viewContact(cls):
       InMemoryImpl._paint(cls.contact_list)

    @classmethod
    def search(cls):
        if len(cls.contact_list) > 0:
            name = input("Enter the name to search:")
            s_l = list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contact_list))
            if len(s_l) > 0:
                InMemoryImpl._paint(s_l)
            else:
                print("no data found")
        else:
            print("cbook is empty")


    @classmethod
    def updateContact(cls):
        name = input("Enter the name:")
        con = cls.get_contact_by_name(name)
        if con:
            print("1.Name 2.Email 3.Mobile 4.Address")
            ch = int(input("Enter choice"))
            if ch == 1:
                name = input("Enter the name:")
                print(f"Old name: {con.get__name()}")
                if name:
                    con.set__name(name)
            elif ch == 2:
                email = input("Enter the email:")
                print(f"Old email:{con.get__email()}")
                if email:
                    con.set__email(email)
            elif ch == 3:
                mobile = input("Enter the mob no:")
                print(f"Old no:{con.get__mobile()}")
                if mobile:
                    con.set__mobile(mobile)
            elif ch == 4:
                address = input("Enter the address:")
                print(f"Old address:{con.get__address()}")
                if address:
                    con.set__address(address)


    @staticmethod
    def _paint(lst):
        
        if len(lst) !=0:
            table = BeautifulTable()
            table.column_headers = ["Name","Email","Mobile","Address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"Contact Book is empty!...")
    @classmethod
    def get_contact_by_name(cls,name):
        if len(cls.contact_list) > 0:
            contact = list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contact_list))
            return contact[0] if contact else None
            


 
