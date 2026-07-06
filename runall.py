import subprocess
import os

# Always point to the src directory
BASE_DIR = os.path.join(os.path.dirname(__file__), "src")

files = [
    "main.py",
    "gui_main.py",
    "bruteforce_pwd_analyzer.py",
    "breach_check.py",
    "analyzer.py",
    "__init__.py"
]

for f in files:
    filepath = os.path.join(BASE_DIR, f)
    print(f"\nRunning {f}...")
    if os.path.exists(filepath):
        subprocess.run(["python", filepath])
    else:
        print(f"⚠ File not found: {filepath}")

print("\nAll done!")
