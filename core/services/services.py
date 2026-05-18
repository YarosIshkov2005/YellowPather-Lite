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

from functools import lru_cache
from typing import Any, Optional

from PyQt5.QtWidgets import QMainWindow

class Services:
    """
        Provides access to each individual module of the application.
        
        Args:
            app (Any): The main class of the application.
            
            parent (QMainWindow): The main window of the application.
    """
    def __init__(self, app: Any, parent: Optional[QMainWindow]) -> None:
        self.app = app
        self.parent = parent

    @property
    @lru_cache(maxsize=None)
    def breadcrumbs(self) -> Any:
        """
            Imports a module for navigation through directories (breadcrumbs).
            
            Returns:
                Breadcrumbs (Any): A class for navigation through directories.
        """
        from core.points.points import Breadcrumbs
        return Breadcrumbs()

    @property
    @lru_cache(maxsize=None)
    def storage(self) -> Any:
        """
            Imports a module for retrieving information about drives.
            
            Returns:
                Storage (Any): A class for retrieving information about drives.
        """
        from core.system.storage.storage import Storage
        return Storage(parent=self.parent)

    @property
    @lru_cache(maxsize=None)
    def memory(self) -> Any:
        """
            Imports a module for retrieving information about the memory of drives.
            
            Returns:
                Memory (Any): A class for retrieving information about memory of drives.
        """
        from core.system.memory.memory import Memory
        return Memory(app=self.app, parent=self.parent)

    @property
    @lru_cache(maxsize=None)
    def app_icons(self) -> Any:
        """
            Imports a module for loading application icons.
            
            Returns:
                AppIcons (Any): A class for loading application icons.
        """
        from core.icons.app_icons import AppIcons
        return AppIcons(parent=self.parent, backend=self)

    @property
    @lru_cache(maxsize=None)
    def users(self) -> Any:
        """
            Imports a module for retrieving information about user.
            
            Return:
                Users (Any): A class for retrieving information about user.
        """
        from core.users.users import Users
        return Users(app=self.app, parent=self.parent, backend=self)

    @property
    @lru_cache(maxsize=None)
    def update(self) -> Any:
        """
            Imports a module to update user's UX.
            
            Returns:
                Update (Any): A class to update user's UX.
        """
        from core.update.update import Update
        return Update(app=self.app, backend=self)

    @property
    @lru_cache(maxsize=None)
    def navigation(self) -> Any:
        """
            Imports a module for navigating through directories.
            
            Returns:
                Navigation (Any): A class for navigating through directories.
        """
        from core.navigation.navigation import Navigation
        return Navigation(app=self.app, parent=self.parent, backend=self)

    @property
    @lru_cache(maxsize=None)
    def app_settings(self) -> Any:
        """
            Imports a module for loading and saving application settings.
            
            Returns:
                AppSettings (Any): A class for loading and saving application settings.
        """
        from core.settings.app_settings import AppSettings
        return AppSettings()

    @property
    @lru_cache(maxsize=None)
    def path_manager(self) -> Any:
        """
            Imports a module for working with paths.
            
            Returns:
                PathManager (Any): A class for working with paths.
        """
        from core.paths.manager.path_manager import PathManager
        return PathManager(app=self.app, parent=self.parent, backend=self)

    @property
    @lru_cache(maxsize=None)
    def points(self) -> Any:
        """
            Imports a module for saving selection history.
            
            Returns:
                Points (Any): A class for saving selection history.
        """
        from core.points.points import Points
        return Points()

    @property
    @lru_cache(maxsize=None)
    def items(self) -> Any:
        """
            Imports a module to load content into a content list.
            
            Return:
                Items (Any): A class to load content into a list.
        """
        from core.items.items import Items
        return Items(backend=self)
