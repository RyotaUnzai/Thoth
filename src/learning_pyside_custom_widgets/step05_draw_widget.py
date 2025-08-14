
import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPaintEvent


class QCircularSlider(QtWidgets.QWidget):
    value: int = 0
    indicatorSize: int = 20
    progressWidth: int = 10
    minimum: int = 0
    maximum: int = 100
    fontSize: int = 12
    fontFamily: str = "Segoe UI"

    valueChanged = QtCore.Signal(int)


    def __init__(self, parent=None):
        super().__init__(parent)
        self.font_obj = QtGui.QFont(self.fontFamily, self.fontSize)

    @QtCore.Slot(int)
    def _calueChangedCallback(self, value: int):
        return value

    def setValue(self, value: int):
        self.value = value
        self.valueChanged.emit(self.value)
        self.repaint()

    def paintEvent(self, event: QPaintEvent) -> None:
        outLength = min(self.width(), self.height())
        inLength = int(outLength - self.progressWidth - self.indicatorSize / 2)
        margin = int(self.indicatorSize / 2)
        painter = QtGui.QPainter(self)

        self._drawText(painter, inLength)
        self._drawEmptyBar(painter, margin, inLength)

        painter.end()

    def _drawText(self, painter: QtGui.QPainter, inLength: int):
        pen = QtGui.QPen(QtGui.QColor("#FFF"), self.progressWidth, QtCore.Qt.PenStyle.SolidLine)
        painter.setFont(self.font_obj)
        painter.setPen(pen)
        painter.drawText(
            int(self.fontSize / 4),
            0,
            inLength + self.fontSize,
            int(self.height() - self.fontSize / 3),
            QtCore.Qt.AlignmentFlag.AlignCenter, f"{self.value}"
        )

    def _drawEmptyBar(self, painter: QtGui.QPainter, margin: float, inLength: int):
        margin = int(margin)
        pen = QtGui.QPen(QtGui.QColor("#44475a"), self.progressWidth, QtCore.Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        painter.drawArc(margin, margin, inLength, inLength, 0, 360 * 16)


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
