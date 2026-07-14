import multiprocessing
import time


def CalPower(no):
    
    sum = 0
    for i in range(1,no+1):
        sum = sum  + (i ** 5)

    return sum


def main():
    List = [1000000,2000000,3000000,4000000,5000000]

    print(List)

    Result= []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(CalPower,List)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Power calculation is:")

    print(Result)

    print(f"time required: {end_time - start_time}")


if __name__ =="__main__":
    main()