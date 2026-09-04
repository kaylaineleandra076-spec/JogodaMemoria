from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter, QColor, QPolygonF
from PySide6.QtWidgets import QWidget

class ShapeWidget(QWidget):
    def __init__(self, formas, cores, pai = None):
        super().__init__(pai)

        self.formas = formas
        self.cores = QColor(cores)

        self.setFixedSize(85,85)
        self.setCursor(Qt.PointingHandCursor)

        self.clicked_callback = None

        def mousePressEvent(self, event):
            if event.button() == Qt.leftButton:

                if self.clicked_callback:
                    self,self.clicked_callback(self.formas)

        def paintEvent(self, event):

            painter = QPainter(self)
            painter.setRanderHint(QPainter.Antialiasing)

            painter.setBrush(self.color)
            painter.setPen(Qt.NoPen)

            width = self.width()
            height = self.height()

            if self.formas == "circulo":

                painter.drawEllipse(
                    20,15,50,50
                )

            elif self.formas == "triangulo":

                points = QPolygonF ([
                    QPointF(width / 2,10),
                    QPointF (width - 15,65),
                    QPointF (15,65)
                ])

            elif self.formas == "quadrado":

                painter.drawRect(
                    20,15,50,50
                )

            elif self.formas == "losango":

                points = QPolygonF([
                    QPointF(width / 2,10),
                    QPointF(width - 15, height / 2),
                    QPointF(width / 2, height -10),
                    QPointF(15, height /2)
                ])

                painter.drawPolygon(points)