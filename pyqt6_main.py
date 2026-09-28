import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow  #, QWidget
from PyQt6.uic.load_ui import loadUi

from src.defined import content_paths


class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		loadUi("ui/main_window.ui", self)

		self.CreatePasswdTextBrowser.setSource(QUrl.fromLocalFile(content_paths["create_passwd"]))
		self.MaintPasswdTextBrowser.setSource(QUrl.fromLocalFile(content_paths["maintain_passwd"]))

		self.guideline_sections = (
			(self.CreatePasswdHeaderButton, self.CreatePasswdWidget, self.CreatePasswdTextBrowser),
			(self.MaintPasswdHeaderButton, self.MaintPasswdWidget, self.MaintPasswdTextBrowser),
		)
		for button, _, browser in self.guideline_sections:
			browser.setVisible(button.isChecked()) # start collapsed unless checked
			button.toggled.connect(self.update_guideline_stretch)

		self.update_guideline_stretch()

	def update_guideline_stretch(self) -> None:
		for button, section, _ in self.guideline_sections:
			policy = section.sizePolicy()
			policy.setVerticalStretch(1 if button.isChecked() else 0)
			section.setSizePolicy(policy)

def main():
	app = QApplication(sys.argv)

	try:
		with open("assets/styles.qss", "r") as f:
			app.setStyleSheet(f.read())
	except FileNotFoundError:
		print("Style sheet not found! Running with default theme.")

	window = MainWindow()
	window.show()

	app.exec()

if __name__ == "__main__":
	main()