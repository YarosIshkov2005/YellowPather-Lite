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

import sys

from functools import lru_cache
from typing import Any, Optional

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    """
        Creates and centers the YellowPather Lite application window.
        
        Args:
            main_app (Optional[QMainWindow]): The main class of a PyQt QApplication.
    """
    def __init__(self, main_app: Optional[QMainWindow]) -> None:
        super().__init__()
        
        self.main_app = main_app

        self.WIDTH: int = 1250
        self.HEIGHT: int = 650

        self.screen_position.center_window(self, self.WIDTH, self.HEIGHT)

        self.application.start()

    @property
    @lru_cache(maxsize=None)
    def application(self) -> Any:
        """
            Imports a main application class.

            Returns:
                Application (Any): A main application class.
        """
        from core.app.application import Application
        return Application(window=self)

    @property
    @lru_cache(maxsize=None)
    def screen_position(self) -> Any:
        """
            Imports a main window centralization module.

            Returns:
                ScreenPosition (Any): A main window centralization module.
        """
        from core.screen.screen_position import ScreenPosition
        return ScreenPosition()

    @property
    @lru_cache(maxsize=None)
    def app_events(self) -> Any:
        """
            Imports a application's event handling module.
            
            Returns:
                AppEvents (Any): A class application's handling.
        """
        from core.events.app_events import AppEvents
        return AppEvents(self)

    def mousePressEvent(self, event) -> None:
        """
            Processes mouse clicks.
        """
        self.app_events.mousePressEvent(event)

    def mouseMoveEvent(self, event) -> None:
        """
            Processes mouse motion.
        """
        self.app_events.mouseMoveEvent(event)

app = QApplication(sys.argv)
window = MainWindow(app)
window.setWindowFlag(Qt.FramelessWindowHint)
window.setAttribute(Qt.WA_TranslucentBackground)
window.setStyleSheet("""
    background-color: #121212;
    border-radius: 5px; 
    color: #FFFFFF; 
    font-family: SegoeUI; 
    font-size: 12pt;
""")
window.show()
sys.exit(app.exec())
