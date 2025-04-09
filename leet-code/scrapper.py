import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the website
url = "https://www.vvitguntur.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extract the title of the website
    title = soup.title.string
    print(f"Website Title: {title}")

    # Example: Extract all headings (h1, h2, h3)
    headings = soup.find_all(['h1', 'h2', 'h3'])
    print("Headings:")
    for heading in headings:
        print(heading.text.strip())

    # Example: Extract links
    links = soup.find_all('a')
    link_data = []
    for link in links:
        href = link.get('href')
        text = link.text.strip()
        if href and text:
            link_data.append({"Text": text, "URL": href})

    # Save links to a DataFrame
    df_links = pd.DataFrame(link_data)
    print("\nLinks Extracted:")
    print(df_links)

    # Save to CSV
    df_links.to_csv("vvit_links.csv", index=False)
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")