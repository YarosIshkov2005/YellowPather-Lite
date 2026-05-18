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

from typing import Any

from PyQt5.QtCore import Qt

class AppEvents:
    """
        Handles mouse clicks.
        
        Args:
            main (Any): A main window of the application.
    """
    def __init__(self, main: Any) -> None:
        self.main = main

        self.drag_position: Any = None

    def mousePressEvent(self, event) -> None:
        """
            Handles the left mouse button.
        """
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.main.frameGeometry().topLeft()

    def mouseMoveEvent(self, event) -> None:
        """
            Handles mouse motion.
        """
        if event.buttons() == Qt.LeftButton:
            self.main.move(event.globalPos() - self.drag_position)
