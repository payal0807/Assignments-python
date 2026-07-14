import sys

Power = lambda x : x ** 2

def main():
   

    if(len(sys.argv)==2):
        Value = int(sys.argv[1])
        Ret = Power(Value)
        print(f"power of {Value} is {Ret}")

    else:
        print("Invalid number of Arguments")



if __name__ =="__main__":
    main()