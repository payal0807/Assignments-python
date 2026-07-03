#Write a program which contains one function ChkGreator () that accepts two numbers and prints the greator number 


#question 1 method 1

def ChkGreater(no1,no2):
    if no1>no2:
        print("the greator number is:",no1)
    else:
        print("The greator number is:",no2)   
    



def main():
    ChkGreater(10,20)



if __name__=="__main__":

    main()


#Input method


def ChkGreater(no1,no2):
    if no1>no2:
        print(no1,"is greator")
    else:
        print(no2,"is greator")   
    



def main():
    print("Enter First Number:")
    no1 = int(input())

    print("Enter Second Number:")
    no2 = int(input())



    ChkGreater(no1,no2)



if __name__=="__main__":

    main()


