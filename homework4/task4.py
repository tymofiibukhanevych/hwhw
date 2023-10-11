
stored_name = "anton"


user_input = input("Enter your name: ")


stored_name_lower = stored_name.lower()
user_input_lower = user_input.lower()


if user_input_lower == stored_name_lower:
    print("Your input matches the stored name.")
else:
    print("Your input does not match the stored name.")