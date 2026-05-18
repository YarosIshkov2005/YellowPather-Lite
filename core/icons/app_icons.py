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

from pathlib import Path
from typing import Any, Optional, Tuple

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QPushButton

from core.info.message.message_window import show_message

class AppIcons:
    """
        Load icons for the external interface.

        Args:
            parent (Optional[QMainWindow]): The main window of the application.

            backend (Any): The application's API.
    """
    def __init__(self, parent: Optional[QMainWindow], backend: Any) -> None:
        self.parent = parent
        self.backend = backend

    def load_icons(self, path: str, size: Tuple[int], custom: str = "app") -> QPixmap:
        """
            Loads icons for labels and lists.
            
            Args:
                path (str): The relative path to the icon.

                size (Tuple[int]): Icon size (width, height).

                custom (str): If app - sets the icon for the application elements, 
                    for the user otherwise.

            Returns:
                QPixmap: The done scaled icon object.
        """
        try:
            settings_path = self.backend.path_manager.settings_path
            settings = self.backend.app_settings.load_settings(settings_path)
            file_path = Path(settings["user"])

            if custom == "app":
                file_path = str(self.backend.path_manager.app_icon_path / path)
            else:
                if not file_path.exists():
                    file_path = str(self.backend.path_manager.user_icon_path / path)
                else:
                    file_path = str(file_path)

            pixmap = QPixmap(file_path)
            if pixmap is None:
                pixmap = QPixmap(file_path)

            scaled_pixmap = pixmap.scaled(
                size[0], size[1], 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            return scaled_pixmap
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def set_button_icon(
        self, button: QPushButton = None, 
        icon_path: Optional[Path] = None, 
        icon_size: Tuple[int] = (50, 50)
    ) -> None:
        """
            Sets the icons for the buttons.

            Args:
                button (QPushButton): The button to apply the icon to.

                icon_path (Optional[Path]): The path to the icon.

                icon_size (Tuple[int]): Icon size (width, height).
        """
        try:
            icon_width = icon_size[0]
            icon_height = icon_size[1]
            btn_icon = self.backend.path_manager.app_icon_path / icon_path
            button.setIcon(QIcon(str(btn_icon)))
            button.setIconSize(QSize(icon_width, icon_height))
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def set_user_icon(
        self, icon_path: Optional[Path] = None, 
        icon_size: Tuple[int] = (46, 50)
    ) -> QPixmap:
        """
            Load the user's icon (avatar).

            Args:
                icon_path (Optional[Path]): The path to the icon.

                icon_size (Tuple[int]): Icon size (width, height).

            Returns:
                QPixmap: The done scaled icon object.
        """
        try:
            pixmap = QPixmap(str(icon_path))
            scaled_pixmap = pixmap.scaled(
                icon_size[0], icon_size[1], 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            return scaled_pixmap
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)
