#!/bin/python2
num = raw_input("Enter number for conversion: ")

base = int(raw_input("Enter your number's base: "))

convert = int(raw_input("Enter what base you would like to convert it to: " ))

toconv = int(num, base) #toconv = input number in b10 to be converted
if convert == 16:
  output = hex(toconv)  #Converts to hex value if conversion given is b16
elif convert == 2:
  output = bin(toconv)
else:
  output = toconv

print(str(output))

root = int(raw_input("Enter what you would like to root your number by: "))

ans = 0

while ans ** root < abs(int(str(output), 10)):
  ans = ans + 1 
if ans ** root != abs(int(str(output), 10)):
  print("Can't do that!")
elif ans < 0:
  ans = -ans
print(str(ans))
