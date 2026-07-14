def Count(Result,no):
    count = 0

    for i in Result:
        if (i == no ):
            count = count + 1
    return count


def main():
    x = int(input("Number of elements:"))

    Result = []

    print("Number Elements:")

    for i in range (x):
        y = int(input())
        Result.append(y)

    no = int(input("Enter element to search:"))


    Ret = Count(Result,no)
    print(f"{no} occurs {Ret } times in list ")

   
if __name__ =="__main__":
    main()