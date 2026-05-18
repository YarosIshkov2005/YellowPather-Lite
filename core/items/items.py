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
from typing import Any, List, Optional, Tuple

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

class Items:
    """
        Uploads the content to the specified list.

        Args:
            backend (Any): The application's API.
    """
    def __init__(self, backend: Any) -> None:
        self.backend = backend

    def item_iteration(
        self, icons: Tuple[QIcon], 
        paths: List[Path], 
        window: Optional[QListWidget], 
        context: bool
    ) -> None:
        """
            Fills in the specified list with the contents.

            Args:
                icons (Tuple[QIcon]): A list with icons.

                paths (List[Path]): A list with paths.

                window (Optional[QListWidget]): A container to put the contents in.

                context (bool): If context - fills a content list,
                    storage list otherwise.
        """
        for path in paths:
            if context:
                icon = icons[0] if path.is_dir() else icons[1]
                text = path.name
            else:
                free = self.backend.memory.get_current_size(
                    str(path), "free", "GB"
                )
                system = self.backend.memory.get_current_size(
                    str(path), "system", "GB"
                )
                icon = icons[0]
                text = f"{path:<18} {free} / {system} GB"

            item = QListWidgetItem(QIcon(icon), text)
            window.addItem(item)
