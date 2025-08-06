import sys
from PySide6 import QtWidgets


def show_text(text: str) -> None:
    mbox = QtWidgets.QMessageBox()
    mbox.setWindowTitle("Show Text")
    mbox.setText(text)
    mbox.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainwindow = QtWidgets.QMainWindow()
    mainwindow.resize(600, 500)

    central_widget = QtWidgets.QWidget()
    mainwindow.setCentralWidget(central_widget)

    vbox = QtWidgets.QVBoxLayout()

    lineedit = QtWidgets.QLineEdit("Sample")
    pushbutton = QtWidgets.QPushButton("Show Text")

    vbox.addWidget(lineedit)
    vbox.addWidget(pushbutton)

    central_widget.setLayout(vbox)

    pushbutton.clicked.connect(lambda: show_text(lineedit.text()))

    mainwindow.show()

    sys.exit(app.exec_())
