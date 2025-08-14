import sys

from PySide6 import QtCore, QtWidgets


class QIntSlider(QtWidgets.QWidget):

    def __init__(
            self,
            parent: QtWidgets.QWidget | None = None,
            f: QtCore.Qt.WindowType = QtCore.Qt.Widget # type: ignore
        ) -> None:
        super().__init__(parent, f)

        self.spinbox = QtWidgets.QSpinBox()
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.slider)
        self.hbox.addWidget(self.spinbox)

        self.slider.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.slider.setValue)
        self.setLayout(self.hbox)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.resize(600, 500)

    vbox = QtWidgets.QVBoxLayout()

    intslider = QIntSlider()

    vbox.addWidget(intslider)

    window.setLayout(vbox)
    window.show()

    sys.exit(app.exec())
