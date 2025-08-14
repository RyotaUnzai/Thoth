
import sys
from typing import TypedDict

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPaintEvent


class SliderDeaults(TypedDict):
    value: int 
    indicatorSize: int 
    progressWidth: int 
    minimum: int
    maximum: int
    fontSize: int 
    fontFamily: str
    fontColor: QtGui.QColor
    backgroundColor: QtGui.QColor


class QCircularSlider(QtWidgets.QWidget):
    value: int
    indicatorSize: int
    progressWidth: int
    minimum: int
    maximum: int 
    fontSize: int
    fontFamily: str
    fontColor: QtGui.QColor
    backgroundColor: QtGui.QColor

    DEFAULTS: SliderDeaults = {
        "value": 0,
        "indicatorSize": 20,
        "progressWidth": 10,
        "minimum":  0,
        "maximum": 100,
        "fontSize": 12,
        "fontFamily": "Segoe UI",
        "fontColor": QtGui.QColor("#FFF"),
        "backgroundColor": QtGui.QColor("44475a")
    }

    valueChanged = QtCore.Signal(int)

    @staticmethod
    def _generate_property(name: str):
        def getter(self):
            return getattr(self, f"_{name}")
        
        def setter(self, value):
            setattr(self, f"_{name}", value)

        return property(getter, setter)

    def __init__(self, parent=None):
        super().__init__(parent)

        for key, val in self.DEFAULTS.items():
            setattr(self, f"_{key}", val)
        for key in self.DEFAULTS.keys():
            if not hasattr(self.__class__, key):
                setattr(self.__class__, key, self._generate_property(key))

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
        pen = QtGui.QPen(self.fontColor, self.progressWidth, QtCore.Qt.PenStyle.SolidLine)
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
        pen = QtGui.QPen(self.backgroundColor, self.progressWidth, QtCore.Qt.PenStyle.SolidLine)
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
