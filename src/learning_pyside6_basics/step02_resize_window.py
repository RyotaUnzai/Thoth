import sys

if __name__ == "__main__":
    from PySide6 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    mainwindow = QtWidgets.QMainWindow()
    mainwindow.resize(600, 500)

    mainwindow.show()

    sys.exit(app.exec_())
