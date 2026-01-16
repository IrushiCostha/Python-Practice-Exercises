#pw generator

#importing the random module
import random


#creating character lists
letters = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','@','#','%','*']


#getting user inputs
print("Welcome to pw generator!")
let = int(input("How many letters do you want in your pw: \n"))
num = int(input("How many numbers do you want in your pw: \n"))
sym = int(input("How many symbols do you want in your pw: \n"))


#creating the pw
password = ""
for char in range(1, let + 1):
    ran = random.choice(letters)
    password += ran

for char in range(1, num + 1):
    ran = random.choice(numbers)
    password += str(ran)

for char in range(1, sym + 1):
    ran = random.choice(symbols)
    password += ran

print(password)
