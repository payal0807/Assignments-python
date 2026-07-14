def Factors (no):
    result = []
    for i in range(1,no):
        if no%i==0:

            result.append(i)

    return result

def Add(result):
    sum = 0
    for no in result:
        sum = sum + no
    return sum
        


def main():
    no = int(input("Enter one number:"))

    Ret = Factors(no)
    print(Ret)

    sum  = Add(Ret)
    print(sum)

if __name__ =="__main__":
    main()