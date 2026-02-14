import os
import requests
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

RSS_FILE = "rss.xml" 
OUTPUT_FILE = "output.txt"

def fetch_content(url):
    """Fetch content from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return f"URL: {url}\nContent:\n{response.text[:300]}...\n\n"  # preview only
    except Exception as e:
        return f"URL: {url}\nError: {e}\n\n"

def load_rss_and_extract():
    """Load RSS file, extract links, and fetch content in parallel."""
    if not os.path.exists(RSS_FILE):
        print("Error: RSS XML file not found.")
        return

    try:
        tree = ET.parse(RSS_FILE)
        root = tree.getroot()
    except Exception as e:
        print(f"Error: Failed to parse RSS XML file. Details: {e}")
        return

    links = [item.find("link").text for item in root.findall("./channel/item") if item.find("link") is not None]

    if not links:
        print("Error: No links found in RSS XML file.")
        return

    # Fetch content in parallel
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_content, links))

    # Write to output.txt
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for result in results:
            f.write(result)

    print(f"✅ Content extracted from {len(links)} links and written to {OUTPUT_FILE}")

def main():
    load_rss_and_extract()

if __name__ == "__main__":
    main()