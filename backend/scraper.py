import requests
from bs4 import BeautifulSoup
import csv
import string
import time

BASE_URL = "https://travelhealthpro.org.uk/countries"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://google.com",
    "Connection": "keep-alive"
}

def scrape_country_page(url):
    """Scrape vaccine info and malaria tab for one country page."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        most_vaccines = []
        some_vaccines = []

        # Check for Malaria tab
        malaria_flag = "No"  # default
        malaria_tab = soup.select_one("ul.section-tabs li#\\#Malaria-tab a")
        if malaria_tab:
            # Get the content section following the <h1>Malaria</h1> header
            malaria_section = soup.find("h1", string=lambda t: t and "malaria" in t.lower())
            if malaria_section:
                parent_section = malaria_section.find_parent("div", class_="content-section")
                if parent_section:
                    text_content = parent_section.get_text(separator=" ", strip=True).lower()
                    if "malaria-free" not in text_content:
                        malaria_flag = "Yes"

        headers = soup.find_all("h2")
        for header in headers:
            title = header.get_text(strip=True).lower()

            if "most travellers" in title:
                acc = header.find_next("div", class_="accordion")
                if acc:
                    most_vaccines = [h4.get_text(strip=True) for h4 in acc.select("h4.accordion-button")]

            elif "some travellers" in title:
                acc = header.find_next("div", class_="accordion")
                if acc:
                    some_vaccines = [h4.get_text(strip=True) for h4 in acc.select("h4.accordion-button")]

        return most_vaccines, some_vaccines, malaria_flag

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return [], [], "No"

def scrape_countries():
    """Scrape the country index page and collect all countries + vaccine info + malaria."""
    response = requests.get(BASE_URL, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    results = []

    for letter in string.ascii_lowercase:
        section_id = f"cntry-{letter}"
        section = soup.find("div", {"id": section_id, "class": "country-content"})
        if not section:
            print(f"No section found for {letter.upper()}, skipping...")
            continue

        countries = section.select("li.number_div a")
        print(f"Found {len(countries)} countries in {letter.upper()}")

        for c in countries:
            country_name = c.get_text(strip=True)
            country_url = c.get("href")
            if country_url and not country_url.startswith("http"):
                country_url = "https://travelhealthpro.org.uk" + country_url

            print(f"Visiting {country_name}")

            most, some, malaria = scrape_country_page(country_url)

            results.append([
                country_name,
                "; ".join(most),
                "; ".join(some),
                malaria,
                country_url
            ])

            time.sleep(1.5)  # polite delay

    return results

def save_to_csv(data, filename="countries_with_vaccines.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Country", "Most travellers", "Some travellers", "Malaria", "URL"])
        writer.writerows(data)
    print(f"Saved {len(data)} countries to {filename}")

if __name__ == "__main__":
    all_data = scrape_countries()
    save_to_csv(all_data)
