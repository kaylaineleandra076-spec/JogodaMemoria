import sys
from PySide6.QtWidgets import QApplication

from game import ShapeMatch


app = QApplication(sys.argv)

game = ShapeMatch()
game.show()

sys.exit(app.exec())