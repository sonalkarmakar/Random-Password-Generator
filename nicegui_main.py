from nicegui import ui
from random import choice, randint

import ui_controls.ngui_controls as ngc
from src.defined import author_details, icons, param_sliders, content_paths

param_input_sliders: dict[str, ui.slider] = {}

# Create UI Elements
with ui.column(align_items="center").classes("w-full"):
	ui.html("<center><h3>Random Password Generator</h3></center>")
	with ui.card(align_items="center").classes("min-w-[34%] md:w-1/3 rounded-3xl"):
		with ui.tabs().classes("w-full flex").props("no-caps dense indicator-color='primary' active-color='primary'") as tabs:
			tab_1 = ui.tab("Generate Random Password").classes("flex-1")
			tab_2 = ui.tab("Secure Password Guidelines").classes("flex-1")

		with ui.tab_panels(tabs, value=tab_1).classes("w-full"):
			with ui.tab_panel(tab_1).classes("items-center p-1"):
				ui.html("<center><h4>Generate a Random Password</h4></center>")

				with ui.row(align_items="center").classes("w-full"):
					ui.label("Password Length")
					ui.space()
					ui.button(color="flat", icon=f"sym_o_{icons['randomiser_icons'][1]}").props("flat round dense") \
						.tooltip("Randomise password length.")

				passwd_len = ui.slider(min=1, max=16, value=1).props("label-always").classes("w-[97%]")

				with ui.card(align_items="center").classes("w-full rounded-3xl shadow-inner shadow-gray-300 border border-gray-300"):
					with ui.row(align_items="center").classes("w-full gap-2"):
						ui.label("Valid Characters")
						ui.space()
						ui.button(color="flat", icon=f"sym_o_{icons['reset_settings']}") \
							.props("flat round dense padding='xs'") \
							.tooltip("Reset all parameters below.")
						ui.button(color="flat", icon=f"sym_o_{choice(icons['randomiser_icons'])}") \
							.props("flat round dense padding='xs'") \
							.tooltip("Randomise number of all character types.")

					ui.separator()

					for k, v in param_sliders.items():
						with ui.row(align_items="center").classes("w-full"):
							ui.markdown(param_sliders[k]['label'])
							ui.space()
							ui.button(
								color="flat",
								icon=f"sym_o_{choice(icons['randomiser_icons'])}",
								on_click=lambda _, key=k: ngc.set_slider_value(
									param_input_sliders[key],
									randint(param_sliders[key]['min_val'], param_sliders[k]['max_val']),
								)
							) \
								.props("flat round dense padding='xs'") \
								.tooltip(param_sliders[k]['rndmz_btn_tip'])

						param_input_sliders.update({k:
							ui.slider(
								min=param_sliders[k]['min_val'],
								max=param_sliders[k]['max_val'],
								value=param_sliders[k]['min_val']
							).props("label-always").classes("w-[97%]")
						})

				with ui.row(align_items="center", wrap=False).classes("w-full gap-2"):
					ui.button(text="Generate").props("no-caps no-wrap rounded")
					ui.input(placeholder="Your Randomly Generated Password").classes("w-full") \
						.props("outlined rounded dense input-class='text-center'")
					ui.button(color="flat", icon=f"sym_o_{icons['content_copy']}").props("flat round dense").tooltip("Copy")

			with ui.tab_panel(tab_2).classes("items-center p-1 max-h-[75vh]"):
				with ui.expansion("Creating Secure Password", icon=f"sym_o_{icons['password']}").classes("w-full"):
					ui.markdown(ngc.load_markdown(content_paths['create_passwd']))#.classes("max-h-[57vh]")

				with ui.expansion("Creating Secure Password", icon=f"sym_o_{icons['privacy_tip']}").classes("w-full"):
					ui.markdown(ngc.load_markdown(content_paths['maintain_passwd']))#.classes("max-h-[57vh]")

with ui.footer().classes("p-0"):
	ui.space()
	ui.markdown(f"Made by **{author_details['name']}**")
	ui.space()

# Run the app
ui.run(native=False) # True = native app; False = webapp