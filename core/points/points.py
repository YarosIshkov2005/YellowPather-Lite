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
from typing import List, Optional

from PyQt5.QtWidgets import QListWidget

class Breadcrumbs:
    """
        Responsible for generating breadcrumbs for navigating through directories.
    """
    def __init__(self) -> None:
        self.points: List[str] = []

    def generate_breadcrumbs(self, input_path: Optional[Path]) -> None:
        """
            Generates breadcrumbs for navigation (for open).
            
            Args:
                input_path (Optional[Path]): The path for generating.
        """
        path = Path(input_path) if isinstance(input_path, str) else input_path
        self.points = [part for part in path.parts if part and path]

    def generate_path(self, input_path: Optional[Path]) -> None:
        """
            Adds a new breadcrumbs to the points list (for select).

            Args:
                input_path (Optional[Path]): The path for generating.
        """
        path = Path(input_path) if isinstance(input_path, str) else input_path
        self.points.append(path.name)

    def get_previous_path(self, root_path: Optional[Path]) -> Optional[Path]:
        """
            Returns the path to the parent directory by removing the last breadcrumb.
            
            Args:
                root_path (Optional[Path]): The path to the home directory for generation.
        """
        if len(self.points) >= 2:
            self.points.pop()

        for part in self.points:
            root_path /= part
        return root_path

    def clear_all_points(self, root_path: Optional[Path]) -> None:
        """
            Clears the points when resetting (when return to home).
            
            Args:
                root_path (Optional[Path]): The path to the home directory.
        """
        self.points.clear()
        self.points.append(str(root_path))

class Points:
    """
        Responsible for saving the selection history.
    """
    def __init__(self) -> None:
        self.positions: List[int] = []

    def create_new_point(self, index: int) -> None:
        """
            Resets the selection history.
            
            Args:
                index (int): A index of the current (selected) file.
        """
        self.positions.clear()
        self.positions.append(index)

    def add_next_point(
        self, widget: Optional[QListWidget] = None, 
        index: int = 0
    ) -> None:
        """
            Adds the index of the selected directory.
            
            Args:
                widget (Optionl[QListWidget]): A container with content.
                
                index (int): A index to select the file.
        """
        self.positions.append(index)
        widget.setCurrentRow(index)

    def set_current_point(self, index: int) -> None:
        """
            Sets the index of the selected file.
            
            Args:
                index (int): A index of the selected file.
        """
        self.positions[-1] = index

    def pop_back_point(self, widget: Optional[QListWidget] = None) -> None:
        """
            Sets the index of the previous directory.
            
            Args:
                widget (Optional[QListWidget]): A container with content.
        """
        if len(self.positions) > 1:
            self.positions.pop()

        index = self.positions[-1]
        widget.setCurrentRow(index)
        return index
