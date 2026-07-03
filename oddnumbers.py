def EvenNo(no):

    for i in range(1,no+1):
        if i% 2 != 0:
            print(i,end = " ")
        


def main():
    no =  int(input("Enter a number:"))

    ret =  EvenNo(no)
    



if __name__ =="__main__":
    main()