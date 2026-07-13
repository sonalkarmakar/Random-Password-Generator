from nicegui import ui
from random import choice, randint

import ui_controls.ngui_controls as ngc
from src.defined import author_details, icons, param_sliders, content_paths, default_values

dark_theme = ui.dark_mode()

# Create UI Elements
with ui.column(align_items="center").classes("w-full"):
	ui.html("<center><h3>Random Password Generator</h3></center>")
	with ui.card(align_items="center").classes("min-w-[34%] md:w-1/3 rounded-3xl"):
		with ui.tabs().classes("w-full flex").props("no-caps dense indicator-color='primary' active-color='primary'") as tabs:
			tab_1 = ui.tab("Generate Random Password").classes("flex-1")
			tab_2 = ui.tab("Secure Password Guidelines").classes("flex-1")

		with ui.tab_panels(tabs, value=tab_1).classes("w-full"):
			with ui.tab_panel(tab_1).classes("items-center p-1.5"):
				ui.html("<center><h4>Generate a Random Password</h4></center>")

				with ui.row(align_items="center").classes("w-full"):
					ui.label("Password Length")
					ui.space()
					ui.button(
						color="flat",
						icon=f"sym_o_{choice(icons['randomiser_icons'])}",
						on_click=lambda: ngc.set_slider_value(
							ngc.slider_passwd_len,
							randint(default_values['min_passwd_len'], default_values['safe_passwd_len'])
						),
					) \
						.props("flat round dense") \
						.tooltip("Randomise password length.")

				ngc.slider_passwd_len = ui.slider(
					min=default_values['min_passwd_len'],
					max=default_values['max_passwd_len'],
					value=default_values['min_passwd_len'],
					on_change=lambda: ngc.chk_passlen_slider_val(),
				) \
					.props("label-always id=slider_passwd_len").classes("w-[97%]")

				with ui.card(align_items="center") \
					.classes("w-full rounded-3xl shadow-inner shadow-gray-300 border border-gray-300 dark:shadow-gray-600 dark:border-gray-600"):
					with ui.row(align_items="center").classes("w-full gap-2"):
						ui.label("Valid Characters")
						ui.space()
						ui.button(color="flat", icon=f"sym_o_{icons['reset_settings']}", on_click=lambda: ngc.reset_all_sliders()) \
							.props("flat round dense padding='xs'") \
							.tooltip("Reset all parameters below.")
						ui.button(color="flat", icon=f"sym_o_{choice(icons['randomiser_icons'])}", on_click=lambda: ngc.rndmz_all_sliders()) \
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
									ngc.param_input_sliders[key],
									randint(param_sliders[key]['min_val'], param_sliders[k]['max_val']),
									chk_passlen_slider=True
								)
							) \
								.props("flat round dense padding='xs'") \
								.tooltip(param_sliders[k]['rndmz_btn_tip'])

						ngc.param_input_sliders.update({k:
							ui.slider(
								min=param_sliders[k]['min_val'],
								max=param_sliders[k]['max_val'],
								value=param_sliders[k]['min_val']
							).props(f"label-always id={k}").classes("w-[97%]")
						})

				with ui.row(align_items="center", wrap=False).classes("w-full gap-2"):
					ui.button(text="Generate", on_click=lambda: ngc.show_password(passwd_text)).props("no-caps no-wrap rounded")
					passwd_text = ui.input(placeholder="Your Randomly Generated Password").classes("w-full") \
						.props("outlined rounded dense input-class='text-center'")
					ui.button(
						color="flat", icon=f"sym_o_{icons['content_copy']}",
						on_click=lambda: ngc.copy_to_clipboard(passwd_text.value),
					) \
						.props("flat round dense").tooltip("Copy")

			with ui.tab_panel(tab_2).classes("items-center p-1.5 max-h-[75vh]"):
				with ui.expansion("Creating Secure Password", icon=f"sym_o_{icons['password']}").classes("w-full"):
					ui.markdown(ngc.load_markdown(content_paths['create_passwd']))

				with ui.expansion("Creating Secure Password", icon=f"sym_o_{icons['privacy_tip']}").classes("w-full"):
					ui.markdown(ngc.load_markdown(content_paths['maintain_passwd']))

with ui.footer().classes("p-0 bg-blue-grey-3 text-grey-9"):
	ui.switch("Dark Mode", value=False, on_change=lambda e: dark_theme.enable() if e.value else dark_theme.disable()) \
		.props("color=grey-9")
	ui.space()
	ui.markdown(f"Made by **{author_details['name']}**")
	ui.space()
	ui.markdown(f"Source code: [GitHub]({author_details['links']['repository']['GitHub']}) | [GitLab]({author_details['links']['repository']['GitLab']})")

# Run the app
ui.run(native=False) # True = native app; False = webapp