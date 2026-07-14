from functools import reduce

ChkNo = lambda no: (no >= 70 and no<= 90)

Increment = lambda no : (no + 10)

Product = lambda no1 , no2  : no1 * no2


def main():
    x = int(input("Enter no of elements:"))

    List = []

    for i in range (x):
        y = int(input())

        List.append(y)
    
    print("Input List:",List)

    FData = list(filter(ChkNo,List))

    print("List After Filter:",FData)

    MData = list(map(Increment,FData))

    print("List After Map:",MData)

    RData = (reduce(Product,MData))

    print("Output of Reduce :",RData)



if __name__ == "__main__":
    main()