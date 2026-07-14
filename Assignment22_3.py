import multiprocessing

def countprime(no):
    
    
    count = 0
    for i in range(2,no+1):
            flag = True
      
            for j in range(2,i):
                  if i % j ==0:
                        flag = False
                        break
            
            if flag :
                  count = count + 1
    
    return count


    


def main():
    List = [10,15,20,25]

    print("Input List is:",List)

    Result= []

    pobj = multiprocessing.Pool()

    Result = pobj.map(countprime,List)

    pobj.close()
    pobj.join()

    print("Count of prime no is:")

    print(Result)


if __name__ =="__main__":
    main()



