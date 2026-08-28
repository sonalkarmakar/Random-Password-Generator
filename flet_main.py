from pathlib import Path
from random import randint

import flet as ft

import ui_controls.fl_controls as ui
from src.defined import *

#-----------------------#
# VARIABLE DECLARATIONS #
#-----------------------#
# Minimum Window Dimensions
min_window_width: int = 520
min_window_height: int = 780
# Components to render
page_components: list[ft.Control] = []
# Password Generator Tab Controls
passgen_tab_ctrl_list: list[ft.Control] = []
# Guidelines Tab Controls
gdlns_tab_ctrl_list: list[ft.Control] = []
# Slider Label Text Theme
sldr_lbl_txt_thm: ft.TextThemeStyle = ft.TextThemeStyle.BODY_MEDIUM

#-----------------------#
# APP TITLE AND HEADING #
#-----------------------#
app_title: str = "Random Password Genrator"
heading: ft.Text = ft.Text(value=app_title, theme_style=ft.TextThemeStyle.HEADLINE_LARGE)

#--------------------------------#
# PASSWORD GENERATOR TAB CONTENT #
#--------------------------------#
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
		variant=ft.CardVariant.OUTLINED, bgcolor=ft.Colors.TERTIARY_CONTAINER, content=ft.Container(
			padding=5, content=ft.Row(
				intrinsic_height=True, spacing=0, controls=[
					ft.Container(aspect_ratio=1.0, content=ft.Icon(
						ft.Icons.WARNING, size=40, color=ft.Colors.TERTIARY),
					),
					ft.VerticalDivider(color=ft.Colors.TERTIARY, thickness=2),
					ft.Column(
						expand=True, spacing=5, controls=[
							ft.Text(
								"Password length might be too long!",
								weight=ft.FontWeight.BOLD, color=ft.Colors.ON_TERTIARY_CONTAINER
							),
							ft.Text(
								"Old systems may not support this length.", color=ft.Colors.ON_TERTIARY
							),
						]
					),
				]
			)
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


#--------------------#
# PARAMETERS SECTION #
#--------------------#
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
# Looping through defined parameters
for k, v in param_sliders.items(): # defines all Parameter Controls
	# Shows Parameter Slider value
	param_sldr_val: ft.Text = ft.Text(theme_style=sldr_lbl_txt_thm)
	# Parameter Slider
	param_sldr: ft.Slider = ft.Slider(
		key=k, min=int(v['min_val']), max=int(v['max_val']),
		value=int(v['min_val']), divisions=(int(v['max_val']) - int(v['min_val'])),
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
				ft.Markdown(value=str(v['label']), expand=True,),
				param_sldr_val,
				ft.IconButton(
					icon=ft.Icons.CASINO_OUTLINED, padding=0,
					tooltip=f"{v['rndmz_btn_tip']}",
					on_click=lambda e, v_=v, lbl=param_sldr_val, s=param_sldr: [
						ui.update_sldr(lbl, s, randint(int(v_['min_val']), int(v_['max_val']))),
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


#----------------#
# OUTPUT SECTION #
#----------------#
# Show Generated Password
passwd_output: ft.TextField = ft.TextField(
	hint_text="Your Randomly Generated Password", text_align=ft.TextAlign.CENTER,
	expand=True, border_radius=200, border_color=ft.Colors.ON_PRIMARY_CONTAINER,
)
# Password Generator Button
passgen_btn: ft.FilledButton = ft.FilledButton(
	on_click=lambda e: ui.show_password(
		passwd_output,
		int(passlen_sldr.value) if passlen_sldr.value is not None else default_values['min_passwd_len']
	),
	content="Generate", style=ft.ButtonStyle(
		text_style=ft.TextStyle(size=16), padding=ft.Padding.symmetric(horizontal=16)
	),
)
# Password Copy Button
passwd_copy_btn: ft.IconButton = ft.IconButton(
	tooltip="Copy password",
	padding=0, icon=ft.Icons.CONTENT_COPY_OUTLINED,
	on_click=lambda e: e.page.run_task(ui.copy_to_clipboard, passwd_output.value),
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


#------------------------#
# GUIDELINES TAB CONTENT #
#------------------------#
gdlns_exp_lst: ft.ExpansionPanelList = ft.ExpansionPanelList(
	divider_color=ft.Colors.INVERSE_PRIMARY, expanded_header_padding=ft.Padding.symmetric(horizontal=15),
	controls=[
		ft.ExpansionPanel(
			can_tap_header=True, header=ft.Row(
				intrinsic_height=True, controls=[
					ft.Icon(ft.Icons.PASSWORD_OUTLINED), ft.Text("Creating a Secure Password", expand=True)
				]
			),
			content=ft.Container(
				padding=ft.Padding.all(10),
				content=ft.Markdown(
					ui.load_markdown(f"{Path(__file__).resolve().parent}/{content_paths['create_passwd']}")
				),
			)
		),
		ft.ExpansionPanel(
			can_tap_header=True, header=ft.Row(
				intrinsic_height=True, controls=[
					ft.Icon(ft.Icons.PRIVACY_TIP_OUTLINED), ft.Text("Maintaining Password Security", expand=True),
				]
			),
			content=ft.Container(
				padding=ft.Padding.all(10),
				content=ft.Markdown(
					ui.load_markdown(f"{Path(__file__).resolve().parent}/{content_paths['maintain_passwd']}")
				),
			)
		),
	]
)
# Guidelines Expansion Panel Container
gdlns_exp_cont: ft.Container = ft.Container(
	padding=ft.Padding.all(15),
	content=gdlns_exp_lst,
)
# Guidelines Tab Controls
gdlns_tab_ctrl_list.append(gdlns_exp_cont)
# Guidelines Tab Column
gdlns_tab_col: ft.Column = ft.Column(controls=gdlns_tab_ctrl_list)


#-----------------#
# TAB DEFINITIONS #
#-----------------#
# Password Generator Tab Column
passgen_tab_col: ft.Column = ft.Column(spacing=0, controls=passgen_tab_ctrl_list)
# Password Generator Tab Title
passgen_tab_title: str = "Generate Random Password"
passgen_panel_title: ft.Text = ft.Text("Generate a Random Password", theme_style=ft.TextThemeStyle.TITLE_LARGE)
# Guidelines Tab Title
gdlns_tab_title: str = "Secure Password Guidelines"
gdlns_panel_title: ft.Text = ft.Text("Guidelines for a Secure Password")

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

#---------------------#
# MAIN CONTENT LAYOUT #
#---------------------#
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
		bgcolor=ft.Colors.INVERSE_PRIMARY, content=main_panel_tabs,
		clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
	)]
)

# Main Content Container
main_cont: ft.Container = ft.Container(
	padding=0, expand=True, alignment=ft.Alignment.TOP_CENTER,
	content=ft.Column(
		spacing=0, alignment=ft.MainAxisAlignment.START,
		horizontal_alignment=ft.CrossAxisAlignment.CENTER,
		controls=[heading, main_panel], scroll=ft.ScrollMode.AUTO
	),
)
page_components.append(main_cont)


#----------------------------#
# FOOTER LAYOUT & DEFINITION #
#----------------------------#
# Text Label Themes
footer_lbl_size: ft.TextThemeStyle = ft.TextThemeStyle.LABEL_MEDIUM
lnk_btn_style: ft.ButtonStyle = ft.ButtonStyle(padding=0, visual_density=ft.VisualDensity.COMPACT)

# Dark Mode Toggle Button
dark_mode_togg: ft.Switch = ft.Switch(label="Dark Mode", expand=True)

# Author's Name
author_credit: ft.Row = ft.Row(
	alignment=ft.MainAxisAlignment.CENTER,
	expand=True, spacing=0, wrap=True, controls=[
		ft.Text(value="Made by ", theme_style=footer_lbl_size),
		ft.Text(value=f"{author_details['name']}", theme_style=footer_lbl_size, weight=ft.FontWeight.BOLD)
	]
)
# Links to Repositories
repositories: ft.Row = ft.Row(
	wrap=True, expand=True, vertical_alignment=ft.CrossAxisAlignment.CENTER,
	spacing=0, run_spacing=0, run_alignment=ft.MainAxisAlignment.END,
	alignment=ft.MainAxisAlignment.END, controls=[
		ft.Container(
			padding=ft.Padding(top=10, right=10), # Counters extra padding of TextButton
			content=ft.Text(value="Source code:", theme_style=footer_lbl_size),
		),
		ft.Row(
			wrap=False, spacing=0, tight=True, controls=[
				ft.TextButton(
					content=ft.Text(
						value="GitHub", color=ft.Colors.PRIMARY,
						theme_style=ft.TextThemeStyle.LABEL_MEDIUM
					),
					url=author_details['links']['repository']['GitHub'],
					style=lnk_btn_style,
				),
				ft.Text(value="|", theme_style=footer_lbl_size),
				ft.TextButton(
					content=ft.Text(
						value="GitLab", color=ft.Colors.PRIMARY,
						theme_style=ft.TextThemeStyle.LABEL_MEDIUM
					),
					url=author_details['links']['repository']['GitLab'],
					style=lnk_btn_style,
				),
			]
		),
	]
)

# Creating the Footer Row
footer: ft.Container = ft.Container(
	alignment=ft.Alignment.CENTER,
	bgcolor=ft.Colors.ON_INVERSE_SURFACE, content=ft.Row(
		alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
		controls=[dark_mode_togg, author_credit, repositories],
	)
)
page_components.append(footer)


#------------------------#
# MAIN FUNCTION FOR FLET #
#------------------------#
async def main(page: ft.Page):
	# Setting App Window Size
	page.window.height = min_window_height
	page.window.width = min_window_width
	# Extra offsets counter Flet's bug allowing sizes smaller than defined minimum
	page.window.min_height = min_window_height + 99
	page.window.min_width = min_window_width + 52

	# Light Theme definition
	page.theme = ft.Theme(
		color_scheme=ft.ColorScheme(
			tertiary=ft.Colors.AMBER_600, # warning icon
			on_tertiary=ft.Colors.YELLOW_900, # warning text
			tertiary_container=ft.Colors.YELLOW_100, # warning panel
			on_tertiary_container=ft.Colors.DEEP_ORANGE_900, # warning heading
		)
	)
	# Dark Theme definition
	page.dark_theme = ft.Theme(
		color_scheme=ft.ColorScheme(
			tertiary=ft.Colors.AMBER_50, # warning icon
			on_tertiary=ft.Colors.ORANGE_900, # warning text
			tertiary_container=ft.Colors.AMBER, # warning panel
			on_tertiary_container=ft.Colors.DEEP_ORANGE_900, # warning heading
		)
	)

	# Layout Configuration
	page.padding = 0 # Makes the page more compact
	page.title = app_title
	page.theme_mode = ft.ThemeMode.LIGHT # Initial theme on launch
	page.vertical_alignment = ft.MainAxisAlignment.START # Content renders from window top edge
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER # Content renders vertically centred
	# Function call for theme change
	dark_mode_togg.on_change = lambda e: ui.toggle_theme(page, e.control.value)

	# Adding all conetnts to render
	page.add(
		ft.Column(
			spacing=0, expand=True, controls=page_components,
			horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
			alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
		)
	)

if __name__ == "__main__":
	# Comment below suppresses linter's whining
	_ = ft.run(main) # pyright: ignore[reportUnknownMemberType]