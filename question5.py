# Print example


def First():
    print("Welcome to marvellous")

def main():
    First()

if __name__ =="__main__":
    main()

#Here only print statement will print because there is no return statement in First()
#print statement will only display on console but no return value

#Return Statement

def Demo(a,b):
    Ans= a+b
    return 21

def main():
    Ret = Demo(10,20)
    print(Ret)

if __name__ =="__main__":
    main()


#Here return statement is used in fnction Demo() ,thats why when function is being call it will return 21 value 
#return sends value back to caller
#if a function does not use return ,it will return None by default 


