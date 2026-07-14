import threading

def Small(str):
    count = 0
    print("Thread Id is: ",threading.get_ident())
    print("Thread Name is:",threading.current_thread().name)

    for ch in str:
        if ch.islower():
            count = count + 1
    print("LowerCaseCount :",count)

def Capital(str):
    count = 0

    print("Thread Id is: ",threading.get_ident())
    print("Thread Name is:",threading.current_thread().name)

    for ch in str:
        if ch.isupper():
            count=count+1
    print("UpperCaseCount:",count)


def Digits(str):
    count = 0

    print("Thread Id is: ",threading.get_ident())
    print("Thread Name is:",threading.current_thread().name)

    for ch in str:
        if ch.isdigit():
            count=count+1
    print("Digits are:",count)

def main():
    x = (input("Enter string:"))

    print("Main Thread ID:",threading.get_ident())

    print("Main Thread name:",threading.current_thread().name)

    t1 = threading.Thread(target=Small, args = (x,))

    t2 = threading.Thread(target=Capital, args = (x,))

    t3 = threading.Thread(target=Digits, args = (x,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from Main thread")
    


if __name__ =="__main__":
    main()