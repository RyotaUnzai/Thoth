import sys

from PySide6 import QtWidgets
from ui.centralwidget import Centralwidget
from ui.mainwindow import Mainwindow


def run():
    app = QtWidgets.QApplication(sys.argv)

    mainwindow = Mainwindow()
    centralwidget = Centralwidget(parent=mainwindow)

    mainwindow.setCentralWidget(centralwidget)

    mainwindow.show()

    sys.exit(app.exec())
