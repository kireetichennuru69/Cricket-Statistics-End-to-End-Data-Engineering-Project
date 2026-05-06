
from google.cloud import bigquery

def run_transformation():
    client = bigquery.Client()

    query = """
CREATE OR REPLACE view `cricket-statisctics.transformed_dataset.icc_odi_rankings` AS        
WITH base AS (
  SELECT *,
    UPPER(TRIM(country)) AS country_clean
  FROM `cricket-statisctics.cricket_dataset.icc-odi-rankings`
),

extracted AS (
  SELECT *,
    REGEXP_EXTRACT_ALL(country_clean, r'[A-Z]{2,3}') AS codes
  FROM base
)

SELECT 
  CAST(id AS INT64) AS id,
  CAST(rank AS INT64) AS rank,
  name as player_name,
  COALESCE(
    (
      SELECT code
      FROM UNNEST(codes) AS code WITH OFFSET pos
      WHERE code NOT IN ('ICC', 'AFR', 'ASIA', 'WORLD')
      ORDER BY pos DESC
      LIMIT 1
    ),
    country_clean,
    'UNK' -- fallback for unknown
  ) AS country,
  CASE 
    WHEN REGEXP_CONTAINS(career_span, r'^\d{4}-\d{4}$') THEN
      SAFE_CAST(SPLIT(career_span, '-')[OFFSET(1)] AS INT64)
      - SAFE_CAST(SPLIT(career_span, '-')[OFFSET(0)] AS INT64)
    ELSE NULL
  END AS career_span_years,
  CAST(innings AS INT64) AS innings,
  CAST(matches AS INT64) AS matches,
  CAST(runs AS INT64) AS runs,
  SAFE_CAST(avg AS FLOAT64) AS average_runs,
  SAFE_CAST(sr AS FLOAT64) AS strike_rate,
  SAFE_CAST(highestScore AS INT64) AS highest_score,
  SAFE_CAST(hundreds AS INT64) AS hundreds,
  SAFE_CAST(fifties AS INT64) AS fifties

FROM extracted
            """

    job = client.query(query)
    job.result()
    print("Transformation completed successfully.")

if __name__ == "__main__":
    run_transformation()
