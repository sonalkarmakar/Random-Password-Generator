from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

# Generates the Random Password
def generate_password(
	passwd_len: int = 1,
	upper_chars: int = 1, lower_chars: int = 1,
	spcl_chars: int = 1, num_digits: int = 1
) -> str:
	password: list[str] = []

	# Specified number of Uppercase Characters
	for i in range(upper_chars):
		password.append(choice(ascii_uppercase))

	# Specified number of Lowercase Characters
	for i in range(lower_chars):
		password.append(choice(ascii_lowercase))

	# Specified number of Special Characters
	for i in range(spcl_chars):
		password.append(choice(punctuation))

	# Specified number of Numeric Digits
	for i in range(num_digits):
		password.append(choice(digits))

	# Specified Password Length met with random characters
	if passwd_len > (upper_chars + lower_chars + num_digits):
		for i in range(passwd_len - (upper_chars + lower_chars + num_digits)):
			password.append(choice(choice([ascii_lowercase, ascii_uppercase, punctuation, digits])))

	shuffle(password) # Shuffle password

	return "".join(password) # Return password as string