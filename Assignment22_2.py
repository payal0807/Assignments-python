import multiprocessing
import os


def Factorials(no):
    print("Process Id for running process:",os.getpid())
    sum = 1
    for i in range(1,no+1):
        sum = sum * i

    return sum


def main():
    List = [10,15,20,25]

    print(List)

    Result= []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorials,List)

    pobj.close()
    pobj.join()

    print("Factorial is:")

    print(Result)


if __name__ =="__main__":
    main()




