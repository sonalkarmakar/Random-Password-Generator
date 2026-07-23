import flet as ft

app_title = "Random Password Generator"

heading = ft.Text("Random Password Generator", theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
footer = ft.BottomAppBar(
	content=ft.Switch(label="Dark Mode"),
	padding=5
)

page_components = [heading, ]

def main(page: ft.Page):
	page.title = app_title
	page.bottom_appbar = footer
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

	page.add(*page_components)

if __name__ == "__main__":
	ft.run(main)