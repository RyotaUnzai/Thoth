import sys
from pathlib import Path

from PySide6 import QtCore

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


def on_click() -> None:
    print("ok")


if __name__ == "__main__":
    from PySide6 import QtWidgets
    from PySide6.QtUiTools import QUiLoader

    app = QtWidgets.QApplication(sys.argv)
    loader = QUiLoader()
    path_mainwindow = DIR_UI / "mainwindow.ui"
    path_centralwidget = DIR_UI / "centralwidget.ui"

    mainwindow: QtWidgets.QMainWindow = loader.load(path_mainwindow)
    centralwidget: QtWidgets.QWidget = loader.load(path_centralwidget)
    mainwindow.setCentralWidget(centralwidget)

    push_button = QtWidgets.QPushButton("Button")
    centralwidget.verticalLayout.addWidget(push_button)
    centralwidget.pushButton.clicked.connect(on_click)

    mainwindow.show()

    sys.exit(app.exec())
