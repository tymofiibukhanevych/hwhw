import random

lower_bound = 1
upper_bound = 10

num_of_numbers = 1

for _ in range(num_of_numbers):
    random_number = random.randint(lower_bound, upper_bound)

    print(random_number)

generated_number = random.randint(1, 10)
user_guess = int(input("Guess the number between 1 and 10: "))
if user_guess == generated_number:
    print("Congarts! You won the quiz!")
else:
    print(f"Sorry, my friend! Try again and never give up!")