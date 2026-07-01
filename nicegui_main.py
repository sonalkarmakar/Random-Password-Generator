from nicegui import ui

from src.defined import author_details

# Create UI Elements
with ui.column(align_items="center").classes('w-full'):
	with ui.card(align_items="stretch"):
		ui.label("Random Password Generator")
		with ui.card(align_items="stretch").classes('no-shadow border border-gray-300'):
			slider = ui.slider(min=1, max=16, value=1).props('label-always')

with ui.footer():
	ui.markdown(f"Made by **{author_details['name']}**")

# Run the app
ui.run(native=False) # True = native app; False = webapp