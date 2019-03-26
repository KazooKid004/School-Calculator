import math
import time
#Welcome and variable setting
print ("here is my new converter i made during my prep!")
cat = raw_input ("pick one: length(l) and Weight(w):  ")
if cat == ("l"):
unit1 = raw_input ("Which unit would you like to convert from: ")
unit2 = raw_input ("Which unit would you like to convert to: ")
num1 = raw_input ("Enter your value: " )

    ##the calculation formulas 

if unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
    
