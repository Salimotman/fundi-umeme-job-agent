import requests
from bs4 import BeautifulSoup

KEYWORDS = [
    "Fundi Umeme",
    "Electrical Technician",
    "Electrician",
    "Maintenance Electrician"
]

URLS = [
    "https://www.zoomtanzania.net/jobs/",
]

def tafuta_kazi():
    for url in URLS:
        try:
            response = requests.get(url, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")

            text = soup.get_text(" ", strip=True)

            for keyword in KEYWORDS:
                if keyword.lower() in text.lower():
                    print(f"Kazi imepatikana: {keyword}")
                    print(url)

        except Exception as e:
            print("Hitilafu:", e)

if __name__ == "__main__":
    tafuta_kazi()