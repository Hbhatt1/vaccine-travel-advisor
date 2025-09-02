### Vaccine Travel Advisor

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![React](https://img.shields.io/badge/React-%2320232a.svg?logo=react&logoColor=%2361DAFB)](#)
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?logo=github&logoColor=white)](#)

Vaccine Travel Advisor is a web application to explore safe travel destinations based on health conditions such as **Rheumatoid Arthritis** or **Pregnancy**, avoiding live vaccines where necessary. It also highlights malaria risk per country.

````markdown
## 🚀 Features

- Filter countries by condition (RA, Pregnancy) or show all.
- Highlight excluded countries in red if not safe for the selected condition.
- Responsive **6-column card grid** for country display.
- Toggle country card details: Most travellers vaccines, Some travellers vaccines, and official URL.
- Detects malaria risk per country.
- Disclaimer included for informational purposes only.

## 💻 Installation

### Backend

```bash
cd vaccine-travel-advisor/backend
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
pip install -r requirements.txt
python app.py
````

Backend runs at `http://127.0.0.1:5000/`.

### Frontend

```bash
cd vaccine-travel-advisor/frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173/` (or URL provided by Vite).

## ⚡ Usage

1. Open frontend in a browser.
2. Use **Select view** dropdown:

   * Show all countries
   * Rheumatoid Arthritis
   * Pregnancy
3. Click a country card to toggle vaccine details and official link.
4. Excluded countries for the selected condition appear in **red**.
5. Always consult your healthcare provider before traveling.

## 🗂 CSV Data

* `countries_with_vaccines.csv` contains scraped data from [TravelHealthPro](https://travelhealthpro.org.uk) using the scraper.
* Columns: `Country`, `Most travellers`, `Some travellers`, `Malaria`, `URL`.

## 🤝 Contributing

1. Fork the repository.
2. Create a branch for your feature:
   `git checkout -b feature/your-feature-name`
3. Commit your changes:
   `git commit -m "Add feature"`
4. Push and create a pull request.

## ⚠️ Disclaimer

This project is **informational only** and **not medical advice**. Always consult a GP before traveling.

```
