import Arithmetic

def main():

    no1 = int(input("Enter one number:"))
    no2 = int(input("Enter second  number:"))

    Ret1 = Arithmetic.Add(no1,no2)
    print("Addition is:",Ret1)

    Ret2 = Arithmetic.Sub(no1,no2)
    print("Substraction is:",Ret2)

    Ret3 = Arithmetic.Mult(no1,no2)
    print("Multiplication is :",Ret3)

    Ret4 = Arithmetic.Div(no1,no2)
    print("Division is:",int(Ret4))

if __name__ == "__main__":
    main()