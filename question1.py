def Multiplication(Value1,Value2):
    Ans = Value1 *Value2
    return Ans


def main():
    No1= int(input("enter first no:"))

    No2=int(input("enter second no:"))

    ret = Multiplication(No1,No2)
    print("Multiplication is:",ret)

if __name__=="__main__":
    main()