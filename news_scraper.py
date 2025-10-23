# news_scraper.py

import requests
from bs4 import BeautifulSoup

# URL of the news site (you can change it to BBC, TOI, etc.)
url = "https://www.bbc.com/news"

# Step 1: Fetch the HTML content
response = requests.get(url)
response.raise_for_status()  # Ensures program stops if there’s a bad request

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headline tags
# (BBC uses <h2> for headlines, adjust this if using another site)
headlines = soup.find_all("h2")

# Step 4: Collect text headlines
headline_list = []
for h in headlines:
    text = h.get_text(strip=True)
    if text:  # Avoid empty tags
        headline_list.append(text)

# Step 5: Save to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headline_list, start=1):
        file.write(f"{i}. {headline}\n")

print("✅ Headlines scraped and saved successfully in 'headlines.txt'")
