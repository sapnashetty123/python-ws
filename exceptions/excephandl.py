try:
    f=open("data.txt","w")
    data = "LINE 1 \r \n"
    f.write(data)
except Exception as e:
    print(f"{e}")
finally:                #to close the resources opened;even if except does not execute finally will
    f.close()


'''try:
    num= 100/0
    
except  ValueError as e:
    print("except block")
    print(f"{e}")
finally:                
    print("finally block")'''


try:
    num= 100/0
    
except  ZeroDivisionError as e:
    print("except block")
    print(f"{e}")
finally:                
    print("finally block")
    
