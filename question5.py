s = "Python"
print(id(s))

s= s + "3"
print(id(s))

#yes there is change in ID
#as string is immutable ,we cant modifiy the characters inside it directly once created
#Instead it create a new string object and makes variable point to that object 

#here in above example we cant change python direct , but we can create another string object  and makes variable point to that object

#output for id 
#2347984424752
#2347984726480


