def is_valid_phone_number(input_string):

    if len(input_string) == 10:

        if input_string.isdigit():
            return True
    return False


phone_number = input("Enter a 10-digit phone number: ")

if is_valid_phone_number(phone_number):
    print("The phone number is in the right format.")
else:
    print("The phone number is not in the right format.")