# styles.py
from PyQt6.QtWidgets import QApplication
from resource_utils import resource_path

def apply_profile(profile_name: str):
    app = QApplication.instance()
    qss_path = resource_path(f"styles/{profile_name}")
    try:
        with open(qss_path, "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"QSS file not found: {qss_path}")
