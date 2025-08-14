import sys

if __name__ == "__main__":
    from PySide6 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    windwo = QtWidgets.QWidget()
    windwo.resize(600, 500)


    vbox = QtWidgets.QVBoxLayout()

    lineedit = QtWidgets.QLineEdit("Sample")
    pushbutton = QtWidgets.QPushButton("Show Text")
    pushbutton.setStyleSheet("""
QPushButton {
    color: #f5f5f5;
    background-color: #ea4c10;
    height: 100px;
    border-style: solid;
    border-color: #381f29;
    border-width: 2px;
    border-radius: 9px;
}

QPushButton:hover {
    background-color: #504cb3;
}

QPushButton:pressed {
    background-color: #4cea59;
}
""")

    vbox.addWidget(lineedit)
    vbox.addWidget(pushbutton)

    windwo.setLayout(vbox)

    windwo.show()

    sys.exit(app.exec())
