# Cricket Statistics Data Engineering Pipeline Using Google Cloud Services 

![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?logo=googlecloud\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python\&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache_Airflow-017CEE?logo=apacheairflow\&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?logo=googlebigquery\&logoColor=white)
![Looker Studio](https://img.shields.io/badge/Looker_Studio-4A90E2?logo=looker\&logoColor=white)

---

## 📌 Overview

This project demonstrates an **end-to-end data engineering pipeline** for cricket analytics using Google Cloud.

It extracts cricket statistics via **Python-based web scraping (ESPN Cricinfo)**, processes and stores the data in **BigQuery**, and visualizes insights using **Looker Studio dashboards**.

The focus is on building **analytics-ready datasets and meaningful KPIs**, not just raw data ingestion.

---

## 🎯 Business Use Case

Cricket statistics are complex and constantly changing. This project simulates a real-world analytics system where raw player data is transformed into **decision-ready insights**.

---

### Key questions answered:

* Which players are performing consistently?
* How do players compare in terms of performance vs strike rate?
* Which countries contribute the most runs?
* What are the latest statistics available for reporting?
* How can cricket data be refreshed automatically?

---

## 🏗️ Architecture

<img width="2513" height="2063" alt="Cricket Statistics Project" src="https://github.com/user-attachments/assets/aad25010-8bb2-41f5-9cb9-c60039e0a763" />

---


### Pipeline Flow

1. Data is extracted using **Python web scraping (ESPN Cricinfo)**
2. **Apache Airflow** orchestrates the workflow
3. Data is stored in **Google Cloud Storage**
4. **Cloud Functions** trigger processing
5. **Dataflow** transforms the data
6. Data is loaded into **BigQuery**
7. **Looker Studio** visualizes insights

---

## 🛠️ Tech Stack

| Layer         | Technology     | Purpose                    |
| ------------- | -------------- | -------------------------- |
| Extraction    | Python         | Web scraping cricket stats |
| Orchestration | Apache Airflow | Workflow automation        |
| Storage       | GCS            | Raw data storage           |
| Processing    | Dataflow       | Data transformation        |
| Warehouse     | BigQuery       | Analytics storage          |
| Visualization | Looker Studio  | Dashboarding               |

---

## 📊 Dashboard Overview

<img width="6250" height="7029" alt="Cricket_Statistics_Project" src="https://github.com/user-attachments/assets/da3ad675-d81b-4458-a49a-dc358bdc5277" />

The Looker Studio dashboard provides **player performance, consistency, and country-level insights**.

---


### 🔢 KPI Metrics

* **Total Runs**
* **Avg Runs per Innings**
* **Avg Strike Rate**
* **Total Hundreds**
* **50→100 Conversion %**
* **Performance Consistency Index**

---

### 📈 Key Visualizations

* **Top 10 Players by Consistency Score**
* **Runs vs Strike Rate (Scatter Plot)** → performance vs efficiency
* **Runs by Country (Bar Chart)** → country comparison
* **Country Contribution (Treemap)** → hierarchical distribution
* **Avg Runs Distribution by Country (Pie Chart)**
* **Conversion Efficiency by Player (Bar Chart)**

---

## ⚙️ Data Pipeline Highlights

* Automated data ingestion using **web scraping**
* **Airflow DAG orchestration** for scheduling
* Event-driven pipeline using **Cloud Functions**
* Scalable processing via **Dataflow**
* Clean, analytics-ready data in **BigQuery**
* Dashboard-ready schema optimized for BI tools

---

## 📂 Repository Structure

```
├── assets/
│   ├── dashboard.png
│   └── architecture.png
├── dags/
├── scripts/
├── data/
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

### Prerequisites

* Google Cloud account
* Airflow setup
* Python 3.x

### Steps

1. Clone repo:

```bash
git clone <your-repo-url>
cd cricket-stat-data-engineering-project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure GCP credentials

4. Run Airflow DAG

5. Validate data in BigQuery

6. Connect Looker Studio dashboard

---

## 📌 Key Takeaways

* Built a **cloud-native data pipeline**
* Designed **correctly aggregated KPIs**
* Created **insight-driven dashboard (not just visuals)**
* Applied **best practices in BI and data modeling**

---

## 🚀 Future Enhancements

* Add **historical data (snapshot_date)** for trend analysis
* Introduce **data quality validation checks**
* Implement **incremental data loads**
* Add **CI/CD pipeline for deployment**

---

## 🙌 Credits

Inspired by the work of Vishal Bulbule

* GitHub: https://github.com/vishal-bulbule/cricket-stat-data-engineering-project
* YouTube: https://youtu.be/UXJxcWgxwu0

---
