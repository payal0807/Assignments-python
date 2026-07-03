def fun():
    x=10
    print(x)
fun()
print(x) 


#Here x is local variable which is accessible inside fun() only that's why only one time 10 will print
# print(x) this statement will not print because as it is written outside the fun() . x is not global variable 
#NameError: name 'x' is not defined ....because x is defined inside the function

