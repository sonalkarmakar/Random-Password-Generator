from nicegui import ui
from random import choice, randint

import ui_controls.ngui_controls as ngc
from src.defined import author_details, icons, param_sliders, content_paths, default_values

ui_appearance: dict[str, dict[str, str]] = {
	"class": {
		"tab": "flex-1",
		"tab_panel": "items-center p-1.5",
		"link": "flex items-center text-blue-700 gap-1 p-0",
		"footer_icons": "w-4 h-4 opacity-70",
		"footer": "items-center p-0 bg-blue-grey-3 text-grey-9",
		"warning_text": "text-amber-600 dark:text-amber-100",
		"warning_heading": "font-bold leading-none text-amber-700 dark:text-amber-200",
		"warning_box": "gap-2 p-2 rounded-lg border border-amber-300 bg-amber-100 dark:bg-amber-800",
		"params_card": "w-full rounded-3xl shadow-inner shadow-gray-300 border border-gray-300 dark:shadow-gray-600 dark:border-gray-600",
	},
	"props": {
		"ui_tabs": "no-caps dense indicator-color='primary' active-color='primary'",
		"input": "outlined rounded dense input-class='text-center'",
		"tert_btn": "flat round dense padding='xs'",
		"generate_btn": "no-caps no-wrap rounded",
		"copy_btn": "flat round dense",
	}
}

# Declare Dark Theme/Mode
dark_theme = ui.dark_mode()

# Create UI Elements
with ui.column(align_items="center").classes("w-full"):
	ui.html("<center><h3>Random Password Generator</h3></center>")
	with ui.card(align_items="center").classes("min-w-[34%] md:w-1/3 rounded-3xl"):
		with ui.tabs().classes("w-full flex").props(ui_appearance['props']['ui_tabs']) as tabs:
			tab_1 = ui.tab("Generate Random Password").classes(ui_appearance['class']['tab'])
			tab_2 = ui.tab("Secure Password Guidelines").classes(ui_appearance['class']['tab'])

		with ui.tab_panels(tabs, value=tab_1).classes("w-full"):
			with ui.tab_panel(tab_1).classes(ui_appearance['class']['tab_panel']):
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
						.props(ui_appearance['props']['tert_btn']) \
						.tooltip("Randomise password length.")

				ngc.slider_passwd_len = ui.slider(
					min=default_values['min_passwd_len'],
					max=default_values['max_passwd_len'],
					value=default_values['min_passwd_len'],
					on_change=lambda: ngc.chk_passlen_slider_val(),
				) \
					.props("label-always id=slider_passwd_len").classes("w-[97%]")

				with ui.row(align_items="center") \
					.classes(ui_appearance['class']['warning_box']) as warning_box: #bg-amber-50
					ui.icon(name="warning", color="warning", size="lg")

					with ui.column().classes("gap-1"):
						ui.label("Password length might be too long!").classes(ui_appearance['class']['warning_heading'])
						ui.label("Old systems may not support this length.").classes(ui_appearance['class']['warning_text'])

				warning_box.bind_visibility_from(
					target_object=ngc.slider_passwd_len,
					target_name='value',
					backward=lambda v: v > default_values['safe_passwd_len'],
				)

				with ui.card(align_items="center") \
					.classes(ui_appearance['class']['params_card']):
					with ui.row(align_items="center").classes("w-full gap-2"):
						ui.label("Valid Characters")
						ui.space()
						ui.button(
							color="flat", icon=f"sym_o_{icons['reset_settings']}",
							on_click=lambda: ngc.reset_all_sliders()
						) \
							.props(ui_appearance['props']['tert_btn']) \
							.tooltip("Reset all parameters below.")
						ui.button(
							color="flat", icon=f"sym_o_{choice(icons['randomiser_icons'])}",
							on_click=lambda: ngc.rndmz_all_sliders()
						) \
							.props(ui_appearance['props']['tert_btn']) \
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
								.props(ui_appearance['props']['tert_btn']) \
								.tooltip(param_sliders[k]['rndmz_btn_tip'])

						ngc.param_input_sliders.update({k:
							ui.slider(
								min=param_sliders[k]['min_val'],
								max=param_sliders[k]['max_val'],
								value=param_sliders[k]['min_val']
							).props(f"label-always id={k}").classes("w-[97%]")
						})

				with ui.row(align_items="center", wrap=False).classes("w-full gap-2"):
					ui.button(text="Generate", on_click=lambda: ngc.show_password(passwd_text)) \
						.props(ui_appearance['props']['generate_btn'])

					passwd_text = ui.input(placeholder="Your Randomly Generated Password").classes("w-full") \
						.props(ui_appearance['props']['input'])

					ui.button(
						color="flat", icon=f"sym_o_{icons['content_copy']}",
						on_click=lambda: ngc.copy_to_clipboard(passwd_text.value),
					).props(ui_appearance['props']['copy_btn']).tooltip("Copy")

			with ui.tab_panel(tab_2).classes(ui_appearance['class']['tab_panel'] + "max-h-[75vh]"):
				with ui.expansion("Creating Secure Password", icon=f"sym_o_{icons['password']}").classes("w-full"):
					ui.markdown(ngc.load_markdown(content_paths['create_passwd']))

				with ui.expansion("Creating Secure Password", icon=f"sym_o_{icons['privacy_tip']}").classes("w-full"):
					ui.markdown(ngc.load_markdown(content_paths['maintain_passwd']))

with ui.footer().classes(ui_appearance['class']['footer']):
	ui.switch(
		"Dark Mode", value=False,
		on_change=lambda e: dark_theme.enable() if e.value else dark_theme.disable()
	).props("color=grey-9")

	ui.space()
	ui.markdown(f"Made by **{author_details['name']}**")
	ui.space()

	with ui.row(align_items="center").classes("gap-1 p-0 pr-2"):
		ui.label("Source code:")
		# GitHub Link + Icon
		with ui.link(target=f"{author_details['links']['repository']['GitHub']}", new_tab=True) \
			.classes(ui_appearance['class']['link']):
			ui.html(f"<img src='{icons['github']}' class='{ui_appearance['class']['footer_icons']}'/>")
			ui.label("GitHub")
		# Separator
		ui.label("│")
		# GitLab Link + Icon
		with ui.link(target=f"{author_details['links']['repository']['GitLab']}", new_tab=True) \
			.classes(ui_appearance['class']['link']):
			ui.html(f"<img src='{icons['gitlab']}' class='{ui_appearance['class']['footer_icons']}'/>")
			ui.label("GitLab")

# Run the app
ui.run(native=False) # True = native app; False = webapp