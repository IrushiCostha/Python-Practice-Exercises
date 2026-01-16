#find the highest mark
print("Let's find the highest mark. please enter marks with a space")

#get data and converting to integer
marks = [int(x) for x in(input("Enter marks: ")).split( )]
print(marks)

highest = 0
for maxi in marks:
    if maxi > highest:
        highest = maxi

print(f"Highest mark is: {highest}")
