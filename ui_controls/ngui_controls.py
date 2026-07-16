from nicegui import ui
from random import randint

from src.defined import param_sliders
from src.logic import generate_password

__all__ = [
	"load_markdown",
	"show_password",
	"set_slider_value",
	"copy_to_clipboard",
	"rndmz_all_sliders",
	"reset_all_sliders",
	"set_passwd_slider",
	"param_input_sliders",
	"chk_passlen_slider_val",
]

slider_passwd_len: ui.slider = ui.slider(min=1, max=5)
param_input_sliders: dict[str, ui.slider] = {}

# Load Markdown content from file
def load_markdown(file_path: str) -> str:
	with open(file_path, 'r', encoding="utf-8") as f:
		return f.read()

# Set a Slider's value
def set_slider_value(slider_ref: ui.slider, val: int, chk_passlen_slider: bool = False) -> None:
	slider_ref.set_value(value=val)
	if chk_passlen_slider:
		set_passwd_slider()

# Randomise a Slider's value
def rndmz_all_sliders(set_dpdt_slider: bool = True) -> None:
	for k, v in param_input_sliders.items():
		set_slider_value(v, randint(param_sliders[k]['min_val'], param_sliders[k]['max_val']))

	if set_dpdt_slider:
		set_passwd_slider()

# Reset all Parameter Sliders
def reset_all_sliders() -> None:
	for k, v in param_input_sliders.items():
		set_slider_value(v, param_sliders[k]['min_val'])

# Set Password Length to sum of depending parameters
def set_passwd_slider() -> None:
	# Editor might whine, don't know how to fix

	logical_min_val = sum(
		(slider.value if slider.value is not None else -100)
		for slider in param_input_sliders.values()
	)

	if slider_passwd_len.value is not None:
		if slider_passwd_len.value < logical_min_val:
			slider_passwd_len.value = logical_min_val

# Check Password Length Slider's value
def chk_passlen_slider_val() -> None:
	# Editor might whine, don't know how to fix
	logical_min_val = sum(
		(slider.value if slider.value is not None else -100)
		for slider in param_input_sliders.values()
	)

	if slider_passwd_len.value is not None:
		if slider_passwd_len.value < logical_min_val:
			reset_all_sliders()

# Shows the Generated Password in the Text Field
def show_password(text_input: ui.input) -> None:
	text_input.value = generate_password( # Editor might whine, don't know how to fix
		slider_passwd_len.value,
		param_input_sliders['slider_upper_chars'].value,
		param_input_sliders['slider_lower_chars'].value,
		param_input_sliders['slider_spcl_chars'].value,
		param_input_sliders['slider_digits'].value
	)

# Copies Text to User's Clipboard
def copy_to_clipboard(text: str | None) -> None:
	if text:
		ui.run_javascript(f"navigator.clipboard.writeText('{text}')") # WORKS ONLY ON LOCALHOST WITHOUT HTTPS
		ui.notify(message="Copied!", type="positive", position="top", color="primary")
	else:
		pass