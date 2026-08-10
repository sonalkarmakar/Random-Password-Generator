from random import randint

import flet as ft

from src.defined import *
from src.logic import generate_password

__all__ =[
	"change_tab",
	"chk_passlen_sldr",
	"passlen_sldr_warn",
	"reset_all_sldrs",
	"rndmz_all_sldrs",
	"set_passlen_sldr",
	"show_password",
	"update_sldr",
]

param_input_sldrs: dict[str, ft.Slider] = {}
param_sldr_labels: dict[str, ft.Text] = {}

# Update Slider and corresponding Value Label with provided Value
# Or, show Slider's current value in Value Label
def update_sldr(
	label: ft.Text, slider: ft.Slider, value: int | None = None,
	panel: ft.Control | None = None, is_passlen: bool = False,
) -> None:
	if slider is not None:
		if value is not None:
			slider.value = value
		label.value = f"{slider.value}"

		if is_passlen and panel is not None:
			passlen_sldr_warn(panel, slider)

# Warns for high Password Length Slider value
def passlen_sldr_warn(warn_msg: ft.Control, slider: ft.Slider) -> None:
	warn_msg.visible = slider.value > default_values['safe_passwd_len']
	if slider.value > default_values['safe_passwd_len']:
		slider.active_color = ft.Colors.AMBER
		slider.inactive_color = ft.Colors.AMBER_50
	else:
		slider.active_color = None
		slider.inactive_color = None

# Reset all Parameter Sliders if Password Length Slider is below the sum of Parameter values
def chk_passlen_sldr(passlen_sldr: ft.Slider) -> None:
	logical_min_val: int = sum(
		int(slider.value) if slider.value is not None else 100
		for slider in param_input_sldrs.values()
	)

	if passlen_sldr.value is None or passlen_sldr.value < logical_min_val:
		reset_all_sldrs()

# Set Password Length Slider value if it's less than sum of Paramter values
def set_passlen_sldr(passlen_sldr: ft.Slider, passlen_lbl: ft.Text, warn_panel: ft.Control) -> None:
	logical_min_val: int = sum(
		int(slider.value) if slider.value is not None else 100
		for slider in param_input_sldrs.values()
	)

	if passlen_sldr.value is None or passlen_sldr.value < logical_min_val:
		update_sldr(passlen_lbl, passlen_sldr, logical_min_val, warn_panel, True)

# Switches Tab content Visibility
def change_tab(tab_list: list[ft.Control], curr_index: int = 0) -> None:
	for i in range(len(tab_list)):
		tab_list[i].visible = (i == curr_index)

# Randomise all Parameter Slider values
def rndmz_all_sldrs() -> None:
	for k, v in param_input_sldrs.items():
		x: int = randint(int(v.min), int(v.max)) # Linter may whine
		# Alternate approach tied to defined.py
		# x: int = randint(param_sliders[k]['min_val'], param_sliders[k]['max_val'])
		update_sldr(param_sldr_labels[k], v, x)

# Resets all Parameter Sliders to their minimum values
def reset_all_sldrs() -> None:
	for k, v in param_input_sldrs.items():
		update_sldr(param_sldr_labels[k], v, int(v.min))

def show_password(text_input: ft.TextField, passlen: int) -> None:
	text_input.value = generate_password(
		passlen,
		int(param_input_sldrs['slider_upper_chars'].value)
		if param_input_sldrs['slider_upper_chars'].value is not None else 1,

		int(param_input_sldrs['slider_lower_chars'].value)
		if param_input_sldrs['slider_lower_chars'].value is not None else 1,

		int(param_input_sldrs['slider_spcl_chars'].value)
		if param_input_sldrs['slider_spcl_chars'].value is not None else 1,

		int(param_input_sldrs['slider_digits'].value)
		if param_input_sldrs['slider_digits'].value is not None else 1,

	)