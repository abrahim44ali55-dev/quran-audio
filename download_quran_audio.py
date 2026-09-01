
import os
import requests

# 9 قراء
reciters = {
    "Alafasy": "https://server8.mp3quran.net/afs",
    "Maher_Almuaiqly": "https://server12.mp3quran.net/maher",
    "Al_Sudais": "https://server8.mp3quran.net/sds",
    "Al_Shuraym": "https://server8.mp3quran.net/shur",
    "Al_Ajmi": "https://server10.mp3quran.net/ajm",
    "Al_Ghamdi": "https://server8.mp3quran.net/ghamdi",
    "Al_Minshawi": "https://server8.mp3quran.net/minsh",
    "Al_Husary": "https://server13.mp3quran.net/husr",
    "Yasser_Dosari": "https://server8.mp3quran.net/yasser"
}

base_dir = "Quran_Audio"
os.makedirs(base_dir, exist_ok=True)

for name, url_base in reciters.items():
    folder = os.path.join(base_dir, name)
    os.makedirs(folder, exist_ok=True)
    print(f"--- {name} ---")
    for i in range(1, 115):
        surah = f"{i:03d}.mp3"
        url = f"{url_base}/{surah}"
        path = os.path.join(folder, surah)
        if os.path.exists(path):
            continue
        try:
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                with open(path, "wb") as f:
                    f.write(r.content)
                print(f"Downloaded {name}/{surah}")
            else:
                print(f"Failed {url}")
        except Exception as e:
            print(f"Error {url} {e}")

print("تم كل شي")
