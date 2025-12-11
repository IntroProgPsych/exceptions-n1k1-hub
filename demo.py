



try:
   print(1/0)
except:
   print("You cant divide by 0")
else:
   print("All is good")
finally:
   print("This is the end!!!")

try:
  number = int(input("Type in a number: "))
  1/number
except ValueError:
   print("You need to type a number")
except:
   print("Something went wrong")
else:
   print("All is good!")
finally:
   print("This is the end!!!")