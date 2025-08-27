from PySide6 import QtWidgets
from ui.mainwindow_ui import Ui_MainWindow


class Mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
