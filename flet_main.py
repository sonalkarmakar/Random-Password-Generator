from random import randint

import flet as ft

import ui_controls.fl_controls as ui
from src.defined import *

# Components to render
page_components: list[ft.Control] = []
# Password Generator Tab Controls
passgen_tab_ctrl_list: list[ft.Control] = []
# Guidelines Tab Controls
gdlns_tab_ctrl_list: list[ft.Control] = []

sldr_lbl_txt_thm: ft.TextThemeStyle = ft.TextThemeStyle.BODY_MEDIUM


# App Title and Heading
app_title: str = "Random Password Genrator"
heading: ft.Text = ft.Text(value=app_title, theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
page_components.append(heading)


# Password Generator Tab Content
# Password Length section
# Slider Label
passlen_sldr_lbl: ft.Text = ft.Text("Password Length", theme_style=sldr_lbl_txt_thm, expand=True)
# Password Length value
passlen_sldr_val: ft.Text = ft.Text(theme_style=sldr_lbl_txt_thm)
# Password Length Warning
warning_panel: ft.Container = ft.Container(
	visible=False, alignment=ft.Alignment.CENTER,
	padding=ft.Padding.symmetric(horizontal=10, vertical=0),
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
	on_change=lambda e: [
		ui.update_sldr(passlen_sldr_val, e.control, None, warning_panel, True),
		ui.chk_passlen_sldr(e.control),
	],
)
# Initiate with Minumum Slider Value
ui.update_sldr(label=passlen_sldr_val, slider=passlen_sldr)

# Password Length Randomiser Button
passlen_rndmz_btn: ft.IconButton = ft.IconButton(
	icon=ft.Icons.CASINO_OUTLINED, padding=0, tooltip="Randomise password length.",
	on_click=lambda e: [
		ui.update_sldr(
			panel=warning_panel, is_passlen=True,
			label=passlen_sldr_val, slider=passlen_sldr,
			value=randint(default_values['min_passwd_len'], default_values['safe_passwd_len']),
		),
		ui.chk_passlen_sldr(passlen_sldr),
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
passgen_tab_ctrl_list.append(passlen_col)


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
							on_click=lambda e: ui.reset_all_sldrs(),
						),
						ft.IconButton(
							icon=ft.Icons.CASINO_OUTLINED, padding=0,
							tooltip="Randomise number of all character types.",
							on_click=lambda e: [
								ui.rndmz_all_sldrs(),
								ui.set_passlen_sldr(passlen_sldr, passlen_sldr_val, warning_panel),
							],
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
		key=k, min=v['min_val'], max=v['max_val'],
		value=v['min_val'], divisions=(v['max_val'] - v['min_val']),
		on_change=lambda e, lbl=param_sldr_val: [
			ui.update_sldr(label=lbl, slider=e.control),
			ui.set_passlen_sldr(passlen_sldr, passlen_sldr_val, warning_panel),
		]
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
						ui.update_sldr(lbl, s, randint(v_['min_val'], v_['max_val'])),
						ui.set_passlen_sldr(passlen_sldr, passlen_sldr_val, warning_panel),
					]
				),
			]
		)
	)
	# Storing Sliders to fetch their values later
	ui.param_input_sldrs.update({k: param_sldr})
	ui.param_sldr_labels.update({k: param_sldr_val})
	# Initiate with Minimum Slider Value
	ui.update_sldr(label=param_sldr_val, slider=param_sldr)
	# Individual Parameter Container
	param_sldr_cont: ft.Container = ft.Container(
			padding=0, alignment=ft.Alignment.CENTER,
			content=ft.Column(spacing=0, controls=[param_lbl_cont, param_sldr]
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
passgen_tab_ctrl_list.append(params_panel)


# Output Section
# Show Generated Password
passwd_output: ft.TextField = ft.TextField(
	hint_text="Your Randomly Generated Password", expand=True,
	border_radius=200, text_align=ft.TextAlign.CENTER,
)
# Password Generator Button
passgen_btn: ft.FilledButton = ft.FilledButton(
	on_click=lambda e: ui.show_password(
		passwd_output, int(passlen_sldr.value) if passlen_sldr.value is not None else default_values['min_passwd_len']
	),
	content="Generate", style=ft.ButtonStyle(
		text_style=ft.TextStyle(size=16), padding=ft.Padding.symmetric(horizontal=16)
	)
)
# Password Copy Button
passwd_copy_btn: ft.IconButton = ft.IconButton(
	padding=0, icon=ft.Icons.CONTENT_COPY_OUTLINED,
	tooltip="Copy password"
)
# Container for getting output
output_cont: ft.Container = ft.Container(
	padding=ft.Padding(left=15, right=15, bottom=15), alignment=ft.Alignment.CENTER,
	content=ft.Row(
		intrinsic_height=True, alignment=ft.MainAxisAlignment.SPACE_EVENLY,
		vertical_alignment=ft.CrossAxisAlignment.STRETCH,
		controls=[passgen_btn, passwd_output, passwd_copy_btn]
	)
)
passgen_tab_ctrl_list.append(output_cont)


# Password Generator Tab Column
passgen_tab_col: ft.Column = ft.Column(spacing=0, controls=passgen_tab_ctrl_list)
# Password Generator Tab Title
passgen_tab_title: str = "Generate Random Password"
passgen_panel_title: ft.Text = ft.Text("Generate a Random Password", theme_style=ft.TextThemeStyle.TITLE_LARGE)


# Guidelines Tab Content
gdlns_tab_title: str = "Secure Password Guidelines"
gdlns_panel_title: ft.Text = ft.Text("Guidelines for a Secure Password")
gdlns_tab_ctrl_list.append(gdlns_panel_title)
# Guidelines Tab Column
gdlns_tab_col: ft.Column = ft.Column(controls=gdlns_tab_ctrl_list)


# Bar for Fake Tabs
fake_tab_bar: ft.TabBar = ft.TabBar(
	scrollable=False, divider_color=ft.Colors.TRANSPARENT, indicator_size=ft.TabBarIndicatorSize.TAB,
	tab_alignment=ft.TabAlignment.FILL, tabs=[
		ft.Tab(label=ft.Text(passgen_tab_title, no_wrap=True)),
		ft.Tab(label=ft.Text(gdlns_tab_title, no_wrap=True)),
	]
)

# Column for each Panel Tab
tab_panels_col: ft.Column = ft.Column(
	spacing=0, controls=[passgen_tab_col, gdlns_tab_col],
)

# Set Default Tab
passgen_tab_col.visible = True
gdlns_tab_col.visible = False

# Render Tabs inside Main Panel
main_panel_tabs: ft.Tabs = ft.Tabs(
	length=2, selected_index=0,
	on_change=lambda e: ui.change_tab([passgen_tab_col, gdlns_tab_col], e.control.selected_index),
	content=ft.Column(
		spacing=0, controls=[fake_tab_bar, tab_panels_col],
	),
)

# Main Panel
main_panel: ft.ResponsiveRow = ft.ResponsiveRow(
	alignment=ft.MainAxisAlignment.CENTER,
	controls=[ft.Card(
		col={
			ft.ResponsiveRowBreakpoint.SM: 12,
			ft.ResponsiveRowBreakpoint.MD: 8,
			ft.ResponsiveRowBreakpoint.LG: 6,
			ft.ResponsiveRowBreakpoint.XXL: 4,
		},
		bgcolor=ft.Colors.LIGHT_BLUE_50, content=main_panel_tabs,
		clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
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