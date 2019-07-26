inp = input("entr the sen:")
for ch in inp:
    if ch in  ['a','e','i','o','u']:
        inp=inp.replace(ch," ")

print(inp)