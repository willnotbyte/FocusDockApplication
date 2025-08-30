import sys, os
from PyQt6.QtWidgets import QApplication
from focusdock.ui_main import FocusDock
from resource_utils import resource_path

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load QSS
    qss_path = resource_path("style.qss")
    with open(qss_path, "r") as f:
        app.setStyleSheet(f.read())

    window = FocusDock()
    window.show()
    screen = QApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    x = (screen_geometry.width() - window.width()) // 2
    y = (screen_geometry.height() - window.height()) // 2
    window.move(x, y)
    sys.exit(app.exec())
