# Created By 
# Deepak Jaiswar 25/7/20

print("Percentage Calculator ")
print("")

#Input Your Marks
x = float(input("Your Marks = "))

#per multiplying number
per = 100

#Input Sub Total Marks
y = float(input("Total Marks = "))
print("")

#Here we put aur formula
z = x * per / y
print("")

print("You Got = %.2f " %z)

if z >= 35:
	print("Congratulation")
else:
	print("Better Luck Next Time!")
