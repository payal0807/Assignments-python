#Write a program which accepts one number and prints cube of that number 

def Cube(no1):
    ans = no1*no1*no1
    return ans


def main():
    print("Enter one number:")
    no1=int(input())

    ans = Cube(no1)
    print("Cube of given number is:",ans)

if __name__=="__main__":
    main()




#program without function
def main():
    no = int(input("Enter number:"))

    ans = no*no*no
    print(ans)

if __name__ == "__main__":
    main()
    