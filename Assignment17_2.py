def main():

    no = int(input("Enter one number:"))

    for i in range(no):  #this loop will decide how much rows we want (outer loop)
        for j in range(no):  #this loop will decide coloumn (inner loop)
            print("*",end = " " )
        print()



if __name__ == "__main__":
    main()