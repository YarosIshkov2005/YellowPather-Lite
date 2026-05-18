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

from screeninfo import get_monitors

from PyQt5.QtCore import Qt

class ScreenPosition:
    """
        Responsible for centering the application window on the monitor.
    """
    def __init__(self) -> None:
        pass

    def center_window(self, window: Qt, width: int, height: int) -> None:
        """
            Centralizes the application window on the monitor.
            
            Args:
                window (Qt): A main application window.
                
                width (int): A width of the application window.
                
                height (int): A height of the application window.
        """
        monitor_width, monitor_height = self.get_monitor_size()
        window_x = max(0, (monitor_width // 2) - (width // 2))
        window_y = max(0, (monitor_height // 2) - (height // 2))
        window.setGeometry(window_x, window_y, width, height)

    def get_monitor_size(self) -> int:
        """
            Returns the current monitor size.
        """
        try:
            monitor = get_monitors()[0]
            monitor_width = monitor.width
            monitor_height = monitor.height
            return monitor_width, monitor_height
        except Exception:
            pass
