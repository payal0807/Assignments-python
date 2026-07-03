def PalindromeChk(no):
        reverse = 0

        while no>0:
            digit =  no %10
            reverse = reverse*10+digit
            no=no//10

        return reverse


def main():
    no = int(input("Enter number:"))

    Ret = PalindromeChk(no)

    if (Ret==no):
         print("Its Palindrome")

    else:
        print("It is not palindrome")



if __name__=="__main__":
    main()