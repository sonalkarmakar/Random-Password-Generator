from nicegui import ui
from random import choice

from src.defined import author_details, icons

# Create UI Elements
with ui.column(align_items="center").classes('w-full'):
	ui.html("<h3>Random Password Generator</h3>")
	with ui.card(align_items="stretch"):
		ui.label("Generate a Random Password")
		with ui.card(align_items="stretch").classes("no-shadow border border-gray-300"):
			with ui.row(align_items="center"):
				ui.label("Valid Characters")
				ui.space()
				ui.button(color="flat", icon="o_refresh").props("flat round dense")
				ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense")

			ui.separator()

			with ui.row(align_items="center"):
				ui.markdown("Number of Uppercase characters [`A`, `B`, `C`, ... `Z`]")
				ui.space()
				# NiceGUI doesn't support new Material icons like "ifl"
				ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense")

			slider = ui.slider(min=1, max=16, value=1).props('label-always switch-label-side')

with ui.footer():
	ui.markdown(f"Made by **{author_details['name']}**")

# Run the app
ui.run(native=False) # True = native app; False = webapp