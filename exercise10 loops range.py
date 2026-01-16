#sum of even numbers from 1 to the number which enters by the user
#getting the veriable
print("Welcome!")
x = int(input("Enter a number: "))

tot = 0
for y in range(2,x+1,2):
    print(y)
    tot += y

print(f"Total is {tot}")
