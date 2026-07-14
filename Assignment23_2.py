import multiprocessing
import os

def SumOdd(no):
    print("Process id :",os.getpid())
    print("Input Number:",no)
    
    sum = 0
    for i in range(1,no+1,2):
        sum = sum + i
    
    print("Sum of odd numbers is:",sum) 

    return sum


    

def main():
    List = [100000,2000000,3000000,4000000]

    print("Input List is:",List)

    Result= []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumOdd,List)

    pobj.close()
    pobj.join()

    print("Final results are:",Result)

  


if __name__ =="__main__":
    main()