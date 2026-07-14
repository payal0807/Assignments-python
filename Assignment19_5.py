from functools import reduce

def PrimeNo(no):
    List = []
    for i in range(2,no):
        if no%i==0:
           break
    else:
        List.append(no)
    return List


def Mult(no):
    return no * 2

def Max (no1 ,no2):
    if no1 > no2:
        return no1
    else:
        return no2


def main():
    x = int(input("Enter no of elements:"))

    List = []

    for i in range (x):
        y = int(input())

        List.append(y)
    
    print("Input List:",List)

    FData = list(filter(PrimeNo,List))

    print("List After Filter:",FData)

    MData = list(map(Mult,FData))

    print("List After Map:",MData)

    RData = (reduce(Max,MData))

    print("Output of Reduce :",RData)



if __name__ == "__main__":
    main()