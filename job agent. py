import requests
from bs4 import BeautifulSoup

URL = "https://www.zoomtanzania.net/jobs/"

KEYWORDS = [
    "fundi umeme",
    "electrician",
    "electrical technician",
    "maintenance electrician"
]

def tafuta_kazi():
    print("Natafuta kazi za Fundi Umeme...")

    try:
        response = requests.get(
            URL,
            timeout=30,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(" ", strip=True).lower()

        found = False

        for keyword in KEYWORDS:
            if keyword in text:
                print("Kazi imepatikana:", keyword)
                found = True

        if not found:
            print("Hakuna kazi iliyopatikana kwa maneno haya kwa sasa.")

    except Exception as error:
        print("Hitilafu:", error)

if __name__ == "__main__":
    tafuta_kazi()