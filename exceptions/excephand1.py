def cast_vote(age):
    assert age >=18, f"Age shoudn't be lass than 18,it is {age}"
    print("Thank u for voting")

try:
    age = int(input("Enter the age:"))
    cast_vote(age)
except AssertionError as a:
    print(a)
else:
    print("you have entered valid age")
finally:
    print("End")