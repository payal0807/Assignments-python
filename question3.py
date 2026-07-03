#Write a Program which accepts one number and prints square of that number

def Square(no1):
    ans = no1*no1
    print ("The square of given number is",ans)



def main():
    print("Take one number:")
    no1=int(input())

    Square(no1)


if __name__=="__main__":
    main()


#program without creating function

def main():
    no=int(input("Enter number:"))

    ans = no*no
    print(ans)
    
     
    


if __name__=="__main__":
    main()
