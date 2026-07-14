from MarvellousNum import ChkPrime
from Assignment18_1 import Add
def main():
    x=int(input("Enter number of elements: "))

    List=[]
    for i in range(x):
        y=int(input())
        List.append(y)

    ret=ChkPrime(List)

    Addition=Add(ret)
    print(f"{Addition}{ret}")
    


if __name__=="__main__":
    main()