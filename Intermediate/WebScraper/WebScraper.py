import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Target website
url = "https://www.bbc.com/news"

# Step 2: Send HTTP request
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status codes
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
    exit()

# Step 3: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract headlines and links
headlines = []
for article in soup.find_all("a", href=True):
    title = article.get_text().strip()
    link = article["href"]

    # Clean and filter results
    if title and "/news" in link:
        if not link.startswith("http"):  # Add domain if link is relative
            link = "https://www.bbc.com" + link
        headlines.append([title, link])

# Step 5: Save to CSV
with open("news_headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "Link"])  # Column headers
    writer.writerows(headlines)

print("✅ News headlines and links scraped successfully and saved in news_headlines.csv")
