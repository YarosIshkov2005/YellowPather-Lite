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
from PyQt5.QtWidgets import QMessageBox

def show_message(parent: Qt, message: str, sign: Any) -> None:
    """
        Creates a dialog box for messages.

        Args:
            parent (Qt): A parent window (main application window).

            message (str): A message to display to the user.

            sign (Any): A message type (info, warning).
    """
    msg = QMessageBox(parent)
    msg.setText(message)
    msg.setIcon(sign)
    msg.setWindowFlag(Qt.FramelessWindowHint)
    msg.setStyleSheet("""
        QMessageBox {
            background-color: #121212; 
            border-radius: 5px;
        }

        QMessageBox QPushButton {
            background-color: #0000FF; 
            border: 2px solid #0000FF; 
            border-color: #0000FF; 
            border-radius: 5px; 
            color: #FFFFFF; 
            padding: 5px; 
            min-width: 80px;
        }

        QMessageBox QPushButton::hover {
            background-color: #137FFD; 
            border-color: #137FFD;
        }
    """)
    win = msg.exec()
