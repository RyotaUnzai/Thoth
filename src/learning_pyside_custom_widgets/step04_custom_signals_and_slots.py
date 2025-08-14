
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPaintEvent


class QCircularSlider(QtWidgets.QWidget):
    value: int = 0
    valueChanged = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.font_obj = QtGui.QFont()

    @QtCore.Slot(int)
    def _calueChangedCallback(self, value: int):
        return value

    def setValue(self, value: int):
        self.value = value
        self.valueChanged.emit(self.value)
        self.repaint()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtGui.QColor("#FFF"), 5, QtCore.Qt.PenStyle.SolidLine)
        painter.setFont(self.font_obj)
        painter.setPen(pen)
        painter.drawText(20, 0, 200, 50, QtCore.Qt.AlignmentFlag.AlignCenter, f"{self.value}")
        painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.resize(600, 500)

    vbox = QtWidgets.QVBoxLayout()
    circularSlider = QCircularSlider()
    spinbox = QtWidgets.QSpinBox()
    btn = QtWidgets.QPushButton("print")

    def getvalue():
        print(circularSlider.value)
    
    def setValue(value: int):
        circularSlider.setValue(value)
    
    spinbox.valueChanged.connect(setValue)
    
    circularSlider.valueChanged.connect(getvalue)
    btn.clicked.connect(getvalue)
    circularSlider.setValue(40)

    vbox.addWidget(circularSlider)

    vbox.addWidget(spinbox)
    vbox.addWidget(btn)

    window.setLayout(vbox)
    window.show()

    sys.exit(app.exec())
