num = int(input("Enter the no:"))
if (num %4 ==0 and num % 100 !=0)) or num % 400 ==0 :
    print(f"given year {num} is a leap year")
else:
    print(f"given year {num} is not a leap year")