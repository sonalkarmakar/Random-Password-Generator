from nicegui import ui
from random import randint

from src.defined import param_sliders
from src.logic import generate_password

__all__ = [
	"load_markdown",
	"show_password",
	"reset_btn_cond",
	"set_slider_value",
	"copy_to_clipboard",
	"reset_all_sliders",
	"rndmz_all_sliders",
	"set_passwd_slider",
	"param_slider_change",
	"chk_passlen_slider_val",
]

# Variable for Password Length Slider
slider_passwd_len: ui.slider = ui.slider(min=1, max=2)
# Dictionary for Parameter Sliders
param_input_sliders: dict[str, ui.slider] = {}
for k in param_sliders.keys():
	param_input_sliders.update({k: ui.slider(min=1, max=2)})

# Load Markdown content from file
def load_markdown(file_path: str) -> str:
	with open(file_path, 'r', encoding="utf-8") as f:
		return f.read()

# Handles change in Input Parameter Sliders
def param_slider_change(button: ui.button | None = None) -> None:
	set_passwd_slider()
	if button is not None:
		reset_btn_cond(button)

# Conditions to enable Reset Button
def reset_btn_cond(button: ui.button) -> None:
	# Check if any Input Slider value is more than minimum
	for slider in param_input_sliders.values():
		if slider.value > slider.props['min']:
			button.enable()
			return

	button.disable()

# Set a Slider's value
def set_slider_value(
	slider_ref: ui.slider, val: int, button: ui.button | None = None, chk_passlen_slider: bool = False
) -> None:
	slider_ref.set_value(value=val)
	# Set minimum possible Password Length for current parameter values
	if chk_passlen_slider:
		set_passwd_slider()
	# Check if Reset Button can be enabled
	if button is not None:
		if slider_ref.value > slider_ref.props['min']:
			button.enable()
		else:
			reset_btn_cond(button)

# Randomise a Slider's value
def rndmz_all_sliders(button: ui.button | None = None, set_dpdt_slider: bool = True) -> None:
	for k, v in param_input_sliders.items():
		set_slider_value(v, randint(param_sliders[k]['min_val'], param_sliders[k]['max_val']))
	# Enable Reset Button
	if button is not None:
		button.enable()
	# Set value of any dependent Slider(s)
	if set_dpdt_slider:
		set_passwd_slider()

# Reset all Parameter Sliders
def reset_all_sliders(button: ui.button | None = None) -> None:
	if button is not None:
		button.disable()
	for k, v in param_input_sliders.items():
		set_slider_value(v, param_sliders[k]['min_val'])

# Set Password Length to sum of depending parameters
def set_passwd_slider() -> None:
	# Linter might whine, not sure how to fix
	logical_min_val = sum(
		(slider.value if slider.value is not None else -100)
		for slider in param_input_sliders.values()
	)

	if slider_passwd_len.value is not None:
		if slider_passwd_len.value < logical_min_val:
			slider_passwd_len.value = logical_min_val

# Check Password Length Slider's value
def chk_passlen_slider_val() -> None:
	# Linter might whine, not sure how to fix
	logical_min_val = sum(
		(slider.value if slider.value is not None else -100)
		for slider in param_input_sliders.values()
	)

	if slider_passwd_len.value is not None:
		if slider_passwd_len.value < logical_min_val:
			reset_all_sliders()

# Shows the Generated Password in the Text Field
def show_password(text_input: ui.input) -> None:
	text_input.value = generate_password( # Linter might whine, not sure how to fix
		int(slider_passwd_len.value) if slider_passwd_len.value is not None else 1,

		int(param_input_sliders['slider_upper_chars'].value)
		if param_input_sliders['slider_upper_chars'].value is not None else 1,

		int(param_input_sliders['slider_lower_chars'].value)
		if param_input_sliders['slider_lower_chars'].value is not None else 1,

		int(param_input_sliders['slider_spcl_chars'].value)
		if param_input_sliders['slider_spcl_chars'].value is not None else 1,

		int(param_input_sliders['slider_digits'].value)
		if param_input_sliders['slider_digits'].value is not None else 1,
	)

# Copies Text to User's Clipboard
def copy_to_clipboard(text: str | None) -> None:
	if text:
		ui.run_javascript(f"navigator.clipboard.writeText('{text}')") # WORKS ONLY ON LOCALHOST WITHOUT HTTPS
		ui.notify(message="Copied!", type="positive", position="bottom", color="primary")
	else:
		pass