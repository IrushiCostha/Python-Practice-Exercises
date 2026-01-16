#get 2 names
girl = str(input("Enter the girl's name: "))
boy = str(input("Enter the boy's name: "))

#combine names
com_names = girl+" "+ boy

#make sure all letters are in lowercase
lower_names = com_names.lower()

#count letters
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l+o+v+e

#get the score
score = int(str(first_digit) + str(second_digit))

print("The love calculator is calculating your score...")

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos!")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you make a good team!")
else:
    print(f"Your Score is {score}, Proud of you guyz! keep going.")

    




