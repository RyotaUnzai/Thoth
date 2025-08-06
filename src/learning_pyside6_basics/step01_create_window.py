import sys

if __name__ == "__main__":
    from PySide6 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    mainwindow = QtWidgets.QMainWindow()

    mainwindow.show()

    sys.exit(app.exec_())
