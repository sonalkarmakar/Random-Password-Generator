import flet as ft
from flet.controls.material import slider
import ui_controls.fl_controls as ui

from src.defined import *
from random import randint

# Components to render
page_components: list[ft.Control] = []
# Main Panel Controls
panel_ctrl_list: list[ft.Control] = []

sldr_lbl_txt_thm: ft.TextThemeStyle = ft.TextThemeStyle.BODY_MEDIUM


# App Title and Heading
app_title: str = "Random Password Genrator"
heading: ft.Text = ft.Text(value=app_title, theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
page_components.append(heading)

# Main Panel Tabs

# Tab Panel Title
passgen_title: str = "Generate a Random Password"
tab_panel_title: ft.Text = ft.Text(passgen_title, theme_style=ft.TextThemeStyle.TITLE_LARGE)

# Password Length section
# Slider Label
passlen_sldr_lbl: ft.Text = ft.Text("Password Length", theme_style=sldr_lbl_txt_thm, expand=True)
# Password Length value
passlen_sldr_val: ft.Text = ft.Text(theme_style=sldr_lbl_txt_thm)
# Password Length Warning
warning_panel: ft.Container = ft.Container(
	visible=False, alignment=ft.Alignment.CENTER,
	padding=ft.Padding.symmetric(horizontal=10),
	content=ft.Card(
		variant=ft.CardVariant.OUTLINED,
		bgcolor=ft.Colors.YELLOW_100,
		content=ft.Container(
			padding=5,
			content=ft.Row(intrinsic_height=True, spacing=0, controls=[
				ft.Container(content=ft.Icon(ft.Icons.WARNING, size=40, color=ft.Colors.AMBER_600), aspect_ratio=1.0,),
				ft.VerticalDivider(color=ft.Colors.AMBER_600, thickness=2),
				ft.Column(expand=True, spacing=5, controls=[
					ft.Text("Password length might be too long!", weight=ft.FontWeight.BOLD, color=ft.Colors.DEEP_ORANGE_900),
					ft.Text("Old systems may not support this length.", color=ft.Colors.YELLOW_900),
				]),
			])
		)
	)
)
# Password Length Slider
passlen_sldr: ft.Slider = ft.Slider(
	# label="{value}",
	key="passlen_slider",
	min=default_values['min_passwd_len'],
	max=default_values['max_passwd_len'],
	value=default_values['min_passwd_len'],
	divisions=(default_values['max_passwd_len'] - default_values['min_passwd_len']),
	on_change=lambda e: ui.update_sldr(passlen_sldr_val, e.control, warning_panel, True),
)
# Initiate with Minumum Slider Value
ui.update_sldr_lbl(label=passlen_sldr_val, value=f"{passlen_sldr.value}")

# Password Length Randomiser Button
passlen_rndmz_btn: ft.IconButton = ft.IconButton(
	icon=ft.Icons.CASINO_OUTLINED, padding=0, tooltip="Randomise password length.",
	on_click=lambda e: [
		ui.set_sldr_val(passlen_sldr, randint(default_values['min_passwd_len'], default_values['safe_passwd_len'])),
		ui.update_sldr(passlen_sldr_val, passlen_sldr, warning_panel, True)
	],
)
# Container with Password Length Label and Randomiser Button
passlen_lbl_cont: ft.Container = ft.Container(
	padding=ft.Padding(left=15, right=15,),
	content=ft.Row(
		intrinsic_height=True,
		controls=[passlen_sldr_lbl, passlen_sldr_val, passlen_rndmz_btn],
	)
)

# Password Length section Column
passlen_col: ft.Column = ft.Column(spacing=0, controls=[passlen_lbl_cont, passlen_sldr, warning_panel])
panel_ctrl_list.append(passlen_col)


# Parameters Section
# Parameters List
params_list: list[ft.Control] = [] # list of Controls to render for Parameters Panel

# Parameters Heading
params_list.append(
	ft.Container(
		padding=ft.Padding.symmetric(horizontal=15), alignment=ft.Alignment.CENTER,
		content=ft.Column(
			alignment=ft.MainAxisAlignment.CENTER, spacing=10, controls=[
				ft.Row(
					intrinsic_height=True, spacing=0,
					alignment=ft.MainAxisAlignment.CENTER, controls=[
						ft.Text("Valid Characters", expand=True, theme_style=sldr_lbl_txt_thm),
						ft.IconButton(
							icon=ft.Icons.SETTINGS_BACKUP_RESTORE_OUTLINED,
							padding=0, tooltip="Reset all parameters below.",
						),
						ft.IconButton(
							icon=ft.Icons.CASINO_OUTLINED, padding=0,
							tooltip="Randomise number of all character types.",
						)
					]
				),
				ft.Divider(),
			]
		)
	)
)

for k, v in param_sliders.items(): # defines all Parameter Controls
	# Shows Parameter Slider value
	param_sldr_val: ft.Text = ft.Text(theme_style=sldr_lbl_txt_thm)
	# Parameter Slider
	param_sldr: ft.Slider = ft.Slider(
		key=k,
		min=v['min_val'],
		max=v['max_val'],
		value=v['min_val'],
		divisions=(v['max_val'] - v['min_val']),
		on_change=lambda e, lbl=param_sldr_val: ui.update_sldr(label=lbl, slider=e.control)
	)
	# Parameter Label Container
	param_lbl_cont: ft.Container = ft.Container(
		padding=ft.Padding.symmetric(horizontal=15),
		content=ft.Row(
			intrinsic_height=True, controls=[
				ft.Markdown(value=v['label'], expand=True,),
				param_sldr_val,
				ft.IconButton(
					icon=ft.Icons.CASINO_OUTLINED, padding=0,
					tooltip=f"{v['rndmz_btn_tip']}",
					on_click=lambda e, v_=v, lbl=param_sldr_val, s=param_sldr: [
						ui.set_sldr_val(s, randint(v_['min_val'], v_['max_val'])),
						ui.update_sldr(lbl, s)
					]
				),
			]
		)
	)
	# Storing Sliders to fetch their values later
	ui.param_input_sldrs.update({k: param_sldr})
	# Initiate with Minimum Slider Value
	ui.update_sldr_lbl(label=param_sldr_val, value=f"{param_sldr.value}")
	# Individual Parameter Container
	param_sldr_cont: ft.Container = ft.Container(
		padding=0, alignment=ft.Alignment.CENTER,
		content=ft.Column(
			spacing=0,
			controls=[param_lbl_cont, param_sldr]
		)
	)
	params_list.append(param_sldr_cont)

# Parameters Panel
params_panel: ft.Container = ft.Container(
	padding=10, alignment=ft.Alignment.CENTER,
	content=ft.Card(
		variant=ft.CardVariant.OUTLINED,
		content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, controls=params_list)
	)
)
panel_ctrl_list.append(params_panel)


