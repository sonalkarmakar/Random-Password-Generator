import flet as ft

app_title = "Random Password Generator"

heading = ft.Text("Random Password Generator", theme_style=ft.TextThemeStyle.HEADLINE_LARGE)

tab_title = "Genrate Password"
tab_panel_title = ft.Text("Generate a Random Password", theme_style=ft.TextThemeStyle.BODY_LARGE)

main_panel = ft.Container(
	content=tab_panel_title,
	padding=4, bgcolor=ft.Colors.LIGHT_BLUE_50,
	border_radius=10,
	border=ft.Border.all(width=1, color=ft.Colors.BLACK),
	shadow=ft.BoxShadow(color=ft.Colors.GREY_500, blur_radius=2, offset=ft.Offset(x=3, y=3)),
)

dark_mode_switch = ft.Switch(label="Dark Mode")
author_name = ft.Text("Made by Sonal Karmakar", theme_style=ft.TextThemeStyle.LABEL_SMALL)
repository = ft.Text("Source code: GitHub | GitLab", theme_style=ft.TextThemeStyle.LABEL_SMALL)

bottom_row = ft.Row(
	controls=[dark_mode_switch, author_name, repository],
	alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
	intrinsic_height=True,
)

footer = ft.BottomAppBar(
	content=bottom_row,
	padding=5
)

page_components = [heading, main_panel]

def main(page: ft.Page):
	page.title = app_title
	page.theme_mode = ft.ThemeMode.LIGHT
	page.bottom_appbar = footer
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

	page.add(*page_components)

if __name__ == "__main__":
	ft.run(main)