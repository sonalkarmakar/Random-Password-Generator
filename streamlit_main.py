import streamlit as st
from random import choice, randint

import ui_controls.st_controls as ui
from src.defined import content_paths, default_values, icons, param_sliders, author_details

# Stores user-input for parameters
param_input: dict[str, int] = {}

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

		# Loop through Parameters Dictionary to create UI elements
		for k, v in param_sliders.items():
			with st.container(border=False, horizontal=True):
				param_input.update({k:
					st.slider(
						key=k,
						label=param_sliders[k]['label'],
						min_value=param_sliders[k]['min_val'],
						max_value=param_sliders[k]['max_val'],
						on_change=ui.set_passwd_slider,
					)
				})

				st.button(
					label="",
					on_click=ui.rndmz_param_slider,
					width="content", type="tertiary",
					key=param_sliders[k]['rndmz_btn_key'],
					icon=choice(icons['randomiser_icons']),
					help=param_sliders[k]['rndmz_btn_tip'],
					args=(k, param_sliders[k]['min_val'], param_sliders[k]['max_val']),
				)

	# Password Output Panel
	with st.container(horizontal=True):
		# Password Generator Button
		st.button(
			label="**Generate Password**",
			type="primary", width="content",
			on_click=ui.show_password,
			args=(
				"passwd_textbox",
				passwd_len,
				param_input['slider_upper_chars'],
			 	param_input['slider_lower_chars'],
				param_input['slider_spcl_chars'],
				param_input['slider_digits']
			)
		)
		# Shows the Password
		passwd_text = st.text_input(
			key="passwd_textbox",
			label="Generated Password",
			label_visibility="collapsed",
			placeholder="Your Randomly Generated Password",
		)
		# [DOESN'T FUNCTION] Copy Password Button
		st.button(label="", key="copy_btn", icon=":material/content_copy:", width="content", type="tertiary", on_click=ui.copy_password)

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