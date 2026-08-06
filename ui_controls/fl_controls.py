import flet as ft

from src.defined import *

__all__ =[
	"update_sldr_lbl",
	"passlen_sldr_warn",
	"update_sldr",
	"set_sldr_val",
]

param_input_sldrs: dict[str, ft.Slider] = {}

def update_sldr(label: ft.Text, slider: ft.Slider | None = None, panel: ft.Control | None = None, is_passlen: bool = False) -> None:
	if slider is not None:
		update_sldr_lbl(label=label, value=f"{slider.value}")
		if is_passlen and panel is not None:
			passlen_sldr_warn(panel, slider)

def update_sldr_lbl(label: ft.Text, value: str | None = None) -> None:
	label.value = f"{value}"

def passlen_sldr_warn(warn_msg: ft.Control, slider: ft.Slider) -> None:
	warn_msg.visible = slider.value > default_values['safe_passwd_len']
	if slider.value > default_values['safe_passwd_len']:
		slider.active_color = ft.Colors.AMBER
		slider.inactive_color = ft.Colors.AMBER_50
	else:
		slider.active_color = None
		slider.inactive_color = None

def set_sldr_val(slider: ft.Slider, value: ft.Number) -> None:
	slider.value = value

def change_tab(tab_list: list[ft.Control], curr_index: int = 0) -> None:
	for i in range(len(tab_list)):
		tab_list[i].visible = (i == curr_index)