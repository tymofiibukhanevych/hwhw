import random

input_string = input("Enter a string: ")

random_strings = []

for _ in range(5):

    random_string = ''

    for _ in range(len(input_string)):
        random_char = random.choice(input_string)
        random_string += random_char

    random_strings.append(random_string)

print("Random Strings:")
for i, rand_str in enumerate(random_strings):
    print(f"{i + 1}: {rand_str}")