print("Percentage Calculator ")
print("")
x = float(input("Your Marks = "))
per = 100
y = float(input("Total Marks = "))
print("")
z = x * per / y
print("")
print("You Got = %.2f " %z)

if z >= 35:
	print("Congratulation")
else:
	print("Better Luck Next Time!")