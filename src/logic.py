import streamlit as st
from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

# Generates the Random Password
def generate_password(textbox_key: str, passwd_len: int, upper_chars: int, lower_chars: int, spcl_chars: int, num_digits: int):
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

	st.session_state[textbox_key] = "".join(password) # Return password as string