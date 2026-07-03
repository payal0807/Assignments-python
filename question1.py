#Write a program which accepts one number and prints multiplication table of that number
def table(no):
    for  i in range(1,11):
        print (i*no,end = " ")



def main():
    num =  int(input("Enter a number:"))
    Ret=table(num)
    


if __name__ == "__main__":
    main()