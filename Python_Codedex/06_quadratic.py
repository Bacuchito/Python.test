#Create a quadratic.py program that asks the user for three numbers (a, b, c) and calculates the two roots using the quadratic formula
# quadratic formula

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

result= (-b + (b*b - 4*a*c)**0.5) / (2*a)
result2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(result)
print(result2)



