import flet as ft
import ui_controls.fl_controls as ui

from src.defined import *

# Components to render
page_components: list[ft.Control] = []

sldr_lbl_txt_thm: ft.TextThemeStyle = ft.TextThemeStyle.BODY_MEDIUM

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
passlen_sldr_lbl: ft.Text = ft.Text("Password Length", theme_style=sldr_lbl_txt_thm)
# Password Length value
passlen_sldr_val: ft.Text = ft.Text(theme_style=sldr_lbl_txt_thm)
# Randomiser Button
passlen_rndmz_btn: ft.IconButton = ft.IconButton(icon=ft.Icons.CASINO_OUTLINED)
# Label + Randomiser Button in a Row
passlen_lbl_cont: ft.Container = ft.Container(padding=ft.Padding(left=15, right=15,),
	content=ft.Row(
		controls=[
			ft.Row(
				expand=True,
				alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
				controls=[passlen_sldr_lbl, passlen_sldr_val],
			),
			passlen_rndmz_btn
		], intrinsic_height=True,
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
	on_change=lambda e: ui.update_passlen_sldr(label=passlen_sldr_val, event=e),
	divisions=(default_values['max_passwd_len'] - default_values['min_passwd_len']),
)
ui.update_sldr_lbl(label=passlen_sldr_val, value=f"{passlen_sldr.value}")
passlen_col: ft.Column = ft.Column(controls=[passlen_lbl_cont, passlen_sldr],)

# Container inside Main Panel
panel_container: ft.Container = ft.Container(alignment=ft.Alignment.CENTER, content=passlen_col,)

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
		content=panel_container,
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
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

	# ==== DEBUGGING ====
	# update_size(page)
	# page.on_resize = update_size
	# == END DEBUGGING ==

	page.add(*page_components)

if __name__ == "__main__":
	ft.run(main)