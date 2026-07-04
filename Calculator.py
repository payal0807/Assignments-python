def Addition (no1,no2):
    ans= no1+no2
    return ans 

def Substraction (no1,no2):
    ans= no1-no2
    return ans

def Multiplication (no1,no2):
    ans = no1*no2
    return ans

def Divsion (no1,no2):
    ans = no1/no2
    return ans

def main():
    no1 = int(input("Enter first number:"))

    no2  = int(input("Enter second number:"))

    Ret1 = Addition(no1,no2)
    print("Addition is:",Ret1)

    Ret2 = Substraction(no1,no2)
    print("Substraction is:",Ret2)

    Ret3 = Multiplication (no1,no2)
    print("Multiplication is:",Ret3)  

    Ret4 = Divsion (no1,no2)
    print("Divsion is:",int(Ret4))
    



if __name__=="__main__":
    main()