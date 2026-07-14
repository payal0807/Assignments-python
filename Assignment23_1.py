import multiprocessing
import os

def SumEven(no):
    print("Process id :",os.getpid())
    print("Input Number:",no)
    
    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i
    
    print("Sum of even numbers is:",sum) 

    return sum


    

def main():
    List = [100000,2000000,3000000,4000000]

    print("Input List is:",List)

    Result= []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumEven,List)

    pobj.close()
    pobj.join()

    print("Final results are:",Result)

  


if __name__ =="__main__":
    main()