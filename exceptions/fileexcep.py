try:
 
    word_count=0
    with open("data.txt")as f:
        lines =f.readlines()
        print(len(lines))
        for line in lines:
            
            print(line,end="")
           
            word_count+=len(line.split(" "))
        print(word_count)
except Exception as e:
    print(f"File not found plz chack path {e}")
