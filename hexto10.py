num = raw_input("Enter your number: ")

option = raw_input(" hex to binary(1)\n binary to hex(2)\n hex to decimal(3)\n binary to decimal(4)\n decimal to binary(5)\n decimal to hex(6)\n")

if option == str("1"):
  print(bin(int(num, 16)))
elif option == str("2"):
  print(hex(int(num, 2)))
elif option == str("3"):
  print(int(num, 16))
elif option == str("4"):
  print(int(num, 2)) 
elif option == str("5"):
  print(bin(int(num)))
elif option == str("6"):
  print(hex(int(num)))
elif option == str("7"):
  print(int(num, 8))
else:
  print("Oops! You made a mistake.")



