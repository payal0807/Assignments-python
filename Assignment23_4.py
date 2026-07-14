import multiprocessing
import os

def CountOddEven(no):
    print("Process id :",os.getpid())
    print("Input Number:",no)
    

    count = 0
    for i in range(1,no+1):
        if i % 2!=0:
       
         count = count + 1
    
    print("count  of odd  numbers is:",count) 

    return count


    

def main():
    List = [100000,2000000,3000000,4000000]

    print("Input List is:",List)

    Result= []

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountOddEven,List)

    pobj.close()
    pobj.join()

    print("Final results are:",Result)

  


if __name__ =="__main__":
    main()