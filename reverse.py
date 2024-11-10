# Case 1: If 'n' is an integer and we want to reverse its digits
n = 123  # Example integer
reverse = 0

# Using a while loop to reverse the integer
temp_n = n  # Temporary variable to preserve the original n for printing later
while temp_n != 0:
    digit = temp_n % 10
    reverse = reverse * 10 + digit
    temp_n //= 10

print("Reversed Integer: " + str(reverse))

# Case 2: If 'n' is a string and we want to reverse it directly
n = "Ankit123"  # Example string
reverse_string = n[::-1]

print("Reversed String: " + reverse_string)
