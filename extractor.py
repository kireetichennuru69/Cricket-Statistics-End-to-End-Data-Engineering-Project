import requests
import csv
from bs4 import BeautifulSoup
import os
from google.cloud import storage

def run_extraction():
    # -------------------------------
    # EXTRACT: Fetch data from source
    # -------------------------------
    url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;template=results;type=batting"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("table.engineTable tbody tr.data1")

    output_path = os.path.join(os.getcwd(), "data", "batsmen_rankings.csv")
    os.makedirs("data", exist_ok=True)

    field_names = [
        'id', 'rank', 'name', 'country', 'career_span', 'innings',
        'matches', 'runs', 'avg', 'sr',
        'highestScore', 'hundreds', 'fifties'
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        #writer.writeheader()

        for i, row in enumerate(rows, start=1):
            cols = row.find_all("td")

            if len(cols) < 12:
                continue

            name_country = cols[0].text.strip()

            if "(" in name_country:
                name = name_country.split("(")[0].strip()
                country = name_country.split("(")[-1].replace(")", "").strip()
            else:
                name = name_country
                country = ""

            writer.writerow({
                "id": str(abs(hash(name))),
                "rank": i,
                "name": name,
                "country": country,
                "career_span": cols[1].text.strip(),
                "innings": cols[3].text.strip(),
                "matches": cols[2].text.strip(),
                "runs": cols[5].text.strip(),
                "avg": cols[7].text.strip(),
                "sr": cols[9].text.strip(),
                "highestScore": cols[6].text.strip(),
                "hundreds": cols[10].text.strip(),
                "fifties": cols[11].text.strip()
            })

            if i >= 100:
                break

    print("✅ Extraction complete")

    # -------------------------------
    # LOAD: Upload CSV to GCS
    # -------------------------------
    bucket_name = 'cr-ranking-data'
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    destination_blob_name = 'cricket/batsmen_rankings.csv'

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(output_path)

    print(f"✅ File uploaded to GCS bucket {bucket_name} as {destination_blob_name}")

if __name__ == "__main__":
    run_extraction()
