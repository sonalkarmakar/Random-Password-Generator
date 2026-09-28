import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow  #, QWidget
from PyQt6.uic.load_ui import loadUi

from src.defined import content_paths


class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		loadUi("ui/main_window.ui", self)

		self.CreatePasswdTextBrowser.setVisible(self.CreatePasswdHeaderButton.isChecked())
		self.CreatePasswdTextBrowser.setSource(QUrl.fromLocalFile(content_paths["create_passwd"]))

		self.MaintPasswdTextBrowser.setVisible(self.MaintPasswdHeaderButton.isChecked())
		self.MaintPasswdTextBrowser.setSource(QUrl.fromLocalFile(content_paths["maintain_passwd"]))

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