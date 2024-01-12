import re

def validate_input(input_str, pattern):
    match = re.fullmatch(pattern, input_str)
    return bool(match)

# Email address pattern
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Mobile numbers of Bangladesh pattern
bangladesh_mobile_pattern = r'^\+8801[3-9]\d{8}$'

# Telephone numbers of the USA pattern
usa_telephone_pattern = r'^\+1\d{10}$'

# 16-character alphanumeric password pattern
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'

# Example usage:
email_input = "example@email.com"
mobile_input = "+8801712345678"
telephone_input = "+11234567890"
password_input = "Abcd1234@5678Efgh"

print(validate_input(email_input, email_pattern))                  # True
print(validate_input(mobile_input, bangladesh_mobile_pattern))     # True
print(validate_input(telephone_input, usa_telephone_pattern))      # True
print(validate_input(password_input, password_pattern))            # True
