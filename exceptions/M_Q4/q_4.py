try:
    c=0
    dit={}
    word_count=0
    with open("story.txt")as f:
        lines =f.readlines()
        print(f"no of lines:{len(lines)}")
        for line in lines:
            word_count+=len(line.split(" "))
            for word in line.upper().strip("\n").strip(".").split(" "):
                if  word in dit:
                    dit[word]+=1
                else:
                    dit[word]=1
        print(dit,end="\n")
        for k,v in dit.items():
            if v == max(dit.values()):
                print(f"max occured word and its value:{k} : {v}")

        print(f"word count:{word_count}")
        for key in dit.keys():
            if key.lower() in ['and','but','if']:
                c+=1
    print(f"conjunction count:{c}")
except Exception as e:
    print(f"File not found plz chack path {e}")
