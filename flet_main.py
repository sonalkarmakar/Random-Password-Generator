import flet as ft
import ui_controls.fl_controls as ui

from src.defined import *

# Components to render
page_components: list[ft.Control] = []
# Main Panel Controls
panel_ctrl_list: list[ft.Control] = []

sldr_lbl_txt_thm: ft.TextThemeStyle = ft.TextThemeStyle.BODY_LARGE

# ==== DEBUGGING ====
# window_size_label = ft.Text()
# page_components.append(window_size_label)

# def update_size(e: ft.PageResizeEvent | ft.Page):
# 	window_size_label.value = f"Width = {e.width} | Height = {e.height} | W/H = {e.width / e.height}"
# == END DEBUGGING ==

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
# Randomiser Button
passlen_rndmz_btn: ft.IconButton = ft.IconButton(icon=ft.Icons.CASINO_OUTLINED, padding=0)
# Container with Password Length Label and Randomiser Button
passlen_lbl_cont: ft.Container = ft.Container(
	padding=ft.Padding(left=15, right=15,),
	content=ft.Row(
		intrinsic_height=True,
		controls=[passlen_sldr_lbl, passlen_sldr_val, passlen_rndmz_btn],
	)
)
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
	# active_color=ft.Colors.AMBER,
	# inactive_color=ft.Colors.AMBER_50,
	on_change=lambda e: ui.update_passlen_sldr(label=passlen_sldr_val, panel=warning_panel, event=e),
	divisions=(default_values['max_passwd_len'] - default_values['min_passwd_len']),
)
# Initiate with Minumum Slider Value
ui.update_sldr_lbl(label=passlen_sldr_val, value=f"{passlen_sldr.value}")
# ui.passlen_sldr_warn(warn_msg=warning_panel, slider=passlen_sldr)

# Password Length Container
# passlen_cont: ft.Container = ft.Container(alignment=ft.Alignment.CENTER, content=passlen_col,)

# Password Length section Column
passlen_col: ft.Column = ft.Column(spacing=0, controls=[passlen_lbl_cont, passlen_sldr, warning_panel])
panel_ctrl_list.append(passlen_col)

# Parameters Section
# ==== DEBUGGING ====
# k = "slider_upper_chars"
# v = param_sliders[k]
# == END DEBUGGING ==

# Parameters List
params_list: list[ft.Control] = []

# Parameters Section
for k, v in param_sliders.items():
	# Parameter Label Container
	param_lbl_cont: ft.Container = ft.Container(
		padding=ft.Padding.symmetric(horizontal=15),
		content=ft.Row(
			intrinsic_height=True,
			controls=[
				ft.Markdown(value=v['label'], expand=True),
				ft.Text("<sldr_val>", theme_style=sldr_lbl_txt_thm),
				ft.IconButton(icon=ft.Icons.CASINO_OUTLINED, padding=0)
			]
		)
	)
	# Parameter Slider
	param_sldr: ft.Slider = ft.Slider(
		key=k,
		min=v['min_val'],
		max=v['max_val'],
		value=v['min_val'],
		divisions=(v['max_val'] - v['min_val']),
	)
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
	padding=15, alignment=ft.Alignment.CENTER,
	content=ft.Card(
		variant=ft.CardVariant.OUTLINED,
		content=ft.Column(alignment=ft.MainAxisAlignment.CENTER, controls=params_list)
	)
)
panel_ctrl_list.append(params_panel)

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