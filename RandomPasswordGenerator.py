import streamlit as st
from random import choice, randint, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

# Sets a Slider's value
def set_slider_value(slider_key: str, value: int, is_btn_disabled: bool = False, chk_passlen_slider: bool = False) -> None:
	st.session_state[slider_key] = value
	st.session_state['disable_reset_btn'] = is_btn_disabled
	if chk_passlen_slider:
		chk_passlen_slider_val()

# Randomize Parameter Slider
def rndmz_param_slider(slider_key: str, bottom: int, top: int, set_dpdt_slider: bool = True):
	set_slider_value(slider_key, randint(bottom, top))
	if set_dpdt_slider:
		set_passwd_slider()

# Randomise all Parameter Sliders
def rndmz_all_sliders():
	for key, val in param_sliders.items():
		rndmz_param_slider(key, val['min_val'], val['max_val'], False)
	set_passwd_slider()

# Reset all Parameter Sliders
def reset_all_sliders():
	st.session_state['disable_reset_btn'] = True
	for key, val in param_sliders.items():
		st.session_state[key] = val['min_val']

# Check Password Length Slider's value
def chk_passlen_slider_val():
	logical_min_val = (
		st.session_state['slider_upper_chars'] +
		st.session_state['slider_lower_chars'] +
		st.session_state['slider_spcl_chars'] +
		st.session_state['slider_digits']
	)

	if st.session_state['slider_passwd_len'] < logical_min_val:
		reset_all_sliders()

# Set Password Length to sum of depending parameters
def set_passwd_slider():
	logical_min_val = (
		st.session_state['slider_upper_chars'] +
		st.session_state['slider_lower_chars'] +
		st.session_state['slider_spcl_chars'] +
		st.session_state['slider_digits']
	)

	if st.session_state['slider_passwd_len'] < logical_min_val:
		set_slider_value("slider_passwd_len", logical_min_val)

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

# Define Default Values
default_values = {
	"min_passwd_len": 8,
	"max_passwd_len": 128,
	"safe_passwd_len": 64,
	"disable_reset_btn": True,
}
# Set Default Values in Session State
for key, value in default_values.items():
	st.session_state.setdefault(key, value)

# Parameter Slider dictionary
param_sliders = {
	"slider_upper_chars": {
		"min_val": 1,
		"max_val": 16,
	},
	"slider_lower_chars": {
		"min_val": 1,
		"max_val": 16,
	},
	"slider_spcl_chars": {
		"min_val": 1,
		"max_val": 16,
	},
	"slider_digits": {
		"min_val": 1,
		"max_val": 16,
	},
}

# Aligns input to centre and removes "Press Enter to apply" prompt
customise_text_input = """
	<style>
		.stTextInput > div > div > input { text-align: center; }
		[data-testid="InputInstructions"] { display:None; }
	</style>
	"""
# Applies HTML definition above
st.markdown(customise_text_input, unsafe_allow_html=True)

# Icons for randomiser buttons
randomiser_icons = [":material/casino:", ":material/ifl:"]

# Use full page width instead of centred readable area
st.set_page_config(layout="centered", page_icon=choice(randomiser_icons), page_title="Random Password Generator",)

