
from pathlib import Path

from delegate.icon_list_delegate import IconListDelegate
from lib.functions import load_json_data
from models.icon_item_model import IconItemModel
from models.icon_list_model import IconListModel
from PySide6 import QtCore, QtWidgets
from ui.centralwidget_ui import Ui_Form

DATA_DIR = Path(__file__).parent.with_name("data")

class Centralwidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.model = IconListModel()
        self.delegate = IconListDelegate(parent=self.listView)
        self.listView.setItemDelegate(self.delegate)

        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setUniformItemSizes(True)
        self.listView.setViewMode(QtWidgets.QListView.IconMode)
        self.listView.setSpacing(10)
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setMovement(QtWidgets.QListView.Static)
        self.listView.setWrapping(True)
        self.listView.setWordWrap(True)
        self.listView.setMouseTracking(True)
        self.listView.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listView.setDragEnabled(False)
        self.listView.setAcceptDrops(False)
        self.listView.setDropIndicatorShown(False)
        self.listView.setAlternatingRowColors(True)

        self.load_data()
        self.listView.setModel(self.model)
        self.listView.setCurrentIndex(self.model.index(0, 0))
        self.listView.clicked.connect(self.print_current_item)


    def load_data(self) -> None:
        items = []
        for data in load_json_data():
            items.append(IconItemModel.from_json(data, base_dir=DATA_DIR))
        self.model.set_items(items)

    def print_current_item(self, index: QtCore.QModelIndex) -> None:
        item = self.model.data(index, QtCore.Qt.ItemDataRole.UserRole)
        print(item)
