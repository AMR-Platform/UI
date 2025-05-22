
---

## 🖥️ `main.py`

```python
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AMR Control Panel")
        self.setGeometry(0, 0, 800, 480)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #202020; color: white;")

        layout = QVBoxLayout()

        buttons = {
            "Start SLAM": "scripts/start_slam.py",
            "Start Teleop": "scripts/start_teleop.py",
            "Run Diagnostics": "scripts/diagnostics.py",
            "Shutdown": "shutdown now"
        }

        for label, command in buttons.items():
            button = QPushButton(label)
            button.setFixedHeight(80)
            button.setStyleSheet("font-size: 20px;")
            button.clicked.connect(lambda checked, cmd=command: self.run_command(cmd))
            layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_command(self, cmd):
        if cmd.endswith(".py"):
            subprocess.Popen(["gnome-terminal", "--", "python3", cmd])
        else:
            subprocess.Popen(["gnome-terminal", "--", "bash", "-c", cmd])

def show_main_window():
    main_window = MainMenu()
    main_window.show()
    splash.finish(main_window)

app = QApplication(sys.argv)
splash_pix = QPixmap("splash.png")
splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
splash.showFullScreen()
QTimer.singleShot(3000, show_main_window)
sys.exit(app.exec_())
