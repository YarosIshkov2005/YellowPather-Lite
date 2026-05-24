```!["Screenshot"](screenshots/main_window_1.png)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15-green.svg)](https://pypi.org/project/PyQt5/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

# 🇷🇺 Русская версия

## 📄 Описание (v1.0.1)

Дорогие друзья (если таковые имеются), сегодня я хотел бы представить вам свой новый проект: **YellowPather Lite**. Это (неофициальное) продолжение устаревшей программы YellowPather, написанной на Tkinter, с использованием библиотек:

- **PyQt5** — интерфейс и графика
- **Psutil** — работа с памятью
- **Screeninfo** — получение размеров экрана

Я хотел сделать быстрый и удобный навигатор по файлам, который по скорости в некоторых случаях обгонял бы системный проводник.  
Проект распространяется под лицензией **GPLv3** (GNU General Public License version 3) из-за использования PyQt5 (Open Source) и юридических аспектов Riverbank Computing Limited.

## 🔮 Что нового в v1.0.1

- Исправлен баг с обновлением Memory Chunks при возвращении на диск после извлечения накопителя.

## 📖 Оглавление

1. Инструкция по установке, работа приложения, проблемы и их решения.
2. Поддерживаемые системы (ОС).
3. Установка зависимостей.

---

## 📑 Раздел 1.1: Инструкция по установке

Перед использованием приложения его нужно собрать в `.exe` (или исполняемый файл для вашей ОС) из скачанного репозитория. Для этого понадобится **PyInstaller** (или аналогичный упаковщик).

### Установка PyInstaller

```bash
pip install pyinstaller
```

Сборка приложения

1. Откройте папку репозитория (yellowpather-lite).
2. Найдите файл built.bat и дважды кликните по нему (в Windows откроется cmd32 и автоматически начнётся сборка).
3. Дождитесь завершения и закройте терминал.
4. Готовый .exe файл появится в папке dist. Его можно добавить в меню «Пуск» или на панель задач.

Для внесения изменений: перед сборкой отредактируйте built.bat, добавив нужные папки через --add-data "папка;папка" (для Windows разделитель ;, для Linux/macOS — :).

---

📑 Раздел 1.2: Работа приложения

YellowPather Lite — быстрое и удобное решение для повседневных задач с папками и файлами. Пока не умеет запускать самоисполняемые файлы (в целях безопасности), но в будущем появится специальный флаг.

Элементы интерфейса

1. Path Entry — поле для ввода пути к папке или файлу (относительный или абсолютный). Текущий путь отображается как подсказка (placeholder).
2. Open — открывает объект по указанному пути:
   · если путь ведёт к папке → открывается каталог
   · если к файлу → открывается системным приложением (поддерживаются .txt, .html, .css, .png, .jpg, .jpeg, .gif, .bmp, .webp, .doc, .docx, .flac, .wav, .mp3, .ogg, .log, .json)
3. Clear — очищает поле ввода.
4. Delete — удаляет выделенный элемент из списка файлов (безвозвратно!).
5. Up / Down — перемещают выделение по списку файлов вверх/вниз.
6. Back / Next — навигация по папкам: Next — войти в выделенную папку, Back — вернуться назад.
7. User Icon — аватар пользователя (можно изменить через кнопку New Icon).
8. New Folder — создаёт новую папку по указанному в поле пути.
9. Home — переходит в корневой каталог текущего диска.
10. Update (1) — обновляет интерфейс: Memory Chunks, Memory State, список файлов, список дисков.
11. Memory Chunks — прогресс-бар занятой/свободной памяти на диске.
12. Memory State — метка с объёмом свободной памяти и общим объёмом диска.
13. Context Menu — список директорий и файлов.
14. User Name — имя пользователя и его статус (администратор или нет).
15. New Icon — замена иконки пользователя (поддерживаются .png, .jpg, .jpeg, .bmp, .webp).
16. Storage Menu (YPDM) — список подключённых накопителей (встроенные, SD/microSD, USB Flash). MTP (смартфоны) не поддерживается.
17. Update (2) — обновляет только список дисков (не путать с Update (1)).

---

📑 Раздел 1.3: Проблемы и их решения

1. PyInstaller не может найти файл или зависимость

Убедитесь, что все папки из репозитория добавлены через --add-data "папка;папка" с правильным разделителем:

· Windows — ;
· Linux/macOS — :

Важно: готовые исполняемые файлы теперь доступны во вкладке Releases.

2. Подключённый накопитель не отображается в Storage Menu

Причина обычно в отсутствии прав на чтение/запись.

· На Windows используется ctypes/GetLogicalDrives(), проблема редка.
· На Linux/macOS приложение сканирует /proc/mounts, но может не учитывать реальные точки монтирования.

Решение для SD-карт: проверьте переключатель Lock (защита от записи). Если он активен — отключите и нажмите Update.
Storage Menu показывает только доступные в данный момент диски. Работа с сетевыми томами не гарантирована.

---

📑 Раздел 2.1: Поддерживаемые ОС

YellowPather Lite — кроссплатформенное приложение:

ОС Поддержка
Windows 7, 8, 10, 11 ✅ полная
macOS ✅ (требует установки PyQt5, Psutil)
Linux ✅ (проверьте /proc/mounts для работы с дисками)
Android / iOS ❌ не поддерживается

---

📑 Раздел 3.1: Установка зависимостей

Требования:

· Python ≥ 3.8 (рекомендуется 3.8.10)
· PyQt5 ≥ 5.15
· Psutil ≥ 5.9
· Screeninfo ≥ 0.8

Все зависимости можно установить одной командой:

```bash
pip install -r requirements.txt
```

---

Гудбай, увидимся может быть ещё разок или пока.

---

🇬🇧 English Version

📄 Description (v1.0.1)

Dear friends (if any exist), today I would like to introduce you to my new project: YellowPather Lite. It is basically an (unofficial) continuation of the outdated Tkinter-based program YellowPather, using libraries such as:

· PyQt5 (UI/graphics)
· Psutil (memory handling)
· Screeninfo (getting screen dimensions)

I wanted to create a fast and convenient file navigator that could sometimes outperform the native system file explorer.
This project is distributed under the GPLv3 license (GNU General Public License version 3) due to the use of PyQt5 (Open Source) and the legal aspects of Riverbank Computing Limited.

🔮 What's new in v1.0.1

· Fixed a bug with updating Memory Chunks when returning to the drive after ejecting the drive.

📖 Table of Contents

1. Installation instructions, application usage, issues and their solutions.
2. Supported systems (OS).
3. Installing dependencies.

---

📑 Section 1.1: Installation instructions

Before using the application, you need to build it into an executable file from the downloaded repository. You'll need PyInstaller (or a similar packager).

Installing PyInstaller

```bash
pip install pyinstaller
```

Building the application

1. Open the repository folder (yellowpather-lite).
2. Find the built.bat file and double-click it (on Windows, cmd32 will open and the build will start automatically).
3. Wait for completion and close the terminal.
4. The built .exe file will appear in the dist folder. You can pin it to the Start menu or taskbar.

Making changes: edit built.bat before building, adding folders via --add-data "folder;folder" (separator ; for Windows, : for Linux/macOS).

---

📑 Section 1.2: Application usage

YellowPather Lite is a fast and convenient solution for everyday tasks with folders and files. For security reasons, it cannot run self-executable files yet, but a permission flag is planned.

Interface elements

1. Path Entry — input field for a folder or file path (relative or absolute). The current path is shown as a placeholder.
2. Open — opens the object:
   · folder → opens the directory
   · file → opens with the default system application (supports .txt, .html, .css, .png, .jpg, .jpeg, .gif, .bmp, .webp, .doc, .docx, .flac, .wav, .mp3, .ogg, .log, .json)
3. Clear — clears the input field.
4. Delete — deletes the selected item from the file list (permanently!).
5. Up / Down — move selection up/down in the file list.
6. Back / Next — folder navigation: Next enters the selected folder, Back returns to the previous one.
7. User Icon — user avatar (change via New Icon button).
8. New Folder — creates a new folder at the path shown in the input field.
9. Home — goes to the root directory of the current drive.
10. Update (1) — refreshes the interface: Memory Chunks, Memory State, file list, disk list.
11. Memory Chunks — progress bar showing used/free disk space.
12. Memory State — label with free and total disk space.
13. Context Menu — list of directories and files.
14. User Name — user name and admin status.
15. New Icon — changes the user icon (supports .png, .jpg, .jpeg, .bmp, .webp).
16. Storage Menu (YPDM) — list of connected drives (internal, SD/microSD, USB Flash). MTP (smartphones) is not supported.
17. Update (2) — refreshes only the disk list (not to be confused with Update (1)).

---

📑 Section 1.3: Issues and their solutions

1. PyInstaller cannot find a file or dependency

Make sure all folders from the repository are added via --add-data "folder;folder" with the correct separator:

· Windows — ;
· Linux/macOS — :

Note: ready-made executables are now available in the Releases tab.

2. A connected storage device does not appear in Storage Menu

Usually caused by missing read/write permissions.

· On Windows ctypes/GetLogicalDrives() is used, so issues are rare.
· On Linux/macOS the app scans /proc/mounts but may not account for actual mount points.

Solution for SD cards: check the Lock switch (write protection). If it is active, turn it off and press Update.
Storage Menu shows only currently available drives. Network volumes are not guaranteed to work.

---

📑 Section 2.1: Supported OS

YellowPather Lite is cross-platform:

OS Support
Windows 7, 8, 10, 11 ✅ full
macOS ✅ (requires PyQt5, Psutil installed)
Linux ✅ (check /proc/mounts for drive access)
Android / iOS ❌ not supported

---

📑 Section 3.1: Installing dependencies

Requirements:

· Python ≥ 3.8 (recommended 3.8.10)
· PyQt5 ≥ 5.15
· Psutil ≥ 5.9
· Screeninfo ≥ 0.8

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

Goodbye, maybe we'll see each other again, or see you later.

```
