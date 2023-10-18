import random
input_string = input("Enter a string:" )
random_strings = []
for _ in range(5):
    random_characters = random.choice(input_string)
    random_strings.append(random_characters)
for i, random_strings in enumerate(random_strings):
    print(f"Random string {i + 1}: {random_strings}")