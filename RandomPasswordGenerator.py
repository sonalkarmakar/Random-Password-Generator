import streamlit as st
from random import choice

default_values = {
	"min_passwd_len": 128,
	"safe_passwd_len": 64,
	"min_upper_chars": 1,
	"min_lower_chars": 1,
	"min_spcl_chars": 1,
	"min_digits": 1,
	"max_upper_chars": 16,
	"max_lower_chars": 16,
	"max_spcl_chars": 16,
	"max_digits": 16,
}

# Aligns input to centre and removes "Press Enter to apply" prompt
customise_text_input = """
	<style>
		.stTextInput > div > div > input { text-align: center; }
		[data-testid="InputInstructions"] { display:None; }
	</style>
	"""
st.markdown(customise_text_input, unsafe_allow_html=True)

# Icons for randomiser buttons
randomiser_icons = [":material/casino:", ":material/ifl:"]

# Password Generator Panel
generator_panel = st.container(key="generator_panel", border=True, width="content", horizontal_alignment="center")
with generator_panel:
	st.subheader(body="Random Password Generator", text_alignment="center", anchor=False)

	# Password Length Slider
	with st.container(border=False, horizontal=True):
		st.slider(label="Password Length", min_value=8, max_value=48)
		st.button(label="", key="rndm_btn_passlen", icon=choice(randomiser_icons), width="content", type="tertiary", help="Randomise password length.")

	# Panel for other sliders
	param_slider_panel = st.container(key="param_slider_panel", border=True)
	with param_slider_panel:
		with st.container(border=False, horizontal=True, vertical_alignment="center"):
			st.text(body="Valid Characters", width="stretch")
			st.button(label="", key="rndm_btn_param", icon=choice(randomiser_icons), width="content", type="tertiary", help="Randomise number of all character types.")

		# Divider takes too much vertical space

		# Slider for Number of Uppercase Characters
		with st.container(border=False, horizontal=True):
			st.slider(label="Number of Uppercase characters [`A`, `B`, `C`, ... `Z`]", min_value=1, max_value=10)
			st.button(label="", key="rndm_btn_uppercase", icon=choice(randomiser_icons), width="content", type="tertiary", help="Randomise number of uppercase characters.")

		# Slider for Number of Lowercase Characters
		with st.container(border=False, horizontal=True):
			st.slider(label="Number of Lowercase characters [`a`, `b`, `c`, ... `z`]", min_value=1, max_value=10)
			st.button(label="", key="rndm_btn_lowercase", icon=choice(randomiser_icons), width="content", type="tertiary", help="Randomise number of lowercase characters.")

		# Slider for Number of Special Characters
		with st.container(border=False, horizontal=True):
			st.slider(label="Number of Special characters [`,`, `!`, `_`, etc.]", min_value=1, max_value=10)
			st.button(label="", key="rndm_btn_special", icon=choice(randomiser_icons), width="content", type="tertiary", help="Randomise number of special characters.")

		# Slider for Number of Digits
		with st.container(border=False, horizontal=True):
			st.slider(label="Number of Digits [`0`, `1`, `2`, ... `9`]", min_value=1, max_value=10)
			st.button(label="", key="rndm_btn_digits", icon=choice(randomiser_icons), width="content", type="tertiary", help="Randomise number of digits.")

	# Password Generator Button
	st.button(label="**Generate Password**", type="primary", width="stretch")

	# Password Output Panel
	with st.container(horizontal=True):
		st.text_input(label="Generated Password", label_visibility="collapsed", placeholder="Your Randomly Generated Password")
		st.button(label="", key="copy_btn", icon=":material/content_copy:", width="content", type="tertiary")

with st.bottom:
	st.caption("Made by **Sonal Karmakar**", text_alignment="center")