from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton
)


class GameInterface:

    def __init__(self, window):

        self.window = window

        self.create_interface()

    def create_interface(self):

        self.main_layout = QVBoxLayout(
            self.window
        )

        self.main_layout.setContentsMargins(
            30,25,30,30
        )

        self.main_layout.setSpacing(20)

        self.info_layout = QHBoxLayout()

        self.round_label = QLabel()
        self.points_label = QLabel()
        self.lives_label = QLabel()

        for label in [
            self.round_label,
            self.points_label,
            self.lives_label
        ]:
            label.setStyleSheet("""
                font-size: 20px;
                font-weight: bold;
            """)

        self.info_layout.addWidget(
            self.round_label
        )

        self.info_layout.addWidget(
            self.points_label
        )

        self.info_layout.addWidget(
            self.lives_label
        )

        self.info_layout.addStretch()

        self.main_layout.addLayout(
            self.info_layout
        )


        self.title = QLabel("Formas")

        self.title.setAlignment(
            Qt.AlifnCenter
        )

#titulo
        self.title.setStyleSheet(
            """font-size: 32px;
                font-weight: bold;"""
        )

        self.main_layout.addWidget(
            self.title
        )

        self.content = QWidget()

        self.content_layout = QVBoxLayout(
            self.content
        )

        self.content_layout.seyAlignment(
            Qt.AlignCenter
        )

        self.content_layout.setSpacing(25)

        self.main_layout.addWidget(
            self.content
        )

        self.update_info(
            1,
            0,
            3
        )

    def clear_content(self):

        while self.content_layout.count():
            item = self.content_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

    def update_info(self,round_number, points,lives):

        self.round_label.setText(f"Rodada: {self.round_label}")
        self.points_label.setText(f"Pontos: {self.points_label}")
        self.lives_label.setText(f"Vidas: "+ "❤️" * lives)

    def create_button(self, text):

        button = QPushButton(text)

        button.setFixedWidth(220)

        return button