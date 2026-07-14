import multiprocessing


def SumSquare(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + ( i ** 2)

    return sum


def main():
    List = [1000000,2000000,3000000,4000000,5000000]

    Result= []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare,List)

    pobj.close()
    pobj.join()

    print("Result is:")

    print(Result)


if __name__ =="__main__":
    main()

