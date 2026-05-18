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
import shutil

from pathlib import Path
from typing import Any, List, Optional, Tuple

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QDesktopServices

from core.info.message.message_window import show_message

class PathManager:
    """
        Provides methods for processing and protecting application paths.
        
        Args:
            app (Any): Link to the main application class.
            
            parent (QMainWindow): Link to the main application window.
            
            backend (Any): Link to the app services.
    """
    def __init__(self, app: Any, parent: Optional[QMainWindow], backend: Any) -> None:
        self.app = app
        self.parent = parent
        self.backend = backend

        self.ALLOWED_TYPES: Tuple[str] = (
            ".txt", ".html", ".css", ".png", ".jpg", ".jpeg", ".gif", 
            ".bmp", ".webp", ".doc", ".docx", ".flac", ".wav", ".mp3", 
            ".ogg", ".log", ".json"
        )

        self.system_path: Optional[Path] = None
        self.parent_path: Optional[Path] = Path(__file__).parents[3]

        self.app_icon_path: Optional[Path] = self.parent_path / "icons" / "app"
        self.user_icon_path: Optional[Path] = self.parent_path / "icons" / "user"

        self.settings_path: Optional[Path] = self.parent_path / "settings" / "settings.json"
        self.absolute_path: Optional[Path] = self.system_path
        self.selected_path: Optional[Path] = None

    def scan_input_path(self) -> None:
        """
            Opens the file at the specified path in the input line.
        """
        try:
            input_path = self.app.frontend.path_field.text()
            if not self.check_input_path(input_path):
                return

            path = self.absolute_path / input_path
            if not self.is_path_exists(path, "open"):
                return

            if not self.check_permissions(path):
                show_message(self.parent, f"Permission Denied: {path.name}", QMessageBox.Warning)
                return

            if (
                input_path in self.backend.storage.get_storages()
                or (len(input_path) <= 2 and input_path[1] == ":") 
                and not input_path.startswith(str(self.system_path))
            ):
                show_message(
                    self.parent, 
                    "Use the storage menu to move between disks", 
                    QMessageBox.Warning
                )
                return

            if path.is_dir():
                self.backend.update.update_context_menu(path, 0)
            else:
                if not self.check_file_type(path):
                    return

                QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(str(path)))
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def create_folder(self) -> None:
        """
            Creates a folder at the specified path in the input line.
        """
        try:
            path = self.app.frontend.path_field.text()
            if not self.check_input_path(path):
                return

            folder_path = self.absolute_path / path
            if self.is_path_exists(folder_path, "create"):
                return

            folder_path.mkdir(parents=True, exist_ok=True)
            self.backend.update.update_context_menu(self.absolute_path, 0)
            show_message(
                self.parent, 
                f"{folder_path.name} successfully created!", 
                QMessageBox.Information
            )
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def delete_selected_path(self) -> None:
        """
            Deletes the selected file in the content list.
        """
        try:
            index = self.app.frontend.context_menu.currentRow()
            if not self.backend.storage.resources:
                return

            file_path = self.backend.storage.resources[index]
            if not self.is_path_exists(file_path):
                self.backend.update.update_context_menu(self.absolute_path, index)
                return

            if file_path.is_dir():
                shutil.rmtree(file_path)
            else:
                file_path.unlink(missing_ok=True)

            self.backend.update.update_context_menu(self.absolute_path, 0)
            info_msg = f"{file_path.name} successfully deleted!"
            show_message(self.parent, info_msg, QMessageBox.Information)

            self.backend.points.set_current_point(0)
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def check_input_path(self, path: str) -> bool:
        """
            Checks the number of characters in the input line.
            
            Args:
                path (str): The string (path) for the check.
                
            Returns:
                bool: True if number of characters most than zero, False otherwise.
        """
        if not path:
            show_message(
                self.parent, 
                "Specify the path to the folder or file!", 
                QMessageBox.Warning
            )
            return False
        return True

    def is_path_exists(self, path: Optional[Path], flag: str = "open") -> bool:
        """
            Checks the existence of a file at the specified path.

            Args:
                path (Optional[Path]): The path for the check.

                flag (str): File verification mode.

            Returns:
                bool: True if file exists, False otherwise.
        """
        if flag == "open":
            if not path.exists():
                show_message(
                    self.parent, 
                    f"Path does not exist: {path.name}", 
                    QMessageBox.Warning
                )
                return False
            return True
        else:
            if path.exists():
                show_message(
                    self.parent, 
                    f"{path.name} already exists", 
                    QMessageBox.Warning
                )
                return True
            return False

    def check_file_type(self, path: Optional[Path]) -> bool:
        """
            Checks supported file types.
            
            Args:
                path (Optional[Path]): The path for the check.
                
            Returns:
                bool: True if file extension (path.suffix) is supported, False otherwise.
        """
        if path.suffix not in self.ALLOWED_TYPES:
            error_msg = (
                f"Unsupported file type: {path.suffix}\n\n" 
                f"Supported: {' '.join(self.ALLOWED_TYPES)}"
            )
            show_message(
                self.parent, 
                error_msg, 
                QMessageBox.Warning
            )
            return False
        return True

    def is_root_directory(self, points: List[str]) -> bool:
        """
            Checks whether the user is in the root directory when 
                trying to go up.
                
            Args:
                points (List[str]): A list storing the breadcrumbs to check.

            Returns:
                bool: True if the list consists only one breadcrumb (root), False otherwise.
        """
        if len(points) == 1:
            show_message(
                self.parent, 
                "You already in the root directory", 
                QMessageBox.Information
            )
            return True
        return False

    def check_permissions(self, path: Optional[Path]) -> bool:
        """
            Checks the directory permissions by creating a temporary file
                or the size of the current file.

            Args:
                path (Optional[Path]): The path to the folder of file being checked.

            Returns:
                bool: True if permissions exists, False otherwise.
        """
        try:
            if path.is_dir():
                if path.stat().st_size > 0:
                    next(path.iterdir())
                    
                tmp_file = path / "tmp_file"
                tmp_file.touch()
                tmp_file.unlink(missing_ok=True)
                return True
            else:
                with open(path, "rb") as f:
                    f.read(1)
                return True
        except Exception:
            return False

    def add_slash(self, path: Optional[Path]) -> str:
        """
            Adds a slash to the end of the path if it doesn't exist
                (only for folders).

            Args:
                path (Optional[Path]): The path for the check.

            Returns:
                str: The string with slash.
        """
        if str(path).endswith(os.sep):
            return str(path)
        return str(path) + os.sep

    def check_storage_exists(self) -> bool:
        """
            Checks the existence of the current storage during operations.

            Returns:
                bool: True if storage exists, False otherwise (if drive was removed).
        """
        if self.system_path is not None and not self.system_path.exists():
            error_msg = (
                f"The drive {self.system_path} was removed or damaged\n\n" 
                f"You will be return to {self.app.storage}"
            )
            show_message(
                self.parent, 
                error_msg, 
                QMessageBox.Warning
            )
            return False
        return True
