def Factorial(value):
    sum = 1
    for i in range (1,value+1):
        sum = sum * i
    
    return sum 



def main():
    no = int(input("Enter one number:"))

    Ret = Factorial(no)

    print(Ret)


if __name__ =="__main__":
    main()