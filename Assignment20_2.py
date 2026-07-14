import threading


def SumEvenFactor(no):
    List = []
    Result = []
    for i in range (1,no+1):
        if no % i == 0:
            Result.append(i)
  

    for no in Result:
        if no %2==0:
            List.append(no)
    
    sum = 0
    for no in List:
        sum = sum + no
    print (sum)
       




def SumOddFactor(no):
    List = []
    Result = []
    for i in range (1,no+1):
        if no % i == 0:
            Result.append(i)
  

    for no in Result:
        if no %2!=0:
            List.append(no)
    
    sum = 0
    for no in List:
        sum = sum + no
    print (sum)





def main():
    

    t1 = threading.Thread(target=SumEvenFactor ,args = (10,) )

    t2 = threading.Thread(target=SumOddFactor, args =(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main thread")

    


if __name__ =="__main__":
    main()


