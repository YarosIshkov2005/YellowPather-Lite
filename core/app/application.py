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
from functools import lru_cache
from typing import Any, Optional, Tuple

from PyQt5.QtWidgets import QMainWindow, QMessageBox

from core.info.message.message_window import show_message

class Application:
    """
        The main (central) class of the application.
        
        Args:
            window (QMainWindow): The main window of the application.
    """
    def __init__(self, window: Optional[QMainWindow]) -> None:
        self.window = window

        self.APP_NAME: str = "YellowPather Lite File Viewer:"
        self.index: int = 0

        self.storage: Optional[Path] = self.backend.storage.storage_touch()

        self.ICON_SIZE: Tuple[int] = (30, 30)

    def start(self) -> None:
        """
            Initializes the main components of the application.
        """
        settings = self.settings._DEFAULT_SETTINGS
        settings_path = self.backend.path_manager.settings_path
        self.backend.app_settings.create_settings(settings, settings_path, 4)
        
        self.frontend.frame_container()
        self.frontend.create_gui(self.APP_NAME)

        self.backend.path_manager.system_path = self.storage
        self.update_context_menu(self.storage, self.index)
        self.update_storage_menu()

    @property
    @lru_cache(maxsize=None)
    def frontend(self) -> Any:
        """
            Imports the application's external interface (GUI).
            
            Returns:
                Frontend (Any): A application's GUI.
        """
        from core.gui.frontend import Frontend
        return Frontend(parent=self.window, app=self)

    @property
    @lru_cache(maxsize=None)
    def backend(self) -> Any:
        """
            Imports the application's internal interface (API).
            
            Returns:
                Services (Any): A application's API.
        """
        from core.services.services import Services
        return Services(app=self, parent=self.window)

    @property
    @lru_cache(maxsize=None)
    def settings(self) -> Any:
        """
            Imports a module for loading and saving application settings.
            
            Returns:
                Settings (Any): A class for loading and saving application settings.
        """
        from core.init.settings import Settings
        return Settings(app=self)

    def open_new_storage(self, item) -> None:
        """
            Opens a selected storage (drive) by double-clicking.
        """
        try:
            self.index = 0
            index = self.frontend.storage_menu.row(item)
            drive = self.backend.storage.open_new_storage(index)
            self.backend.path_manager.system_path = drive
            self.update_context_menu(drive, self.index)
        except Exception as e:
            show_message(self.window, str(e), QMessageBox.Warning)
            self.update_storage_menu()

    def scan_input_path(self) -> None:
        """
            Opens the path entered by the user from a input line.
        """
        if not self.backend.path_manager.check_storage_exists():
            self.backend.path_manager.system_path = self.storage
            self.update_context_menu(self.storage, 0)
            self.update_storage_menu()
            return
        self.backend.path_manager.scan_input_path()

    def delete_selected_file(self) -> None:
        """
            Removes the selected object from the content list permanently.
        """
        if not self.backend.path_manager.check_storage_exists():
            self.backend.path_manager.system_path = self.storage
            self.update_context_menu(self.storage, 0)
            self.update_storage_menu()
            return
        self.backend.path_manager.delete_selected_path()

    def create_folder(self) -> None:
        """
            Creates a new folder at the path specified in the input line.
        """
        if not self.backend.path_manager.check_storage_exists():
            self.backend.path_manager.system_path = self.storage
            self.update_context_menu(self.storage, 0)
            self.update_storage_menu()
            return
        self.backend.path_manager.create_folder()

    def update_context_menu(self, path: Optional[Path], index: int = 0) -> None:
        """
            Updates the context/storage menu and memory state.
            
            Args:
                path (Optional[Path]): The path obtained from the input line, or the selected 
                    path in the content list.
                    
                index (int): The index to select the current object in the content list.
        """
        if not self.backend.path_manager.check_storage_exists():
            self.backend.path_manager.system_path = self.storage
            path = self.storage

        self.backend.update.update_context_menu(path, index)
        self.backend.update.update_storage_menu()

        self.backend.memory.show_memory_chunks(
            str(self.backend.path_manager.system_path), 
            self.frontend.progressbar, 
            "GB"
        )

        self.backend.memory.show_memory_state(
            str(self.backend.path_manager.system_path), 
            self.frontend.memory_state, 
            "GB"
        )

    def update_storage_menu(self) -> None:
        """
            Updates the storage menu (YPSM/YPDM).
        """
        self.backend.update.update_storage_menu()

    def scan_selected_path(self, item = None, move: str = "next") -> None:
        """
            Opens the selected file from the content list.
            
            Args:
                item: Link to the selected file in the content list by double-clicking.
                
                move (str): Direction of transition (next or back).
        """
        if move == "next" and not self.backend.storage.resources:
            return

        if not self.backend.path_manager.check_storage_exists():
            self.backend.path_manager.system_path = self.storage
            self.update_context_menu(self.storage, 0)
            self.update_storage_menu()
            return
        self.backend.navigation.scan_selected_path(item, move)

    def move_position(self, level: str) -> None:
        """
            Moves the selection up or down within the content list.
            
            Args:
                level (str): Direction of selection movement.
        """
        if not self.backend.storage.resources:
            return

        if not self.backend.path_manager.check_storage_exists():
            self.backend.path_manager.system_path = self.storage
            self.update_context_menu(self.storage, 0)
            self.update_storage_menu()
            return
        self.backend.navigation.move_position(level)

    def set_position(self, item) -> None:
        """
            Sets the numeric index of the current selection and selected path.
            
            Args:
                item: Link to the selected file in the content list.
        """
        if not self.backend.path_manager.check_storage_exists():
            self.backend.path_manager.system_path = self.storage
            self.update_context_menu(self.storage, 0)
            self.update_storage_menu()
            return
        self.backend.navigation.set_position(item)

    def back_to_home(self) -> None:
        """
            Returns the user to the home directory of the current storage, 
            or to the computer's home directory if the storage has been removed or damaged.
        """
        if not self.backend.path_manager.check_storage_exists():
            self.backend.path_manager.system_path = self.storage
            self.update_context_menu(self.storage, 0)
            self.update_storage_menu()
            return
        self.backend.navigation.back_to_home()
