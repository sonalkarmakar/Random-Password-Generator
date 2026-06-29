import streamlit as st
from random import randint
from src.defined import param_sliders

__all__ = [
	'load_markdown',
	'set_slider_value',
	'rndmz_all_sliders',
	'reset_all_sliders',
	'set_passwd_slider',
	'rndmz_param_slider',
	'chk_passlen_slider_val',
]

# Load Page Content from Markdown file
@st.cache_data
def load_markdown(file_path: str):
	with open(file_path, 'r', encoding="utf-8") as f:
		return f.read()

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