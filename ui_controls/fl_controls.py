import flet as ft

from src.defined import *

__all__ =[
	"update_sldr_lbl",
	"passlen_sldr_warn",
	"update_passlen_sldr",
]

def update_passlen_sldr(label: ft.Text, panel: ft.Control, event: ft.Event[ft.Slider] | None = None) -> None:
	if event is not None:
		update_sldr_lbl(label=label, value=f"{event.control.value}")
		passlen_sldr_warn(panel, event.control)

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