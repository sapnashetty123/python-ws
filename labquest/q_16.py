inp=input("enter the statement:")
lst=["does","do","is","are"]
for word in lst:
    if inp.startswith(word) and inp.endswith("?"):
        print("interrogative")
        break
else:
    print("not")