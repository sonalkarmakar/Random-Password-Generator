import streamlit as st
from random import choice, randint

# Define Default Values
default_values = {
	"min_passwd_len": 8,
	"max_passwd_len": 128,
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
# Set Default Values in Session State
for key, value in default_values.items():
	st.session_state.setdefault(key, value)

# Sets a Slider's value
def set_slider_value(slider_key: str, value: int) -> None:
	st.session_state[slider_key] = value

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

st.set_page_config(layout="wide")

col1, col2 = st.columns(2, border=False, gap="small", )

with col1:
	# Password Generator Panel
	generator_panel = st.container(key="generator_panel", border=True, width="content", horizontal_alignment="center")
	with generator_panel:
		st.subheader(body="Random Password Generator", text_alignment="center", anchor=False)

		# Password Length Slider
		with st.container(border=False, horizontal=True):
			st.slider(
				label="Password Length",
				key="slider_passwd_len",
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
				args=("slider_passwd_len", randint(st.session_state['min_passwd_len'], st.session_state['safe_passwd_len'])),
			)

		# Panel for other sliders
		param_slider_panel = st.container(key="param_slider_panel", border=True)
		with param_slider_panel:
			with st.container(border=False, horizontal=True, vertical_alignment="center"):
				st.text(body="Valid Characters", width="stretch")
				st.button(
					label="",
					key="rndm_btn_param",
					icon=choice(randomiser_icons),
					width="content", type="tertiary",
					help="Randomise number of all character types.",
				)

			# Divider takes too much vertical space

			# Slider for Number of Uppercase Characters
			with st.container(border=False, horizontal=True):
				st.slider(
					key="slider_upper_chars",
					label="Number of Uppercase characters [`A`, `B`, `C`, ... `Z`]",
					min_value=st.session_state['min_upper_chars'],
					max_value=st.session_state['max_upper_chars'],
				)
				st.button(
					label="",
					key="rndm_btn_uppercase",
					icon=choice(randomiser_icons),
					width="content", type="tertiary",
					help="Randomise number of uppercase characters.",
					on_click=set_slider_value,
					args=("slider_upper_chars", randint(st.session_state['min_upper_chars'], st.session_state['max_upper_chars'])),
				)

			# Slider for Number of Lowercase Characters
			with st.container(border=False, horizontal=True):
				st.slider(
					key="slider_lower_chars",
					label="Number of Lowercase characters [`a`, `b`, `c`, ... `z`]",
					min_value=st.session_state['min_lower_chars'],
					max_value=st.session_state['max_lower_chars'],
				)
				st.button(
					label="",
					key="rndm_btn_lowercase",
					icon=choice(randomiser_icons),
					width="content", type="tertiary",
					help="Randomise number of lowercase characters.",
					on_click=set_slider_value,
					args=("slider_lower_chars", randint(st.session_state['min_lower_chars'], st.session_state['max_lower_chars'])),
				)

			# Slider for Number of Special Characters
			with st.container(border=False, horizontal=True):
				st.slider(
					key="slider_spcl_chars",
					label="Number of Special characters [`,`, `!`, `_`, etc.]",
					min_value=st.session_state['min_spcl_chars'],
					max_value=st.session_state['max_spcl_chars'],
				)
				st.button(
					label="",
					key="rndm_btn_special",
					icon=choice(randomiser_icons),
					width="content", type="tertiary",
					help="Randomise number of special characters.",
					on_click=set_slider_value,
					args=("slider_spcl_chars", randint(st.session_state['min_spcl_chars'], st.session_state['max_spcl_chars'])),
				)

			# Slider for Number of Digits
			with st.container(border=False, horizontal=True):
				st.slider(
					key="slider_digits",
					label="Number of Digits [`0`, `1`, `2`, ... `9`]",
					min_value=st.session_state['min_digits'],
					max_value=st.session_state['max_digits'],
				)
				st.button(
					label="", key="rndm_btn_digits",
					icon=choice(randomiser_icons),
					width="content", type="tertiary",
					help="Randomise number of digits.",
					on_click=set_slider_value,
					args=("slider_digits", randint(st.session_state['min_digits'], st.session_state['max_digits'])),
				)

		# Password Generator Button
		st.button(label="**Generate Password**", type="primary", width="stretch")

		# Password Output Panel
		with st.container(horizontal=True):
			st.text_input(label="Generated Password", label_visibility="collapsed", placeholder="Your Randomly Generated Password")
			st.button(label="", key="copy_btn", icon=":material/content_copy:", width="content", type="tertiary")

with col2:
	st.write(st.session_state)

with st.bottom:
	st.caption("Made by **Sonal Karmakar**", text_alignment="center")