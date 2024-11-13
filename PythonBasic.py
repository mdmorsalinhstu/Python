print("Hello World! This is Morsalin here.")
for i in range(5) :
  print("Morsalin")

#finding the even and odd numbers
a = int(input("Give a number: "))
if a % 2 == 0:
  print(str(a) + " is a even number")
else:
  print(str(a) + " is a odd number")
#finding the smallest and largest number among three
a = 9
b = 8
c = 10
if (a > b) & (a > c):
    print(str(a) + " is largest number")
elif (b > a) & (b > c):
    print(str(b) + "  is the largest number")
else:
    print(str(c) + " is the largest number")

if (a < b) & (a < c) :
    print(str(a) + " is the smallest number")
elif (b < a) & (b < c) :
    print(str(b) + " is the smallest number")
else :
    print(str(c) + " is the smallest number")

#That's done
