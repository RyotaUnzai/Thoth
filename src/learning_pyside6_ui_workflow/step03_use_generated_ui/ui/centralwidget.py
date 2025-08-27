from lib.functions import print_text
from lib.widget_circularslider import QCircularSlider
from PySide6 import QtWidgets
from ui.centralwidget_ui import Ui_Form


class Centralwidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: print_text(self.lineEdit.text()))
        self.lineEdit.textChanged.connect(print_text)

        self.circular = QCircularSlider(self)
        self.verticalLayout.addWidget(self.circular)
