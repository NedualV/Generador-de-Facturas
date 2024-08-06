import os
import subprocess
import sys

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_program():
    import main

if __name__ == "__main__":
    try:
        import reportlab
    except ImportError:
        install_requirements()
    run_program()
