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

class Update:
    """
        Updates the applications user's GUI/UX.

        Args:
            app (Any): A main class of the application.

            backend (Any): A application's API.
    """
    def __init__(self, app: Any, backend: Any) -> None:
        self.app = app
        self.backend = backend

    def update_context_menu(self, path: Optional[Path], index: int) -> None:
        """
            Updates the main file list.

            Args:
                path (Optional[Path]): The path to the selected file.

                index (int): A index of the current file.
        """
        self.app.frontend.path_field.clear()
        self.app.frontend.context_menu.clear()

        self.backend.breadcrumbs.generate_breadcrumbs(path)
        folder_icon = self.backend.app_icons.load_icons("folder_icon.png", (30, 30), "app")
        file_icon = self.backend.app_icons.load_icons("file_icon.png", (30, 30), "app")
        icons = (folder_icon, file_icon)

        paths = self.backend.storage.path_iteration(path)
        self.backend.items.item_iteration(icons, paths, self.app.frontend.context_menu, True)
        self.backend.points.add_next_point(self.app.frontend.context_menu, index)
        self.backend.path_manager.absolute_path = path

        if self.backend.storage.resources:
            self.backend.path_manager.selected_path = self.backend.storage.resources[index]
        else:
            self.backend.path_manager.selected_path = None

        path = self.backend.path_manager.add_slash(path)

        self.app.frontend.path_field.setPlaceholderText(path)
        self.app.frontend.context_menu.setCurrentRow(index)

    def update_storage_menu(self) -> None:
        """
            Updates the drive menu list.
        """
        index = self.app.frontend.storage_menu.currentRow()
        if index <= -1:
            index = 0
        self.app.frontend.storage_menu.clear()

        drive_icon = self.backend.app_icons.load_icons("drive_icon.png", (30, 30), "app")
        storages = self.backend.storage.get_storages()
        icons = (drive_icon,)

        self.backend.items.item_iteration(icons, storages, self.app.frontend.storage_menu, False)
        self.app.frontend.storage_menu.setCurrentRow(index)
