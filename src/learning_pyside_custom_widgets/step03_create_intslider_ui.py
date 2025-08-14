import sys
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

PATH_FILE = Path(__file__)
CURRENT_DIR = PATH_FILE.parent
DIR_UI = CURRENT_DIR / "ui"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.resize(600, 500)

    vbox = QtWidgets.QVBoxLayout()

    intslider_path = DIR_UI / "intslider.ui"

    loader = QUiLoader()
    intslider = loader.load(intslider_path.as_posix())

    vbox.addWidget(intslider)

    window.setLayout(vbox)
    window.show()

    sys.exit(app.exec())
