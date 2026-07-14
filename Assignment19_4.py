from functools import reduce

EvenNo = lambda no: ( no %2 == 0)

Square = lambda no : (no * no )

Add = lambda no1 , no2  : no1 + no2


def main():
    x = int(input("Enter no of elements:"))

    List = []

    for i in range (x):
        y = int(input())

        List.append(y)
    
    print("Input List:",List)

    FData = list(filter(EvenNo,List))

    print("List After Filter:",FData)

    MData = list(map(Square,FData))

    print("List After Map:",MData)

    RData = (reduce(Add,MData))

    print("Output of Reduce :",RData)



if __name__ == "__main__":
    main()