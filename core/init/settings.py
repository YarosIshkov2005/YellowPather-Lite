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

from typing import Any, Dict

class Settings:
    """
        Stores the default settings configuration.
    """
    def __init__(self, app: Any) -> None:
        self.app = app

        self._DEFAULT_SETTINGS: Dict[Any] = {
            "user": f"{self.app.backend.path_manager.app_icon_path}/user_icon.png"
        }