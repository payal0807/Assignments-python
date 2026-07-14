import multiprocessing
import os

def Factorials(no):
    print("Process id :",os.getpid())
    print("Input Number:",no)
    

    sum = 1
    for i in range(1,no+1):
        sum  = sum * i
       
        
    
    print("Factorial is:",sum) 

    return sum


    

def main():
    List = [10,15,20,25]

    print("Input List is:",List)

    Result= []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorials,List)

    pobj.close()
    pobj.join()

    print("Final results are:",Result)

  


if __name__ =="__main__":
    main()