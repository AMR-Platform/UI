# AMR Jetson Nano GUI Interface

This repository provides a simple graphical user interface (GUI) for an Autonomous Mobile Robot (AMR) running on a Jetson Nano. The interface includes:

- A splash screen on startup
- A main menu with 4 options
- Execution of terminal commands from the menu

## Features

- ✅ PyQt5-based GUI
- ✅ Fullscreen splash screen
- ✅ Customizable menu layout
- ✅ First menu button launches a terminal and runs setup scripts
- ⚙️ Easily extendable for robot control, diagnostics, or telemetry

---

## Screenshots

| Splash Screen | Main Menu |
|---------------|-----------|
| ![Splash](docs/splash_example.png) | ![Menu](docs/menu_example.png) |

---

## Requirements

- Jetson Nano (Ubuntu 18.04 or later)
- Python 3
- PyQt5

### Install PyQt5

```bash
sudo apt update
sudo apt install python3-pyqt5
