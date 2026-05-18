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

import os
import getpass
import platform

from typing import Any, Optional, Tuple

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from core.info.message.message_window import show_message

class Users:
    """
        Provides information about the user.

        Args:
            app (Any): A main class of the application.

            parent (Optional[QMainWindow]): A main window of the application.

            backend (Any): A application's API.
    """
    def __init__(self, app: Any, parent: Optional[QMainWindow], backend: Any) -> None:
        self.app = app
        self.parent = parent
        self.backend = backend

        self.os_system: str = platform.system()

        self.ALLOWED_TYPES: Tuple[str] = (
            ".bmp", ".jpg", ".jpeg", ".png", ".wepb"
        )

        self._ICON_PATH: str = "user_icon.png"

    def get_username(self) -> str:
        """
            Returns username with user's status.
            
            Returns:
                str: Username with user's status.
        """
        try:
            if self.os_system == "Windows":
                if self.check_user_status() == 1:
                    status = "(admin)"
            else:
                if self.check_user_status() == 0:
                    status = "(admin)"
            return f"{getpass.getuser()} {status}"
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def check_user_status(self) -> int:
        """
            Returns UID.
            
            Returns:
                int: User's UID (1 if user is a admin - Windows, 0 if UNIX).
        """
        try:
            if self.os_system == "Windows":
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin()
            else:
                return os.getuid()
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def set_user_icon(self) -> None:
        """
            Sets new user icon.
        """
        try:
            icon_path = self.backend.path_manager.selected_path
            if not self.backend.path_manager.is_path_exists(icon_path):
                absolute_path = self.backend.path_manager.absolute_path
                self.backend.update.update_context_menu(absolute_path, 0)
                return

            if icon_path.is_dir():
                show_message(
                    self.parent, 
                    "Select a file for the icon, not a folder!", 
                    QMessageBox.Warning
                )
                return

            if icon_path.suffix not in self.ALLOWED_TYPES:
                error_msg = (
                    "Select image file with extension:\n\n" 
                    f"{' '.join(self.ALLOWED_TYPES)}"
                )
                show_message(self.parent, error_msg, QMessageBox.Warning)
                return

            if not self.backend.path_manager.check_file_type(icon_path):
                return

            new_icon = QPixmap(str(icon_path))
            self.app.frontend.user_icon.setPixmap(new_icon)

            settings_path = self.backend.path_manager.settings_path
            settings = self.backend.app_settings.load_settings(settings_path)

            new_settings = {"user": str(icon_path)}
            settings.update(new_settings)

            self.backend.app_settings.save_settings(settings, settings_path, 4)
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)
