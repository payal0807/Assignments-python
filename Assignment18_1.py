def Add(no):
         
    sum = 0
    for i in no:
        sum = sum + i
    return sum



def main():
    x = int(input("Number of elements:"))

    Result = []

    print("Number Elements:")

    for i in range (x):
        y = int(input())
        Result.append(y)


    Ret = Add(Result)
    print("Addition is:",Ret)


   

if __name__ =="__main__":
    main()