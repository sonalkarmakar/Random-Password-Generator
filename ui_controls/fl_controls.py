import flet as ft

__all__ =[
	"update_sldr_lbl",
]

def update_sldr_lbl(label: ft.Text, value: str | None = None, event: ft.Event[ft.Slider] | None = None) -> None:
	if event is not None:
		label.value = f"{event.control.value}"
	elif value is not None:
		label.value = value