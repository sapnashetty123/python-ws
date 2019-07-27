class MaxLimitError(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return f"{self.__class__.__name__} : {self.message}"

c=0
def login(username,password):
    global c
    if username == "abc" and password == "cvb":
        print("Login is success")
    else:
        print("bad credentials")
    c+=1
    if c>2:
        raise MaxLimitError("you have reached the max limit")

login("ABS","hfg")
login("ABS","hfg")
login("ABS","hfg")
login("ABS","hfg")