# Password Generator Panel
generator_panel = st.container(key="generator_panel", border=True, width="stretch", horizontal_alignment="center", vertical_alignment="top")
with generator_panel:
	st.subheader(body="Random Password Generator", text_alignment="center", anchor=False)

	# Password Length Slider
	with st.container(border=False, horizontal=True):
		passwd_len = st.slider(
			label="Password Length",
			key="slider_passwd_len",
			on_change=chk_passlen_slider_val,
			min_value=st.session_state['min_passwd_len'],
			max_value=st.session_state['max_passwd_len'],
		)
		st.button(
			label="",
			key="rndm_btn_passlen",
			icon=choice(randomiser_icons),
			width="content", type="tertiary",
			help="Randomise password length.",
			on_click=set_slider_value,
			args=("slider_passwd_len", randint(st.session_state['min_passwd_len'], st.session_state['safe_passwd_len']), True),
		)

	warning_panel = st.empty()

	# Password length might be too long!
	if passwd_len > st.session_state['safe_passwd_len']:
		st.warning(
			title="Password length might be too long!",
			body="Old systems may not support this length.",
			icon=":material/warning:",
		)

	# Panel for other sliders
	param_slider_panel = st.container(key="param_slider_panel", border=True)
	with param_slider_panel:
		with st.container(border=False, horizontal=True, vertical_alignment="center"):
			st.text(body="Valid Characters", width="stretch")
			st.button(
				label="",
				key="reset_all_params",
				on_click=reset_all_sliders,
				icon=":material/reset_settings:",
				width="content", type="tertiary",
				help="Reset all parameters below.",
				disabled=st.session_state['disable_reset_btn'],
			)
			st.button(
				label="",
				key="btn_rndmz_param",
				on_click=rndmz_all_sliders,
				icon=choice(randomiser_icons),
				width="content", type="tertiary",
				help="Randomise number of all character types.",
			)

		# Divider takes too much vertical space

		# Slider for Number of Uppercase Characters
		with st.container(border=False, horizontal=True):
			upper_chars = st.slider(
				key="slider_upper_chars",
				label="Number of Uppercase characters [`A`, `B`, `C`, ... `Z`]",
				min_value=param_sliders["slider_upper_chars"]['min_val'],
				max_value=param_sliders["slider_upper_chars"]['max_val'],
				on_change=set_passwd_slider,
			)
			st.button(
				label="",
				key="rndm_btn_uppercase",
				icon=choice(randomiser_icons),
				width="content", type="tertiary",
				help="Randomise number of uppercase characters.",
				on_click=rndmz_param_slider,
				args=("slider_upper_chars", param_sliders["slider_upper_chars"]['min_val'], param_sliders["slider_upper_chars"]['max_val']),
			)

		# Slider for Number of Lowercase Characters
		with st.container(border=False, horizontal=True):
			lower_chars = st.slider(
				key="slider_lower_chars",
				label="Number of Lowercase characters [`a`, `b`, `c`, ... `z`]",
				min_value=param_sliders["slider_lower_chars"]['min_val'],
				max_value=param_sliders["slider_lower_chars"]['max_val'],
				on_change=set_passwd_slider,
			)
			st.button(
				label="",
				key="rndm_btn_lowercase",
				icon=choice(randomiser_icons),
				width="content", type="tertiary",
				help="Randomise number of lowercase characters.",
				on_click=rndmz_param_slider,
				args=("slider_lower_chars", param_sliders["slider_lower_chars"]['min_val'], param_sliders["slider_lower_chars"]['max_val']),
			)

		# Slider for Number of Special Characters
		with st.container(border=False, horizontal=True):
			spcl_chars = st.slider(
				key="slider_spcl_chars",
				label="Number of Special characters [`,`, `!`, `_`, etc.]",
				min_value=param_sliders["slider_spcl_chars"]['min_val'],
				max_value=param_sliders["slider_spcl_chars"]['max_val'],
				on_change=set_passwd_slider,
			)
			st.button(
				label="",
				key="rndm_btn_special",
				icon=choice(randomiser_icons),
				width="content", type="tertiary",
				help="Randomise number of special characters.",
				on_click=rndmz_param_slider,
				args=("slider_spcl_chars", param_sliders["slider_spcl_chars"]['min_val'], param_sliders["slider_spcl_chars"]['max_val']),
			)

		# Slider for Number of Digits
		with st.container(border=False, horizontal=True):
			num_digits = st.slider(
				key="slider_digits",
				label="Number of Digits [`0`, `1`, `2`, ... `9`]",
				min_value=param_sliders["slider_digits"]['min_val'],
				max_value=param_sliders["slider_digits"]['max_val'],
				on_change=set_passwd_slider,
			)
			st.button(
				label="", key="rndm_btn_digits",
				icon=choice(randomiser_icons),
				width="content", type="tertiary",
				help="Randomise number of digits.",
				on_click=rndmz_param_slider,
				args=("slider_digits", param_sliders["slider_digits"]['min_val'], param_sliders["slider_digits"]['max_val']),
			)

	# Password Generator Button
	st.button(
		label="**Generate Password**",
		type="primary", width="stretch",
		on_click=generate_password,
		args=("passwd_textbox", passwd_len, upper_chars, lower_chars, spcl_chars, num_digits)
	)

	# Password Output Panel
	with st.container(horizontal=True):
		passwd_text = st.text_input(
			key="passwd_textbox",
			label="Generated Password",
			label_visibility="collapsed",
			placeholder="Your Randomly Generated Password",
		)
		st.button(label="", key="copy_btn", icon=":material/content_copy:", width="content", type="tertiary")

with st.bottom:
	st.caption("Made by **Sonal Karmakar**", text_alignment="center")