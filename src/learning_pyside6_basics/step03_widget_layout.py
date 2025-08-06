import sys

if __name__ == "__main__":
    from PySide6 import QtWidgets

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

    mainwindow.show()

    sys.exit(app.exec_())
