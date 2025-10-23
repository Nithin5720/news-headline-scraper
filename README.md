# news-headline-scraper
# news_scraper.py

import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")

headline_list = []
for h in headlines:
    text = h.get_text(strip=True)
    if text:
        headline_list.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headline_list, start=1):
        file.write(f"{i}. {headline}\n")

print("✅ Headlines scraped and saved successfully in 'headlines.txt'")
