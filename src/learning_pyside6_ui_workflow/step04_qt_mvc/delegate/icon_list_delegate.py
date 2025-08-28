from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets


class IconListDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent: QtWidgets.QListView | None = None):
        super().__init__(parent)
        self._parent = parent

    def _get_colors(self, option: QtWidgets.QStyleOptionViewItem):
        if option.state & QtWidgets.QStyle.StateFlag.State_Selected:
            return QtGui.QColor("#00E7B8"), QtGui.QColor("#00b8b8")
        elif option.state & QtWidgets.QStyle.StateFlag.State_MouseOver:
            return QtGui.QColor(0, 184, 184, 30), QtGui.QColor("#00b8b8")
        else:
            return QtGui.QColor("#f0f0f0"), QtGui.QColor("#cccccc")

    def _draw_background(self, painter, rect, bg_color, border_color):
        painter.save()
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(bg_color)
        painter.setPen(QtGui.QPen(border_color, 2))
        painter.drawRoundedRect(rect.adjusted(2, 2, -2, -2), 8, 8)
        painter.restore()

    def _draw_icon(self, painter, rect, item):
        if item and getattr(item, "image_url", None) and Path(item.image_url).exists():
            pixmap = QtGui.QPixmap(str(item.image_url))
            icon_size = min(rect.width(), rect.height()) - 32
            pixmap = pixmap.scaled(icon_size, icon_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
            x = rect.x() + (rect.width() - pixmap.width()) // 2
            y = rect.y() + 16
            painter.drawPixmap(x, y, pixmap)
            return y + pixmap.height()
        else:
            return rect.y() + 16

    def _draw_text(self, painter, rect, text, text_y):
        painter.save()
        painter.setPen(QtGui.QPen(QtGui.QColor("#252525")))
        font = QtGui.QFont()
        font.setPixelSize(10)
        painter.setFont(font)
        painter.drawText(rect.x(), text_y, rect.width(), 20, QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop, text)
        painter.restore()

    def paint(self, painter, option, index) -> None:
        model = index.model()
        item = model.data(index, QtCore.Qt.ItemDataRole.UserRole)
        rect = option.rect
        bg_color, border_color = self._get_colors(option)
        self._draw_background(painter, rect, bg_color, border_color)
        text_y = self._draw_icon(painter, rect, item)
        text = getattr(item, "display_name", "")
        self._draw_text(painter, rect, text, text_y)

    def sizeHint(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QSize:
        return QtCore.QSize(100, 100)
