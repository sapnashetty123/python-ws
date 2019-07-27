class  Stack:
    def __init__(self):
        self.st=[]

    def push(self,ele):
        #ele=int(input("Enter the ele to push:"))
        self.st.append(ele)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            ele=self.st.pop()
            print(f"Element {ele} is removed from the stack")

        
    def search(self,searchele):
        if self.is_empty():
            print("Stack is empty")
        else:
            for index,ele in enumerate(self.st):
                if ele == searchele:
                    return index
        
    def show(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.st)
    def is_empty(self):
        return len(self.st) ==0


if __name__ == "__main__":
    st=Stack()
    
    while True:

        print("1.Push 2. Pop 3. search 4.Shoe 5.exit")
        try:
            ch = int(input("Enter your choice:"))
            if ch ==1:
                ele=int(input("Enter the ele to push:"))
                st.push(ele)
            elif ch ==2:
                st.pop()
            elif ch==3:
                ele=int(input("Enter the ele to search:"))
                index=st.search(ele)
                print(f"{ele} found in position {index}")
            elif ch == 4:
                st.show()
            else:
                break
        except (ValueError, KeyError):
            print("Enter only no 1-5")














