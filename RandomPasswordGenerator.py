import streamlit as st
from random import choice

# Aligns input to centre and removes "Press Enter to apply" prompt
customise_text_input = """
	<style>
		.stTextInput > div > div > input { text-align: center; }
		[data-testid="InputInstructions"] { display:None; }
	</style>
	"""
st.markdown(customise_text_input, unsafe_allow_html=True)

randomiser_icon = [":material/casino:", ":material/ifl:"]

generator_panel = st.container(key="generator_panel", border=True, width="content", horizontal_alignment="center")
with generator_panel:
	st.subheader(body="Random Password Generator", text_alignment="center", anchor=False)

	with st.container(border=False, horizontal=True):
		st.slider(label="Password Length", min_value=8, max_value=48)
		st.button(label="", key="rndm_btn_passlen", icon=choice(randomiser_icon), width="content", type="tertiary", help="Randomise password length.")

	param_slider_panel = st.container(key="param_slider_panel", border=True)
	with param_slider_panel:
		with st.container(border=False, horizontal=True, vertical_alignment="center"):
			st.text(body="Valid Characters", width="stretch")
			st.button(label="", key="rndm_btn_param", icon=choice(randomiser_icon), width="content", type="tertiary", help="Randomise number of all character types.")

		# Divider takes too much vertical space

		with st.container(border=False, horizontal=True):
			st.slider(label="Number of Uppercase characters [`A`, `B`, `C`, ... `Z`]", min_value=1, max_value=10)
			st.button(label="", key="rndm_btn_uppercase", icon=choice(randomiser_icon), width="content", type="tertiary", help="Randomise number of uppercase characters.")

		with st.container(border=False, horizontal=True):
			st.slider(label="Number of Lowercase characters [`a`, `b`, `c`, ... `z`]", min_value=1, max_value=10)
			st.button(label="", key="rndm_btn_lowercase", icon=choice(randomiser_icon), width="content", type="tertiary", help="Randomise number of lowercase characters.")

		with st.container(border=False, horizontal=True):
			st.slider(label="Number of Special characters [`,`, `!`, `_`, etc.]", min_value=1, max_value=10)
			st.button(label="", key="rndm_btn_special", icon=choice(randomiser_icon), width="content", type="tertiary", help="Randomise number of special characters.")

		with st.container(border=False, horizontal=True):
			st.slider(label="Number of Digits [`0`, `1`, `2`, ... `9`]", min_value=1, max_value=10)
			st.button(label="", key="rndm_btn_digits", icon=choice(randomiser_icon), width="content", type="tertiary", help="Randomise number of digits.")

	st.button(label="**Generate Password**", type="primary", width="stretch")

	with st.container(horizontal=True):
		st.text_input(label="Generated Password", label_visibility="collapsed", placeholder="Your Randomly Generated Password")
		st.button(label="", key="copy_btn", icon=":material/content_copy:", width="content", type="tertiary")

with st.bottom:
	st.caption("Made by **Sonal Karmakar**", text_alignment="center")