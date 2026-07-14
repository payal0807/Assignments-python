import sys

Mult = lambda x,y : x * y

def main():
   

    if(len(sys.argv)==3):
        Value1 = int(sys.argv[1])

        Value2 = int(sys.argv[2])

        Ret = Mult(Value1,Value2)
        print(f"Multiplication of {Value1} and {Value2} is : {Ret}")

    else:
        print("Invalid number of Arguments")



if __name__ =="__main__":
    main()