print("Let's find the average of the hights! Enter the hights with a space.")

h = [int(heights) for heights in input("Enter hights: ").split( )]
print(h)

#get summation
total = 0
for one_height in h:
    total += one_height
print(f"Total height is: {total}cm")

#get the length
no_of_students = 0
for student in h:
    no_of_students += 1
print(f"Number of students are: {no_of_students}")
    
#get average
average = round(total/no_of_students)
print(f"Average height is: {average}")
