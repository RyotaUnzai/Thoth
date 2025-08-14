
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
    progressColor: QtGui.QColor




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
    progressColor: QtGui.QColor

    DEFAULTS: SliderDeaults = {
        "value": 0,
        "indicatorSize": 20,
        "progressWidth": 10,
        "minimum":  0,
        "maximum": 100,
        "fontSize": 12,
        "fontFamily": "Segoe UI",
        "fontColor": QtGui.QColor("#FFF"),
        "backgroundColor": QtGui.QColor("44475a"),
        "progressColor": QtGui.QColor("#24B626")
    }

    valueChanged = QtCore.Signal(int)

    @staticmethod
    def _make_property(name: str):
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
                setattr(self.__class__, key, self._make_property(key))

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
        circularRadius = outLength - self.indicatorSize
        angle = int(self.value * 360 / self.maximum)

        painter = QtGui.QPainter(self)


        self._drawText(painter, inLength)
        self._drawEmptyBar(painter, margin, inLength)
        self._createProgressBar(
            painter, margin, margin, circularRadius, circularRadius,
            -90 * 16, -angle * 16
        )
    
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

    def _createProgressBar(
            self, painter: QtGui.QPainter,
            x: int, y:int, width: int, height:int,
            startAngle: int, spanAngle: int
        ):
        pen = QtGui.QPen(self.progressColor)
        pen.setCapStyle(QtCore.Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawArc(x, y, width, height, startAngle, spanAngle)


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
