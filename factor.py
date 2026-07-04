def Factorial(value):

    result= []
    for i in range (1,value+1):
        if (value%i==0):
        
            result.append(i)
    
    return result


def main():
    no = int(input("Enter number:"))

    Ret = Factorial(no)
    
    print("Factors are:",Ret)



if __name__=="__main__":
    main()