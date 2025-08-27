import sys
from pathlib import Path
from typing import Any, Type

from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import loadUiType

PATH_FILE = Path(__file__)
CURRENT_DIR = PATH_FILE.parent
DIR_UI = CURRENT_DIR / "ui"


def load_ui(file_path: Path | str) -> QtCore.QFile:
    if isinstance(file_path, str):
        file_path = Path(file_path)
    ui_file = QtCore.QFile(file_path.as_posix())
    if not ui_file.open(QtCore.QFile.ReadOnly):
        print("Failed to open UI file")
        sys.exit(1)
    return ui_file


def load_ui_type(file_path: Path | str) -> tuple[Type[Any], Type[Any]]:
    if isinstance(file_path, Path):
        file_path = file_path.as_posix()

    return loadUiType(file_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    path_mainwindow = DIR_UI / "mainwindow.ui"
    path_centralwidget = DIR_UI / "centralwidget.ui"

    # --- Define MainWindow Class
    _Mainwindow_base: Type[QtWidgets.QMainWindow]
    _Mainwindow_from, _Mainwindow_base = load_ui_type(path_mainwindow)

    class MainWindow(_Mainwindow_base, _Mainwindow_from):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setupUi(self)

    _Centralwidget_base: Type[QtWidgets.QWidget]
    _Centralwidget_from, _Centralwidget_base = load_ui_type(path_centralwidget)
    # ---

    # --- Define Centralwidget
    class Centralwidget(_Centralwidget_base, _Centralwidget_from):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setupUi(self)

            self.pushButton.clicked.connect(self.on_click)

        def on_click(self):
            print(self.sender().text())

    # ---

    mainwindow = MainWindow()
    centralwidget = Centralwidget(parent=mainwindow)

    mainwindow.setCentralWidget(centralwidget)

    push_button = QtWidgets.QPushButton("Button")
    centralwidget.verticalLayout.addWidget(push_button)

    mainwindow.show()

    sys.exit(app.exec())
