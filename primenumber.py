def primeNO(value): #5
    for i in range(2,value): # 2,3,4
        if (value%i==0): 
            print("Its not prime number")
            break
        else:
            print("Its prime number")
            break

def main():
    no =  int(input("Enter number:"))

    ret =  primeNO(no)




if __name__ =="__main__":
    main()