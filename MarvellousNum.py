def ChkPrime(list):
    NewList=[]
    for no in list :
        if no<2:
            continue
        for i in range(2,no):
            if no%i==0:
               break
        else:
            NewList.append(no)
    return NewList

