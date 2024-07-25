#Can be solved by applying triangle inequality theorem

def checkIfTriangleIsPossible(a,b,c):
    return a + b > c and a + c > b and b + c > a

#Input variables

a = int(input("Insert the first number: "))
b = int(input("Insert the second number: "))
c = int(input("Insert the third number: "))

if checkIfTriangleIsPossible(a,b,c):
    print('Yes')
else:
    print("No")