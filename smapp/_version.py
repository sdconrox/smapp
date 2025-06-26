import subprocess
from pathlib import Path

def get_version():
    try:
        # Get the latest git tag
        tag = subprocess.check_output(['git', 'describe', '--tags']).decode().strip()
        return tag
    except:
        # Fallback version if not in a git repo
        return "0.1.0"

__version__ = get_version()
