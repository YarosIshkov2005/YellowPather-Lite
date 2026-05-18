# YellowPather Lite File Navigator - File Navigator with open source code.
# Copyright (C) 2026 Yaroslav.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from typing import Any, Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QProgressBar, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QListWidget, QMessageBox

class Frontend:
    """
        The external interface of the application.

        Args:
            parent (Optional[QMainWindow]): The main window of the application.

            app (Any): The main class of the application.
    """
    def __init__(self, parent: Optional[QMainWindow], app: Any) -> None:
        self.parent = parent
        self.app = app

        self.index: int = 0

    def frame_container(self) -> None:
        """
            Configures the layout for arranging interface elements.
        """
        self.central = QWidget()
        self.parent.setCentralWidget(self.central)
        self.main_layout = QVBoxLayout(self.central)

        self.title_layout = QHBoxLayout()
        self.title_layout.setContentsMargins(5, 5, 5, 5)

        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(5, 5, 5, 5)

        self.function_layout = QHBoxLayout()
        self.function_layout.setContentsMargins(5, 5, 5, 5)

        self.central_layout = QHBoxLayout()
        self.central_layout.setContentsMargins(5, 5, 5, 5)

        self.user_layout = QHBoxLayout()
        self.user_layout.setContentsMargins(5, 5, 5, 5)

        self.context_layout = QVBoxLayout()
        self.context_layout.setContentsMargins(5, 5, 5, 5)

    def create_gui(self, title: str) -> None:
        """
            Creates interface elements.
            
            Args:
                title (str): The name of the application.
        """
        self.app_name = QLabel(title, self.parent)
        self.app_name.setStyleSheet("""
            QLabel {
                background-color: #121212;
                border: 2px solid #121212;
                border-color: #121212;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 12pt;
            }
        """)
        self.title_layout.addWidget(
            self.app_name, stretch=0, alignment=Qt.AlignLeft)

        self.close_app_button = QPushButton(self.parent)
        self.close_app_button.setStyleSheet("""
            QPushButton {
                background-color: #121212;
                border: 2px solid #121212;
                border-color: #121212;
                border-radius: 5px;
            }
            QPushButton::hover {
                background-color: #2D2D2D; 
                border-color: #2D2D2D;
            }
        """)
        self.title_layout.addWidget(
            self.close_app_button, stretch=1, alignment=Qt.AlignRight)
        self.close_app_button.setFixedSize(65, 65)
        self.close_app_button.clicked.connect(self.close_app)

        self.app.backend.app_icons.set_button_icon(
            self.close_app_button, "close_icon.png", (65, 65))

        self.path_field = QLineEdit(self.parent)
        self.path_field.setStyleSheet("""
            QLineEdit {
                background-color: #121212;
                border: 2px solid #0000FF;
                border-color: #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QLineEdit::hover {
                border-color: #137ffd;
            }
        """)
        self.top_layout.addWidget(self.path_field, stretch=1)
        self.top_layout.addSpacing(10)

        self.open_button = QPushButton("Open", self.parent)
        self.open_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.open_button.setFixedWidth(70)
        self.open_button.clicked.connect(self.app.scan_input_path)
        self.top_layout.addWidget(self.open_button, stretch=0)
        self.top_layout.addSpacing(10)

        self.clear_button = QPushButton("Clear", self.parent)
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.clear_button.setFixedWidth(70)
        self.clear_button.clicked.connect(lambda: self.path_field.clear())
        self.top_layout.addWidget(self.clear_button, stretch=0)
        self.top_layout.addSpacing(10)

        self.delete_button = QPushButton("Delete", self.parent)
        self.delete_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.delete_button.setFixedWidth(70)
        self.delete_button.clicked.connect(self.app.delete_selected_file)
        self.top_layout.addWidget(self.delete_button, stretch=0)
        self.top_layout.addSpacing(10)

        self.up_button = QPushButton("Up", self.parent)
        self.up_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.up_button.setFixedWidth(70)
        self.up_button.clicked.connect(lambda: self.app.move_position("top"))
        self.top_layout.addWidget(self.up_button, stretch=0)
        self.top_layout.addSpacing(10)

        self.down_button = QPushButton("Down", self.parent)
        self.down_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.down_button.setFixedWidth(70)
        self.down_button.clicked.connect(lambda: self.app.move_position("down"))
        self.top_layout.addWidget(self.down_button, stretch=0)
        self.top_layout.addSpacing(10)

        self.back_button = QPushButton("Back", self.parent)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.back_button.setFixedWidth(70)
        self.back_button.clicked.connect(lambda: self.app.scan_selected_path(None, "back"))
        self.top_layout.addWidget(self.back_button, stretch=0)
        self.top_layout.addSpacing(10)

        self.next_button = QPushButton("Next", self.parent)
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.next_button.setFixedWidth(70)
        self.next_button.clicked.connect(lambda: self.app.scan_selected_path(None, "next"))
        self.top_layout.addWidget(self.next_button, stretch=0)
        self.top_layout.addSpacing(10)

        self.user_icon = QLabel(self.parent)
        self.user_icon.setStyleSheet("""
            QLabel {
                background-color: #121212;
                border: 3px solid #B39DDB; 
                border-radius: 5px;
            }
        """)
        self.user_icon.setFixedSize(50, 50)
        self.user_icon.setScaledContents(True)
        self.top_layout.addWidget(self.user_icon)

        user_icon = self.app.backend.app_icons.load_icons(
            "user_icon.png", (46, 50), "user")
        self.user_icon.setPixmap(user_icon)

        self.create_button = QPushButton("New Folder", self.parent)
        self.create_button.setStyleSheet("""
            QPushButton {
                background-color: #1E1E1E;
                border: 2px solid #1E1E1E;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #3D3D3D; 
                border-color: #3D3D3D;
            }
        """)
        self.create_button.setFixedWidth(120)
        self.create_button.setFixedHeight(40)
        self.create_button.clicked.connect(self.app.create_folder)
        self.function_layout.addWidget(self.create_button, stretch=0)
        self.function_layout.addSpacing(10)

        self.app.backend.app_icons.set_button_icon(
            self.create_button, "folder_icon.png", (20, 20))

        self.home_button = QPushButton("Home", self.parent)
        self.home_button.setStyleSheet("""
            QPushButton {
                background-color: #1E1E1E;
                border: 2px solid #1E1E1E;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #3D3D3D; 
                border-color: #3D3D3D;
            }
        """)
        self.home_button.setFixedWidth(90)
        self.home_button.setFixedHeight(40)
        self.home_button.clicked.connect(self.app.back_to_home)
        self.function_layout.addWidget(self.home_button, stretch=0)
        self.function_layout.addSpacing(10)

        self.app.backend.app_icons.set_button_icon(
            self.home_button, "home_icon.png", (30, 30))

        self.update_button_1 = QPushButton("Update", self.parent)
        self.update_button_1.setStyleSheet("""
            QPushButton {
                background-color: #1E1E1E;
                border: 2px solid #1E1E1E;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #3D3D3D; 
                border-color: #3D3D3D;
            }
        """)
        self.update_button_1.setFixedWidth(90)
        self.update_button_1.setFixedHeight(40)
        self.update_button_1.clicked.connect(
            lambda: self.app.update_context_menu(
                self.app.backend.path_manager.absolute_path, 0
        ))
        self.function_layout.addWidget(self.update_button_1, stretch=0)
        self.function_layout.addSpacing(10)

        self.app.backend.app_icons.set_button_icon(
            self.update_button_1, "update_icon.png", (20, 20))

        self.progressbar = QProgressBar(self.parent)
        self.progressbar.setStyleSheet("""
            QProgressBar {
                background-color: #121212; 
                border: 2px solid #3D3D3D; 
                border-color: #3D3D3D; 
                border-radius: 5px;
            }

            QProgressBar::chunk {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #42AAFF, stop:0.5 #0000FF, stop:1 #9C27B0
                );
                border-radius: 5px;
            }
        """)
        self.progressbar.setFixedWidth(593)
        self.progressbar.setTextVisible(False)
        self.progressbar.setMinimum(self.app.backend.memory.USE_MINIMAL)
        self.progressbar.setMaximum(self.app.backend.memory.USE_MAXIMAL)
        self.function_layout.addWidget(self.progressbar, stretch=1)
        self.function_layout.addSpacing(10)

        self.memory_state = QLabel(self.parent)
        self.memory_state.setStyleSheet("""
            QLabel {
                background-color: #1E1E1E;
                border: 2px solid #1E1E1E;
                border-color: #1E1E1E;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 12pt;
            }
        """)
        self.memory_state.setFixedHeight(40)
        self.function_layout.addWidget(
            self.memory_state, stretch=1, alignment=Qt.AlignCenter)

        self.context_menu = QListWidget(self.parent)
        self.context_menu.setStyleSheet("""
            QListWidget {
                background-color: #1E1E1E; 
                border: none; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 12pt;
            }
            QListWidget::item:hover {
                background-color: #0000FF; 
                border-radius: 5px;
            }
            QListWidget::item:selected {
                background-color: #137FFD; 
                border-radius: 5px; 
                color: #FFFFFF;
            }
            QListWidget::item:selected:!active {
                background-color: #3D3D3D;
            }
            QListWidget::item:focus {
                outline: none;
            }
            QListWidget QScrollBar:vertical {
                background-color: #1E1E1E; 
                width: 12px; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::handle:vertical {
                background-color: #3D3D3D; 
                min-height: 20px; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::handle:vertical:hover {
                background-color: #5A5A5A;
            }
            QListWidget QScrollBar::add-page:vertical, QListWidget QScrollBar::sub-page:vertical {
                background-color: #1E1E1E; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::sub-line:vertical, QListWidget QScrollBar::add-line:vertical {
                height: 0px; 
                width: 0px;
            }
            QListWidget QScrollBar:horizontal {
                background-color: #1E1E1E; 
                width: 12px; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::handle:horizontal {
                background-color: #3D3D3D; 
                min-height: 20px; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::handle:horizontal:hover {
                background-color: #5A5A5A;
            }
            QListWidget QScrollBar::add-page:horizontal, QListWidget QScrollBar::sub-page:horizontal {
                background-color: #1E1E1E; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::sub-line:horizontal, QListWidget QScrollBar::add-line:horizontal {
                height: 0px; 
                width: 0px;
            }
        """)
        self.context_menu.setCurrentRow(0)
        self.context_menu.setFocusPolicy(Qt.ClickFocus)
        self.context_menu.itemClicked.connect(self.app.set_position)
        self.context_menu.itemDoubleClicked.connect(self.app.scan_selected_path)
        self.user_layout.addWidget(self.context_menu, stretch=1)
        self.user_layout.addSpacing(10)

        self.username = QLabel(self.parent)
        self.username.setStyleSheet("""
            QLabel {
                background-color: #212121;
                border: 2px solid #212121; 
                border-radius: 5px; 
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 12pt;
            }
        """)
        self.username.setFixedHeight(40)
        self.context_layout.addWidget(self.username, stretch=1)

        username = self.app.backend.users.get_username()
        self.username.setText(username)

        self.new_icon_button = QPushButton("New Icon", self.parent)
        self.new_icon_button.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.new_icon_button.setFixedHeight(40)
        self.new_icon_button.clicked.connect(self.app.backend.users.set_user_icon)
        self.context_layout.addWidget(self.new_icon_button, stretch=1)

        self.storage_menu = QListWidget(self.parent)
        self.storage_menu.setStyleSheet("""
            QListWidget {
                background-color: #1E1E1E; 
                border: none; 
                border-radius: 5px; 
                color: #FFFFFF; 
                font-family: SegoeUI; 
                font-size: 12pt;
            }
            QListWidget::item:hover {
                background-color: #0000FF; 
                border-radius: 5px;
            }
            QListWidget::item:selected {
                background-color: #137FFD; 
                border-radius: 5px; 
                color: #FFFFFF;
            }
            QListWidget::item:selected:!active {
                background-color: #3D3D3D;
            }
            QListWidget::item:focus {
                outline: none;
            }
            QListWidget QScrollBar:vertical {
                background-color: #1E1E1E; 
                width: 12px; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::handle:vertical {
                background-color: #3D3D3D; 
                min-height: 20px; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::handle:vertical:hover {
                background-color: #5A5A5A;
            }
            QListWidget QScrollBar::add-page:vertical, QListWidget QScrollBar::sub-page:vertical {
                background-color: #1E1E1E; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::sub-line:vertical, QListWidget QScrollBar::add-line:vertical {
                height: 0px; 
                width: 0px;
            }
            QListWidget QScrollBar:horizontal {
                background-color: #1E1E1E; 
                width: 12px; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::handle:horizontal {
                background-color: #3D3D3D; 
                min-height: 20px; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::handle:horizontal:hover {
                background-color: #5A5A5A;
            }
            QListWidget QScrollBar::add-page:horizontal, QListWidget QScrollBar::sub-page:horizontal {
                background-color: #1E1E1E; 
                border-radius: 5px;
            }
            QListWidget QScrollBar::sub-line:horizontal, QListWidget QScrollBar::add-line:horizontal {
                height: 0px; 
                width: 0px;
            }
        """)
        self.storage_menu.setCurrentRow(0)
        self.storage_menu.setFocusPolicy(Qt.ClickFocus)
        self.context_layout.addWidget(self.storage_menu, stretch=1)
        self.storage_menu.itemDoubleClicked.connect(self.app.open_new_storage)

        self.update_button_2 = QPushButton("Update", self.parent)
        self.update_button_2.setStyleSheet("""
            QPushButton {
                background-color: #0000FF;
                border: 2px solid #0000FF;
                border-radius: 5px;
                color: #FFFFFF;
                font-family: Segoe UI;
                font-size: 11pt;
            }
            QPushButton::hover {
                background-color: #137ffd; 
                border-color: #137ffd;
            }
        """)
        self.update_button_2.setFixedHeight(40)
        self.update_button_2.clicked.connect(self.app.update_storage_menu)
        self.context_layout.addWidget(self.update_button_2, stretch=1)

        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.function_layout)
        self.main_layout.addLayout(self.central_layout)
        self.main_layout.addLayout(self.user_layout)
        self.user_layout.addLayout(self.context_layout)

    def close_app(self) -> None:
        self.parent.main_app.quit()
