def main():
    no = int(input("Enter one number:"))
    sum = 0
    for i in range (1,no):
        if (no%i==0):
            sum = sum+i
    
    if sum==no:
        print("Perfect Number")
    else:
        print("Not a perfect number")



if __name__=="__main__":
    main()