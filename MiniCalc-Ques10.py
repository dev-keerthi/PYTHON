x=int(input("Value:"))
y=int(input("Value:"))
operation= input("Add/Sub/Multi/Div :")
if(operation=="Add"):
      print(x+y)
elif(operation=="Sub"):
    print(x-y)
elif(operation=="Multi"):
    print(x*y)
elif(operation=="Div"):
    print(x/y)
else:
    print("Invalid")
