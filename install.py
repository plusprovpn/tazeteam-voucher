import sys
import urllib.request
import subprocess

CORE_URL = "https://raw.githubusercontent.com/plusprovpn/tazeteam-voucher/main/ruijie_core.py"
CORE_FILE = "ruijie_core.py"

print("[*] Downloading core...")
urllib.request.urlretrieve(CORE_URL, CORE_FILE)
print("[+] Download complete")
print("[*] Running...")
subprocess.run([sys.executable, CORE_FILE], check=True)
