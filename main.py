import sys
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
    sys.exit(app.exec())
