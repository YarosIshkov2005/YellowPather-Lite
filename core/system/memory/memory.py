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

import psutil

from pathlib import Path
from typing import Any, Optional

from PyQt5.QtWidgets import QLabel, QMessageBox, QMainWindow, QProgressBar

from core.info.message.message_window import show_message

class Memory:
    """
        Provides information about the drive memory amount.

        Args:
            app (Any): A main class of the application.

            parent (Optional[QMainWindow]): A main window of the application.
    """
    def __init__(self, app: Any, parent: Optional[QMainWindow]) -> None:
        self.app = app
        self.parent = parent

        self.USE_MINIMAL: int = 0
        self.USE_MAXIMAL: int = self.get_current_size(
            str(self.app.storage), "system", "GB")

    def get_current_size(self, storage: str = "C:\\", 
        using: str = "system", size: str = "GB") -> float:
        """
            Returns the current amount of drive memory.

            Args:
                storage (str): The path to the current drive's home directory.

                using (str): The amount of memory status (system, used, free).

                size (int): Unit of measurement of memory (Bytes, KBytes, MBytes, GBytes).

            Returns:
                float: Current drive's amount of memory.
        """
        try:
            storage = str(storage) if isinstance(storage, Path) else storage
            sizes = {
                "system": round(psutil.disk_usage(storage).total, 1), 
                "used": round(psutil.disk_usage(storage).used, 1), 
                "free": round(psutil.disk_usage(storage).free, 1)
            }
            return self.translate_to(sizes[using], size)
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def translate_to(self, bytes: int, size: str = "GB") -> float:
        """
            Returns the amount of memory as a float number according to the
                specified unit of measurement.

            Args:
                bytes (int): Specified (raw) memory size.

                size (str): Unit of measurement of memory.

            Returns:
                float: Formatted memory amount.
        """
        sizes = {
            "B": round(bytes, 1), 
            "KB": round(bytes / 1024, 1), 
            "MB": round(bytes / 1048576, 1), 
            "GB": round(bytes / 1073741824, 1)
        }
        return sizes[size]

    def show_memory_chunks(
        self, storage: str = "C:\\", 
        widget: QProgressBar = None, 
        size: str = "GB"
    ) -> None:
        """
            Displays the amount (progress chunks) of memory on the screen.

            Args:
                storage (str): The path to the current drive's home directory.

                widget (QProgressBar): A progressbar for display the memory chunks.

                size (str): Unit of measuring of memory.
        """
        system = self.get_current_size(storage, "system", size)
        used = self.get_current_size(storage, "used", size)
        widget.setMaximum(system)
        widget.setValue(used)

    def show_memory_state(
        self, storage: str = "C:\\", 
        widget: QLabel = None, 
        size: str = "GB"
    ) -> None:
        """
            Displays the amount (memory status) on the screen.
            
            Args:
                storage (str): The path to the current drive's home directory.

                widget (QLabel): A Label for display the memory status.

                size (str): Unit of measuring of memory.
        """
        system = self.get_current_size(storage, "system", size)
        free = self.get_current_size(storage, "free", size)
        widget.setText(f"Free: {free} from: {system} {size}")
