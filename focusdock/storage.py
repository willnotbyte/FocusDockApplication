import os
import sys
import json

def get_save_path(filename="settings.json"):
    """
    Returns the path to the JSON save file.
    Creates 'savedata' folder next to the exe if it doesn't exist.
    """
    if getattr(sys, "frozen", False):
        # Running in PyInstaller bundle
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as script
        base_dir = os.path.dirname(__file__)
    
    save_dir = os.path.join(base_dir, "savedata")
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

def clear_save():
    default_data = {
        "username": "user",
        "theme": "default.qss",
        "increments": 0,
        "tasks": [],
        "lt_total": 0,
        "total_completed": 0,
        "completed": 0
    }

    path = get_save_path()
    with open(path, "w") as f:
        json.dump(default_data, f, indent=4)
