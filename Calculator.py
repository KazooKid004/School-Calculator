#script written by KazooKid004
#Help from @Freddy0001, @Matt-Gleich, and @Cal-Hagner
#------------------------------------
import math

# This function adds the two numbers
def add(x, y):
   return x + y
# This function subtracts the two numbers
def subtract(x, y):
   return x - y
# This function multiplies the two numbers
def multiply(x, y):
   return x * y
# This function adds the two numbers
def add(x, y):
   return x + y
# This function subtracts the two numbers
def subtract(x, y):
   return x - y
# This function multiplies the two numbers
def multiply(x, y):
   return x * y
# This function divides the two numbers
def divide(x, y):
   return x / y
#This function raises x to the y power
def exponent(x, y):
    return x ** y
#these are your options to pick from
print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exponent\n6.Squareroot\n7.Sine\n8.Cosine\n9.Tangent\n10.InvSine\n11.InvCos\n12.InvTan")

# Take response from the user
choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12):")

if (int(choice) <= 5): #only 1 input for any choice above 5
   num1 = float(input("Enter first number:"))
   num2 = float(input("Enter second number:"))
else:
   num1 = float(input("Enter your number:"))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
   print("Haha you cant do basic math lol!")#addition
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2)) #subtraction
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2)) #multiplication
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2)) #Division
elif choice == '5':
   print(num1,"**",num2,"=", exponent(num1,num2)) #exponent
elif choice == "6":
   print(math.sqrt(num1)) #Squareroot
elif choice == "7":
   print(math.degrees(math.sin(num1))) #Sine
elif choice == "8":
   print(math.degrees(math.cos(num1))) #Cosine
elif choice == "9":
    print(math.degrees(math.tan(num1))) #Tangent
elif choice == "10":
    print(math.degrees(math.asin(num1))) #InvSine
elif choice == "11":
    print(math.degrees(math.acos(num1))) #InvCos
elif choice == "12":
    print(math.degrees(math.atan(num1))) #InvTan
else:
   print("Invalid input")
   print("here you go my dude")
