import threading

def ChkNonPrime(List):
    NonPrimeNo = []
    for no in List:
        for i in range(2,no):
            if (no%i==0):
                NonPrimeNo.append(no)
                break

         

        
    print(NonPrimeNo)


def ChkPrime(List):
    PrimeNo = []
    for no in List:
        for i in range(2,no):
            if (no%i==0):
                
                break

        else:
            
            PrimeNo.append(no)
        
    print(PrimeNo) 



def main():
    no = int(input("Enter no of elements:"))

    print("Enter elements:")

    List = []

    for i in range(no):
        x = int(input())
        List.append(x)

    print(List)


    Prime = threading.Thread(target= ChkPrime,args= (List,))
    NonPrime= threading.Thread(target= ChkNonPrime,args= (List,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()



if __name__ =="__main__":
    main()