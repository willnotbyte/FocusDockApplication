import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # When running as a bundled app
        base_path = sys._MEIPASS
    except Exception:
        # When running normally
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
