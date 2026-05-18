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

import json

from pathlib import Path
from typing import Dict, Optional

class AppSettings:
    """
        Loads and saving the application settings.
    """
    def __init__(self) -> None:
        pass

    def create_settings(self, settings: Dict, settings_path: Optional[Path], indent: int = 4) -> None:
        """
            Creates settings.json if it doesn't exist.
            
            Args:
                settings (Dict): Default settings for writing to a file.
                
                settings_path (Optional[Path]): The path to the settings file.
                
                indent (int): A number of indents in the settings content.
        """
        if settings_path.exists() and settings_path.stat().st_size != 0:
            return

        with open(settings_path, "w", encoding="utf-8") as config:
            json.dump(settings, config, indent=indent)

    def load_settings(self, settings_path: Optional[Path]) -> Dict:
        """
            Loads and returns data with settings from settings.json.
            
            Args:
                settings_path (Optional[Path]): The path to the settings file.

            Returns:
                Dict: A data with settings from settings.json.
        """
        with open(settings_path, "r", encoding="utf-8") as config:
            return json.loads(config.read())

    def save_settings(self, settings: Dict, save_path: Optional[Path], indent: int = 4) -> None:
        """
            Saves a data with settings to settings.json.
            
            Args:
                settings (Dict): Current settings for saving to settings.json.
                
                save_path (Optional[Path]): The path to the settings file.
                
                indent (int): A indents of the settings content.
        """
        with open(save_path, "w", encoding="utf-8") as config:
            json.dump(settings, config, indent=indent)
