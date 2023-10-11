def get_modified_string(input_string):
    if len(input_string) < 2:
        return ""

    first_two_chars = input_string[:2]
    last_two_chars = input_string[-2:]

    return first_two_chars + last_two_chars


sample_string1 = 'helloworld'
result1 = get_modified_string(sample_string1)
print("Sample String:", sample_string1)
print("Expected Result:", 'held')
print("Actual Result:", result1)

sample_string2 = 'my'
result2 = get_modified_string(sample_string2)
print("\nSample String:", sample_string2)
print("Expected Result:", 'mymy')
print("Actual Result:", result2)

sample_string3 = 'x'
result3 = get_modified_string(sample_string3)
print("\nSample String:", sample_string3)
print("Expected Result: Empty String")
print("Actual Result:", result3)