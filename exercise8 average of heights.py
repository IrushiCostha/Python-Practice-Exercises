#my code
print("Let's calculate the average student height!")

#heights
h = [int(x) for x in input("Please enter height in cm: ").split(',')]
#print(h)

#get summation
sh = sum(h)
#print(sh)

#get average
ash = round(sh/len(h))
print(ash)
