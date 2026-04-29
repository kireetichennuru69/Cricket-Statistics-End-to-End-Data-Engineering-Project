from googleapiclient.discovery import build


def trigger_df_job(cloud_event):   
 
    service = build('dataflow', 'v1b3')
    project = "cricket-statisctics"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://cr-dataflow-metadata/udf.js",
        "JSONPath": "gs://cr-dataflow-metadata/bq_schema.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "cricket-statisctics.cricket_dataset.icc_odi_rankings",
        "inputFilePattern": "gs://cr-ranking-data/cricket/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://cr-dataflow-metadata/temp"
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

