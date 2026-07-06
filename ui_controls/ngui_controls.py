from nicegui import ui

__all__ = [
	"load_markdown",
	"set_slider_value",
]

def load_markdown(file_path: str) -> str:
	with open(file_path, 'r', encoding="utf-8") as f:
		return f.read()

def set_slider_value(slider_ref: ui.slider, val: int) -> None:
	slider_ref.set_value(value=val)