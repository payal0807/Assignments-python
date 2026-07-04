def main():
    n = int(input("Enter a number:"))

    binary= ""

    while n > 0:
        digit = n%2
        binary = str(digit)+binary
        n = n//2
    print (binary)


if __name__=="__main__":
    main()