import streamlit as st
from random import choice, randint

import ui_controls.st_controls as ui
from src.defined import content_paths, default_values, icons, param_sliders, author_details

# Set Default Values in Session State
for key, value in default_values.items():
	st.session_state.setdefault(key, value)

# Aligns input to centre and removes "Press Enter to apply" prompt
customise_text_input = """
	<style>
		.stTextInput > div > div > input { text-align: center; }
		[data-testid="InputInstructions"] { display:None; }
	</style>
	"""
# Applies HTML definition above
st.markdown(customise_text_input, unsafe_allow_html=True)

# Use full page width instead of centred readable area
st.set_page_config(layout="centered", page_icon=choice(icons['randomiser_icons']), page_title="Random Password Generator",)
# Website title
st.title(body="Random Password Generator", text_alignment="center", anchor=False,)

# Password Generator Panel
generator_panel = st.container(key="generator_panel", border=True, width="stretch", horizontal_alignment="center", vertical_alignment="top",)
with generator_panel:
	st.header(body="Generate Random Password", text_alignment="center", anchor=False,)

	# Password Length Slider
	with st.container(border=False, horizontal=True):
		passwd_len = st.slider(
			label="Password Length",
			key="slider_passwd_len",
			on_change=ui.chk_passlen_slider_val,
			min_value=st.session_state['min_passwd_len'],
			max_value=st.session_state['max_passwd_len'],
		)
		st.button(
			label="",
			key="rndm_btn_passlen",
			icon=choice(icons['randomiser_icons']),
			width="content", type="tertiary",
			help="Randomise password length.",
			on_click=ui.set_slider_value,
			args=("slider_passwd_len", randint(st.session_state['min_passwd_len'], st.session_state['safe_passwd_len']), True, True),
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
				on_click=ui.reset_all_sliders,
				icon=":material/reset_settings:",
				width="content", type="tertiary",
				help="Reset all parameters below.",
				disabled=st.session_state['disable_reset_btn'],
			)
			st.button(
				label="",
				key="btn_rndmz_param",
				on_click=ui.rndmz_all_sliders,
				icon=choice(icons['randomiser_icons']),
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
				on_change=ui.set_passwd_slider,
			)
			st.button(
				label="",
				key="rndm_btn_uppercase",
				icon=choice(icons['randomiser_icons']),
				width="content", type="tertiary",
				help="Randomise number of uppercase characters.",
				on_click=ui.rndmz_param_slider,
				args=("slider_upper_chars", param_sliders["slider_upper_chars"]['min_val'], param_sliders["slider_upper_chars"]['max_val']),
			)

		# Slider for Number of Lowercase Characters
		with st.container(border=False, horizontal=True):
			lower_chars = st.slider(
				key="slider_lower_chars",
				label="Number of Lowercase characters [`a`, `b`, `c`, ... `z`]",
				min_value=param_sliders["slider_lower_chars"]['min_val'],
				max_value=param_sliders["slider_lower_chars"]['max_val'],
				on_change=ui.set_passwd_slider,
			)
			st.button(
				label="",
				key="rndm_btn_lowercase",
				icon=choice(icons['randomiser_icons']),
				width="content", type="tertiary",
				help="Randomise number of lowercase characters.",
				on_click=ui.rndmz_param_slider,
				args=("slider_lower_chars", param_sliders["slider_lower_chars"]['min_val'], param_sliders["slider_lower_chars"]['max_val']),
			)

		# Slider for Number of Special Characters
		with st.container(border=False, horizontal=True):
			spcl_chars = st.slider(
				key="slider_spcl_chars",
				label="Number of Special characters [`,`, `!`, `_`, etc.]",
				min_value=param_sliders["slider_spcl_chars"]['min_val'],
				max_value=param_sliders["slider_spcl_chars"]['max_val'],
				on_change=ui.set_passwd_slider,
			)
			st.button(
				label="",
				key="rndm_btn_special",
				icon=choice(icons['randomiser_icons']),
				width="content", type="tertiary",
				help="Randomise number of special characters.",
				on_click=ui.rndmz_param_slider,
				args=("slider_spcl_chars", param_sliders["slider_spcl_chars"]['min_val'], param_sliders["slider_spcl_chars"]['max_val']),
			)

		# Slider for Number of Digits
		with st.container(border=False, horizontal=True):
			num_digits = st.slider(
				key="slider_digits",
				label="Number of Digits [`0`, `1`, `2`, ... `9`]",
				min_value=param_sliders["slider_digits"]['min_val'],
				max_value=param_sliders["slider_digits"]['max_val'],
				on_change=ui.set_passwd_slider,
			)
			st.button(
				label="", key="rndm_btn_digits",
				icon=choice(icons['randomiser_icons']),
				width="content", type="tertiary",
				help="Randomise number of digits.",
				on_click=ui.rndmz_param_slider,
				args=("slider_digits", param_sliders["slider_digits"]['min_val'], param_sliders["slider_digits"]['max_val']),
			)

	# Password Output Panel
	with st.container(horizontal=True):
		# Password Generator Button
		st.button(
			label="**Generate Password**",
			type="primary", width="content",
			on_click=ui.show_password,
			args=("passwd_textbox", passwd_len, upper_chars, lower_chars, spcl_chars, num_digits)
		)
		# Shows the Password
		passwd_text = st.text_input(
			key="passwd_textbox",
			label="Generated Password",
			label_visibility="collapsed",
			placeholder="Your Randomly Generated Password",
		)
		# Copy Password Button
		st.button(label="", key="copy_btn", icon=":material/content_copy:", width="content", type="tertiary")

# Password Guidelines Panel
guidelines_panel = st.container(key="guidelines_panel", border=True, width="stretch", horizontal_alignment="center", vertical_alignment="top",)
with guidelines_panel:
	st.header(body="Password Guidelines", text_alignment="center", anchor=False,)

	with st.expander(key="expnd_create_passwd", icon=":material/password:", label="**Creating Secure Password**"):
		st.markdown(ui.load_markdown(content_paths['create_passwd']))

	with st.expander(key="expnd_maintain_passwd", icon=":material/privacy_tip:", label="**Maintaining Password Security**",):
		st.markdown(ui.load_markdown(content_paths['maintain_passwd']))

with st.bottom:
	st.caption(
		text_alignment="center",
		body=f"Made by **{author_details['name']}** | [GitHub]({author_details['links']['websites']['GitHub']}) | [GitLab]({author_details['links']['websites']['GitLab']})",
	)