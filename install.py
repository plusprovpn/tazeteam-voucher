import urllib.request
import importlib.util
from pathlib import Path

SO_URL = "https://raw.githubusercontent.com/plusprovpn/tazeteam-voucher/main/tazeteams.so"
SO_FILE = "tazeteams.so"

print("[*] Downloading core...")
urllib.request.urlretrieve(SO_URL, SO_FILE)
print("[+] Download complete")

p = Path(SO_FILE).resolve()
spec = importlib.util.spec_from_file_location("tazeteams", str(p)) # <- IMPORTANT
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("[+] Core loaded")
import os

launcher_path = "/data/data/com.termux/files/usr/bin/tazeteam"
launcher_script = """#!/data/data/com.termux/files/usr/bin/sh
cd "$HOME"
python install.py
"""

try:
with open(launcher_path, "w") as f:
f.write(launcher_script)
os.chmod(launcher_path, 0o755)
print("[+] Command installed: tazeteam")
except Exception as e:
print(f"[!] Launcher install failed: {e}")
