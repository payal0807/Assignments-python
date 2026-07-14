def Sum(no):
        sum = 0
        while no>0:
            Digit = no % 10
            sum = sum + Digit
            no =no //10
        return sum


def main():
    no = int(input("Enter number:"))

    Ret = Sum(no)
    print(Ret)



     
if __name__ =="__main__":
    main()