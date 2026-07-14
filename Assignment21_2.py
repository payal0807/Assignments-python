import threading

def Max(List):
    sum = 0
    for no in List:
        if sum < no:
            sum = no
    print("Max no is:",sum)


def Min(List):
    sum = List [0]
    
    for no in List:
        if sum > no:
            sum=no
    print("Min no is:",sum)
            
   
       
def main():
    no = int(input("Enter no of elements:"))

    print("Enter elements:")

    List = []

    for i in range(no):
        x = int(input())
        List.append(x)

    print(List)


    Maximum= threading.Thread(target= Max,args= (List,))
    Minimum= threading.Thread(target= Min,args= (List,))

    Maximum.start()
    Minimum.start()

    Maximum.join()
    Minimum.join()


if __name__ =="__main__":
    main()