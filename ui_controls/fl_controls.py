import flet as ft

from src.defined import *
from random import randint

__all__ =[
	"passlen_sldr_warn",
	"update_sldr",
	"change_tab",
	"reset_all_sldrs",
	"rndmz_all_sldrs",
]

param_input_sldrs: dict[str, ft.Slider] = {}
param_sldr_labels: dict[str, ft.Text] = {}

# Update Slider and corresponding Value Label with provided Value
# Or, show Slider's current value in Value Label
def update_sldr(
	label: ft.Text, slider: ft.Slider, value: int | None = None,
	panel: ft.Control | None = None, is_passlen: bool = False
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

def reset_all_sldrs() -> None:
	for k, v in param_input_sldrs.items():
		update_sldr(param_sldr_labels[k], v, int(v.min))