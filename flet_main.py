import flet as ft

from src.defined import *

page_components: list[ft.Control] = []

# ==== DEBUGGING ====
window_size_label = ft.Text()
page_components.append(window_size_label)

def update_size(e: ft.PageResizeEvent | ft.Page):
	window_size_label.value = f"Width = {e.width} | Height = {e.height} | W/H = {e.width / e.height}"

flex_row: ft.ResponsiveRow = ft.ResponsiveRow(
	alignment=ft.MainAxisAlignment.CENTER,
	controls=[ft.Card(
		col={
			ft.ResponsiveRowBreakpoint.SM: 12,
			ft.ResponsiveRowBreakpoint.MD: 6,
			ft.ResponsiveRowBreakpoint.XXL: 4,
		},
		bgcolor=ft.Colors.LIGHT_BLUE_100,
		content=ft.Text("Should be in the MIDDLE"),
	)]
)
page_components.append(flex_row)
# == END DEBUGGING ==

app_title: str = "Random Password Genrator"
heading: ft.Text = ft.Text(value=app_title, theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
page_components.append(heading)


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
	update_size(page)
	page.on_resize = update_size
	# == END DEBUGGING ==

	page.add(*page_components)

if __name__ == "__main__":
	ft.run(main)