def ChkMax(no):
    Arr = 0 

    for i in no:
        if (i>Arr):
            Arr = i
    return Arr
     

def main():
    x = int(input("Number of elements:"))

    Result = []

    print("Number Elements:")

    for i in range (x):
        y = int(input())
        Result.append(y)


    Ret = ChkMax(Result)
    print("Maximum is:",Ret)


   
if __name__ =="__main__":
    main()