from nicegui import ui
from random import choice

from src.defined import author_details, icons, param_sliders

param_input: dict[str, int] = {}

# Create UI Elements
with ui.column(align_items="center").classes("w-full"):
	ui.html("<center><h3>Random Password Generator</h3></center>")
	with ui.card(align_items="center").classes("rounded-3xl"):
		ui.html("<center><h4>Generate a Random Password</h4></center>")

		with ui.row(align_items="center").classes("w-full"):
			ui.label("Password Length")
			ui.space()
			ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense")

		passwd_len = ui.slider(min=1, max=16, value=1).props("label-always").classes("w-[97%]")

		with ui.card(align_items="center").classes("w-full no-shadow rounded-3xl border border-gray-300"):
			with ui.row(align_items="center").classes("w-full gap-2"):
				ui.label("Valid Characters")
				ui.space()
				ui.button(color="flat", icon="o_refresh").props("flat round dense padding='xs'")
				ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense padding='xs'")

			ui.separator()

			for k, v in param_sliders.items():
				with ui.row(align_items="center").classes("w-full"):
					ui.markdown(param_sliders[k]['label'])
					ui.space()
					# NiceGUI doesn't support new Material icons like "ifl"
					ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense padding='xs'")

				slider = ui.slider(
					min=param_sliders[k]['min_val'],
					max=param_sliders[k]['max_val'],
					value=param_sliders[k]['min_val']
				).props("label-always").classes("w-[97%]")

				# print(type(slider.value)) shows <class 'int'>, but linter detects it as float | None
				assert isinstance(slider.value, int) # Eliminate float and None types
				param_input.update({k: slider.value})

		with ui.row(align_items="center", wrap=False).classes("w-full gap-2"):
			ui.button(text="Generate").props("no-caps no-wrap rounded")
			ui.input(placeholder="Your Randomly Generated Password").props("outlined rounded dense input-class='text-center'").classes("w-full")
			ui.button(color="flat", icon=f"o_{icons['content_copy']}").props("flat round dense")

with ui.footer():
	ui.space()
	ui.markdown(f"Made by **{author_details['name']}**")
	ui.space()

# Run the app
ui.run(native=False) # True = native app; False = webapp