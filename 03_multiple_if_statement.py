a = int(input("Enter your age:"))

# if statement no:1
if(a%2 == 0):
    print("Your age is even")

    
# if statement no:2
if (a>=18):
    print("You are above the age of concent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 which is not a valid age")
    
else:
    print("You are below the age of concent")

    print("End of program")