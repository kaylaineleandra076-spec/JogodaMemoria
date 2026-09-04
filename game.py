import random

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QMessageBox
)

from shape import ShapeWidget
from Interface import GameInterface

class ShapeMatch(QWidget):
    def __int__(self):
        super().__init__()

        self.setWindowTitle("Shape Match")

        self.setMinimumSize(800,600)

        #status
        self.round = 1 

        self.points = 0 

        self.sequence = []

        self.player_sequence = []

        #formas
        self.shapes = [
            ("circulo","#00d9ff")
            ("triangulo","#9cff9c")
            ("quadrado","#e066ff")
            ("losango","#b60000")
        ]

        #interface

        self.setup_style()

        self.interface = GameInterface(self)

        self.show_start_screen()

        #estilo

        def setup_style(self):

            self.setStyleSheet("""
                QWidget{
                background-color: #00d9ff;
                color: azul;
                font-family: Arial;
            }

            QpushButton{
                background-color: #00cfe8;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 25px;
                font-size: 17px;
                font-weight: bold;
            }

             QPushButton:hover {
                background-color: #00b8cf;}
            
            
            
            
            """)