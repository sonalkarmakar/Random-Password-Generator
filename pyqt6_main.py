import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget  #, QWidget
from PyQt6.uic.load_ui import loadUi


class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		loadUi("ui/main_window.ui", self)
		self.CreatePasswdScrollArea.setVisible(self.CreatePasswdHeaderButton.isChecked())
		self.MaintPasswdScrollArea.setVisible(self.MaintPasswdHeaderButton.isChecked())


if __name__ == "__main__":
	app = QApplication(sys.argv)

	try:
		with open("assets/styles.qss", "r") as f:
			app.setStyleSheet(f.read())
	except FileNotFoundError:
		print("Style sheet not found! Running with default theme.")

	window = MainWindow()
	window.show()

	app.exec()