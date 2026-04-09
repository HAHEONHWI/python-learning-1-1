input_string = input()
unique_characters = []
for char in input_string:
    if input_string.count(char) == 1:
        unique_characters.append(char)
print(unique_characters)