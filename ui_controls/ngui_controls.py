from fastapi._compat.shared import value_is_sequence
from nicegui import ui
from random import randint

from src.defined import param_sliders

__all__ = [
	"load_markdown",
	"set_slider_value",
	"param_input_sliders",
]

slider_passwd_len: ui.slider
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
	logical_min_val = sum(slider.value for slider in param_input_sliders.values())

	if slider_passwd_len.value < logical_min_val:
		slider_passwd_len.value = logical_min_val

# Check Password Length Slider's value
def chk_passlen_slider_val() -> None:
	logical_min_val = sum(slider.value for slider in param_input_sliders.values())

	if slider_passwd_len.value < logical_min_val:
		reset_all_sliders()