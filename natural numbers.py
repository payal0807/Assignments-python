def sumN(no):
    count = 0
    for i in range (1,no+1):
        
        count = count + i
    return count

    
def main():
    no =  int(input("Enter a number:"))


    ret =  sumN(no)
    print(ret)

 

if __name__ =="__main__":
    main()