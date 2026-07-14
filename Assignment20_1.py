import threading

def Even(no):
    for i in range(2,no+1,2):
        print(i)


def Odd(no):
        for i in range(1,no+1,2):
            print(i)


def main():

    t1 = threading.Thread(target=Even , args=(10,))

    t2 = threading.Thread(target=Odd , args=(10,))

    t1.start()
    t2.start ()

    t1.join()
    t2.join()



if __name__ =="__main__":
    main()