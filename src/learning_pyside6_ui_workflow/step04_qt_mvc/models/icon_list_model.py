from typing import Any

from models.icon_item_model import IconItemModel
from PySide6 import QtCore


class IconListModel(QtCore.QAbstractListModel):
    def __init__(self, items: list[IconItemModel] | None = None, parent: Any = None) -> None:
        super().__init__(parent)
        self._items: list[IconItemModel] = items if items is not None else []
        self.currentItem: IconItemModel | None = self._items[0] if self._items else None
        self._count: int = 0

    def set_items(self, value: list[IconItemModel]) -> None:
        self._items = value
        self.layoutChanged.emit()

    def reload(self, path: str = "") -> None:
        self.layoutChanged.emit()

    def rowCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = QtCore.QModelIndex()) -> int:
        return len(self._items)

    def data(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int = QtCore.Qt.DisplayRole) -> Any:
        if not index.isValid() or not (0 <= index.row() < self.rowCount()):
            return None
        item = self._items[index.row()]
        self.currentItem = item
        if role == QtCore.Qt.DisplayRole:
            return getattr(item, "display_name", str(item))
        if role == QtCore.Qt.ItemDataRole.UserRole:
            return item
        return None

    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlags:
        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
