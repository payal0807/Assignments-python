#Function without Parameters
#does not accept the input value

def demo():
    print("Welcome to Python")

demo() 


#Function with Parametrs

# which accept the input value through parameters

def Addition(Value1,Value2):
    Ans=Value1+Value2
    return Ans

def main():
    Ans=Addition(10,20)
    print(Ans)
if __name__=="__main__":
    main()    