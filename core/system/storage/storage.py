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
import string
import platform

from pathlib import Path
from typing import List, Optional

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from core.info.message.message_window import show_message

class Storage:
    """
        Responsible for detecting connected drives.

        Args:
            parent (Optional[QMainWindow]): A main window of the application.
    """
    def __init__(self, parent: Optional[QMainWindow]) -> None:
        self.parent = parent

        self.os_system: str = platform.system()

        self._DEFAULT_DRIVE: int = 0
        self._MAX_FILES: int = 200

        self.resources: List[Path] = []

    def storage_touch(self) -> Optional[Path]:
        """
            Returns the path to the default drive from the list (for ex: C:\\).

            Returns:
                Optional[Path]: The path to the default drive.
        """
        return self.open_storage(self._DEFAULT_DRIVE)

    def open_storage(self, index: int = 0) -> Optional[Path]:
        """
            Returns the path to the drive from the list at the specified index.

            Args:
                index (int): The index for selecting the drive in the list.

            Returns:
                Optional[Path]: The path to the selected drive from the list.
        """
        if self.os_system == "Windows":
            drives = self.is_system_windows()
        elif self.os_system in ["Darwin", "Linux"]:
            drives = self.is_system_posix()
        return Path(drives[index])

    def get_storages(self) -> List[Path]:
        """
            Returns a list of all drives.

            Returns:
                List[Path]: The list of the drives.
        """
        if self.os_system == "Windows":
            drives = self.is_system_windows()
        elif self.os_system in ["Darwin", "Linux"]:
            drives = self.is_system_posix()
        return drives

    def is_system_windows(self) -> List[Path]:
        """
            Returns a list of all drives for Windows.

            Returns:
                List[Path]: The list of all drives.
        """
        try:
            drives = []
            from ctypes import windll
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.ascii_uppercase:
                if bitmask & 1:
                    if not self.check_drive_permission(f"{letter}:\\"):
                        continue
                    drives.append(f"{letter}:\\")
                bitmask >>= 1
            return drives
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def is_system_posix(self) -> List[Path]:
        """
            Returns a list of all drives for UNIX (MacOS/Linux).

            Returns:
                List[Path]: The list of all drives.
        """
        try:
            drives = []
            with open("/proc/mounts", "r") as f:
                for line in f:
                    if line.startswith("/dev/"):
                        parts = line.split()
                        if not self.check_drive_permission(parts[1]):
                            continue
                        drives.append(parts[1])
            return drives
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)

    def check_drive_permission(self, drive: str) -> bool:
        """
            Checks permissions for the selected drive.

            Args:
                drive (str): The path to the selected drive.

            Returns:
                bool: True if drive is allowed, False otherwise.
        """
        try:
            if self.os_system == "Windows":
                tmp_file = Path(drive) / "tmp_file"
                tmp_file.touch()
                tmp_file.unlink(missing_ok=True)
                return True
            else:
                if os.access(drive, os.W_OK):
                    return True
                else:
                    return False
        except Exception:
            return False

    def open_new_storage(self, index: int) -> Optional[Path]:
        """
            Returns the path to the selected drive (callback method).

            Args:
                index (int): The index for selecting the drive from the list.

            Returns:
                Optional[Path]: The path to the selected drive.
        """
        drive = self.open_storage(index)
        return drive

    def path_iteration(self, open_path: Optional[Path]) -> List[Path]:
        """
            Returns a list with paths.

            Args:
                open_path (Optional[Path]): The path to the directory to open.

            Returns:
                List[Path]: The list with paths.
        """
        try:
            count = 0
            resources = []
            self.resources.clear()
            for path in open_path.iterdir():
                if count >= self._MAX_FILES:
                    show_message(
                        self.parent, 
                        f"Iteration limit exceeded {count}/{self._MAX_FILES}", 
                        QMessageBox.Information
                    )
                    return resources
                self.resources.append(path)
                resources.append(path)
                count += 1
            self.resources.sort()
            resources.sort()
            return resources
        except Exception as e:
            show_message(self.parent, str(e), QMessageBox.Warning)
