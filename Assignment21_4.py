import threading

def Sum(List):
    sum = 0
    for no in List:
        sum=sum+no
    
    print("Summation of numbers:",sum)



def Prouct(List):
    sum = 1
    for no in List:
        sum=sum*no
    
    print(sum)

    print("Product is:",sum)

   
       
def main():
    no = int(input("Enter no of elements:"))

    print("Enter elements:")

    List = []

    for i in range(no):
        x = int(input())
        List.append(x)

    print(List)


    t1= threading.Thread(target= Sum,args= (List,))
    t2= threading.Thread(target= Prouct,args= (List,))
   

    t1.start()
    t2.start()

    t1.join()
    t2.join()
   


if __name__ =="__main__":
    main()