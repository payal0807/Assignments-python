#Write a program which accepts one number and checks whether it is divisble by 3 and 5


def main():
    print("Enter one number:")
    no1=int(input())
    if no1%3==0 and no1%5==0:
        print("Divisible by 3 and 5")
    else:
        print("Condition not satisfied")


   

if __name__=="__main__":
    main()


#using function 

def Divisible(value):
      if value%3==0 and value%5==0:
        print("Divsible by 3 and 5")
       
      else:
        print("Not Divisible by 3 and 5")
       


def main():
    no =  int(input("Enter number:"))

    Ret=Divisible(no)



if __name__ == "__main__":
    main()