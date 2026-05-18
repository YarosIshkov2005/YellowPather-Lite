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
from typing import Any, Optional

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QDesktopServices

from core.info.message.message_window import show_message

class Navigation:
    """
        Responsible for navigating through folders (next, back) and selection (up, down).
    """
    def __init__(self, app: Any, parent: Optional[QMainWindow], backend: Any) -> None:
        self.app = app
        self.parent = parent
        self.backend = backend

        self.index: int = 0

    def move_position(self, level: str) -> None:
        """
            Moves the selection in the content list (up, down).

            Args:
                level (str): Direction of movement.
        """
        if level == "top":
            if self.index > 0:
                self.index -= 1
                self.app.frontend.context_menu.setCurrentRow(self.index)
        else:
            if self.index < self.app.frontend.context_menu.count() - 1:
                self.index += 1
                self.app.frontend.context_menu.setCurrentRow(self.index)
        self.backend.points.set_current_point(self.index)
        self.backend.path_manager.selected_path = self.backend.storage.resources[self.index]

    def set_position(self, item) -> None:
        """
            Sets selected path and current index by single - clicking.

            Args:
                item: Link to the selected file in the content list.
        """
        self.index = self.app.frontend.context_menu.row(item)
        self.backend.path_manager.selected_path = self.backend.storage.resources[self.index]

    def scan_selected_path(self, item = None, move: str = "next") -> None:
        """
            Opens a file selected in the content list.

            Args:
                item: Link to the selected file in the content list.

                move (str): Direction of transition (next, back).
        """
        try:
            if item is not None and not isinstance(item, str):
                index = self.app.frontend.context_menu.row(item)
            else:
                index = self.app.frontend.context_menu.currentRow()

            if self.backend.storage.resources:
                selected_path = Path(self.backend.storage.resources[index])
            else:
                selected_path = self.backend.path_manager.absolute_path

            if not self.backend.path_manager.is_path_exists(selected_path):
                absolute_path = self.backend.path_manager.absolute_path
                self.backend.update.update_context_menu(absolute_path, self.index)
                return

            if (not self.backend.path_manager.check_permissions(selected_path)
                 and move == "next"):
                show_message(
                    self.parent, 
                    f"Permission Denied: {selected_path.name}", 
                    QMessageBox.Warning
                )
                return

            if selected_path.is_dir():
                if move == "next":
                    self.index = 0
                    self.backend.points.add_next_point(self.app.frontend.context_menu, index)
                    self.backend.update.update_context_menu(selected_path, self.index)
                else:
                    if self.backend.path_manager.is_root_directory(self.backend.breadcrumbs.points):
                        return

                    selected_path = self.backend.breadcrumbs.get_previous_path(
                        self.backend.path_manager.system_path)
                    self.index = self.backend.points.pop_back_point(self.app.frontend.context_menu)
                    self.backend.update.update_context_menu(selected_path, self.index)
            else:
                if move == "next":
                    if not self.backend.path_manager.check_file_type(selected_path):
                        return

                    QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(str(selected_path)))
                else:
                    if self.backend.path_manager.is_root_directory(self.backend.breadcrumbs.points):
                        return
                    
                    selected_path = self.backend.breadcrumbs.get_previous_path(
                        self.backend.path_manager.system_path)
                    self.index = self.backend.points.pop_back_point(self.app.frontend.context_menu)
                    self.backend.update.update_context_menu(selected_path, self.index)
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def back_to_home(self) -> None:
        """
            Returns the user to home directory.
        """
        if self.backend.path_manager.is_root_directory(self.backend.breadcrumbs.points):
            return
        self.backend.points.create_new_point(0)
        self.backend.update.update_context_menu(self.backend.path_manager.system_path, 0)
