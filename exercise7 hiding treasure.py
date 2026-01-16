line1 = ["A1", "B1", "C1"]
line2 = ["A2", "B2", "C2"]
line3 = ["A3", "B3", "C3"]

map = [line1,line2,line3]

print("Hiding your Treasure! X marks the spot.")
print(f"{line1}\n{line2}\n{line3}")
position = input("Where do you want to hide the treasure? ")

letter = position[0].lower()

abc = ["a", "b", "c"]

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
