import threading

def EvenList(List):
    sum = 0
    for no in List:
        if no%2==0:
           sum = sum + no
    
    print("Sum of EvenList:",sum)



def OddList(List):
    sum = 0
    for no in List:
        if no%2!=0:
           sum = sum + no
    
    print("Sum of OddList:",sum)
          

def main():
    List = [2,4,1,3,7,9,8,10]

    print("list is:",List)

    t1 = threading.Thread(target=EvenList,args=(List,))

    t2 = threading.Thread(target=OddList,args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()




if __name__ =="__main__":
    main()