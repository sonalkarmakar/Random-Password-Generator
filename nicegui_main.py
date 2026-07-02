from nicegui import ui
from random import choice

from src.defined import author_details, icons

# Create UI Elements
with ui.column(align_items="center").classes("w-full"):
	ui.html("<h3>Random Password Generator</h3>")
	with ui.card(align_items="center"):
		ui.html("<h4>Generate a Random Password</h4>")

		with ui.row(align_items="center").classes("w-full"):
			ui.label("Password Length")
			ui.space()
			ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense")

		slider1 = ui.slider(min=1, max=16, value=1).props("label-always").classes("w-[97%]")

		with ui.card(align_items="center").classes("no-shadow border border-gray-300 w-full"):
			with ui.row(align_items="center").classes("w-full"):
				ui.label("Valid Characters")
				ui.space()
				ui.button(color="flat", icon="o_refresh").props("flat round dense")
				ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense")

			ui.separator()

			with ui.row(align_items="center").classes("w-full"):
				ui.markdown("Number of Uppercase characters [`A`, `B`, `C`, ... `Z`]")
				ui.space()
				# NiceGUI doesn't support new Material icons like "ifl"
				ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense")

			slider2 = ui.slider(min=1, max=16, value=1).props("label-always").classes("w-[97%]")

			with ui.row(align_items="center").classes("w-full"):
				ui.markdown("Number of Lowercase characters [`a`, `b`, `c`, ... `z`]")
				ui.space()
				# NiceGUI doesn't support new Material icons like "ifl"
				ui.button(color="flat", icon=f"o_{icons['randomiser_icons'][0]}").props("flat round dense")

			slider3 = ui.slider(min=1, max=16, value=1).props("label-always").classes("w-[97%]")

with ui.footer():
	ui.space()
	ui.markdown(f"Made by **{author_details['name']}**")
	ui.space()

# Run the app
ui.run(native=False) # True = native app; False = webapp