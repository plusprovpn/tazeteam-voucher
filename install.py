cat > install.py << 'PY'
import os
import sys
import hashlib
import uuid
import requests
import subprocess

APPROVED_URL = "https://raw.githubusercontent.com/plusprovpn/tazeteam-voucher/main/approved_devices.json"
CORE_URL = "https://github.com/user-attachments/files/27424783/ruijie_core.py"
OUT_FILE = "ruijie_core.py"

def hwid():
seed = f"{uuid.getnode()}|{os.getuid()}|termux"
return hashlib.sha256(seed.encode()).hexdigest()

def check_approved(user_id):
h = hwid()
try:
data = requests.get(APPROVED_URL, timeout=15).json()
except Exception as e:
print("[!] Cannot fetch approval list:", e)
return False, h

for d in data.get("devices", []):
if not d.get("enabled", False):
continue
if str(d.get("user_id")) == str(user_id) and str(d.get("hwid")) == str(h):
return True, h
return False, h

def download_core():
r = requests.get(CORE_URL, timeout=20)
if r.status_code != 200:
print("[!] Cannot download core file")
sys.exit(1)
with open(OUT_FILE, "w", encoding="utf-8") as f:
f.write(r.text)

def run_core():
subprocess.run([sys.executable, OUT_FILE])

def main():
user_id = input("Enter your Telegram ID: ").strip()
ok, h = check_approved(user_id)
if not ok:
print("[!] Access Denied")
print("[*] Your HWID:", h)
print("[*] Send ID + HWID to admin for approval.")
return

print("[+] Approved. Downloading core...")
download_core()
print("[+] Starting tool...")
run_core()

if __name__ == "__main__":
main()
PY

python3 install.py
