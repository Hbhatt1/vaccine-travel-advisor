from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

# Live vaccines to check
LIVE_VACCINES = [
    "Rotavirus",
    "MMR",
    "Nasal flu",
    "Shingles",
    "Chickenpox",
    "BCG",
    "Yellow fever",
    "Oral typhoid"
]

countries_data = []
with open("countries_with_vaccines.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        countries_data.append({
            "country": row["Country"],
            "most_travellers": row["Most travellers"],
            "some_travellers": row["Some travellers"],
            "url": row["URL"],
            "malaria": row.get("Malaria", "No")
        })


@app.route("/countries")
def countries():
    """
    Returns countries based on filter:
    filter=all        -> all countries
    filter=safe       -> RA-safe (no live vaccines)
    filter=pregnancy  -> Pregnancy-safe (no live vaccines, no malaria)
    """
    filter_type = request.args.get("filter", "all")

    if filter_type == "all":
        return jsonify({"countries": countries_data, "excluded": []})

    safe = []
    excluded = []

    for c in countries_data:
        all_vaccines = []
        if c["most_travellers"]:
            all_vaccines += [v.strip() for v in c["most_travellers"].split(";")]
        if c["some_travellers"]:
            all_vaccines += [v.strip() for v in c["some_travellers"].split(";")]

        live_in_country = [v for v in all_vaccines if v in LIVE_VACCINES]

        # Pregnancy-specific rule
        if filter_type == "pregnancy":
            if live_in_country or c["malaria"] == "Yes":
                excluded.append({"country": c["country"], "reason": "live vaccine/malaria"})
            else:
                safe.append(c)

        # RA-safe
        elif filter_type == "ra":
            if live_in_country:
                excluded.append({"country": c["country"], "reason": "live vaccine"})
            else:
                safe.append(c)

    return jsonify({"countries": safe, "excluded": excluded})


if __name__ == "__main__":
    app.run(debug=True)