# Output Section
const_height = 45
# Password Generator Button
passgen_btn: ft.FilledButton = ft.FilledButton(content="Generate Password",)
# Show Generated Password
passwd_output: ft.TextField = ft.TextField(
	hint_text="Your Randomly Generated Password", expand=True,
	border_radius=200, text_align=ft.TextAlign.CENTER,
)
# Password Copy Button
passwd_copy_btn: ft.IconButton = ft.IconButton(
	padding=0, icon=ft.Icons.CONTENT_COPY_OUTLINED,
	tooltip="Copy password"
)
# Container for getting output
output_cont: ft.Container = ft.Container(
	padding=15, alignment=ft.Alignment.CENTER,
	content=ft.Row(
		intrinsic_height=True, alignment=ft.MainAxisAlignment.SPACE_EVENLY,
		vertical_alignment=ft.CrossAxisAlignment.STRETCH,
		controls=[passgen_btn, passwd_output, passwd_copy_btn]
	)
)
panel_ctrl_list.append(output_cont)


# Main Panel Column
panel_col: ft.Column = ft.Column(spacing=0, controls=panel_ctrl_list)
# Main Panel
main_panel: ft.ResponsiveRow = ft.ResponsiveRow(
	alignment=ft.MainAxisAlignment.CENTER,
	controls=[ft.Card(
		col={
			ft.ResponsiveRowBreakpoint.SM: 12,
			ft.ResponsiveRowBreakpoint.MD: 6,
			ft.ResponsiveRowBreakpoint.XXL: 4,
		},
		bgcolor=ft.Colors.LIGHT_BLUE_50,
		content=panel_col,
	)]
)
page_components.append(main_panel)

footer_label_size: ft.TextThemeStyle = ft.TextThemeStyle.LABEL_MEDIUM

dark_mode_togg: ft.Switch = ft.Switch(label="Dark Mode")
author_credit: ft.Text = ft.Text(value=f"Made by {author_details['name']}", theme_style=footer_label_size)
repositories: ft.Text = ft.Text(value="Source code: GitHub | GitLab", theme_style=footer_label_size)

footer: ft.BottomAppBar = ft.BottomAppBar(
	bgcolor=ft.Colors.GREY_200,
	content=ft.Row(
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
		controls=[dark_mode_togg, author_credit, repositories],
	)
)

def main(page: ft.Page):
	page.title = app_title
	page.theme_mode = ft.ThemeMode.LIGHT
	page.bottom_appbar = footer
	page.vertical_alignment = ft.MainAxisAlignment.START
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

	# ==== DEBUGGING ====
	# update_size(page)
	# page.on_resize = update_size
	# == END DEBUGGING ==

	page.add(*page_components)

if __name__ == "__main__":
	ft.run(main)