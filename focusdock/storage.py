import os
import sys
import json

def get_save_path(filename="settings.json"):
    """
    Returns the path to the JSON save file.
    Creates 'savadata' folder next to the exe if it doesn't exist.
    """
    if getattr(sys, "frozen", False):
        # Running in PyInstaller bundle
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as script
        base_dir = os.path.dirname(__file__)
    
    save_dir = os.path.join(base_dir, "savadata")
    os.makedirs(save_dir, exist_ok=True)
    
    return os.path.join(save_dir, filename)

def load_settings():
    path = get_save_path()
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_settings(settings: dict):
    path = get_save_path()
    with open(path, "w") as f:
        json.dump(settings, f, indent=4)
