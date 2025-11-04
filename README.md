  🧩 Databricks Declarative Pipelines (Delta Live Tables)

This project demonstrates the implementation of Databricks Declarative Pipelines, also known as Delta Live Tables (DLT) — a modern framework for building reliable, scalable, and automated data pipelines on the Databricks Lakehouse Platform.
The goal of this project is to design and orchestrate a streaming data pipeline that seamlessly transforms raw data into clean, enriched, and analytics-ready datasets following the Medallion Architecture (Bronze → Silver → Gold).

📁 Folder Structure
DeclarativePipelines/
│
├── transformations_SourceCode/
│   ├── bronze/      # Raw ingestion layer
│   ├── silver/      # Cleansed and enriched data
│   └── gold/        # Aggregated business-level tables
│
├── notebooks/       # DLT notebooks defining views and tables
└── configs/         # DLT pipeline configurations

🧠 Key Concepts
🧱 Streaming Tables and Materialized Views
⚙️ Auto CDC (Change Data Capture) and Slowly Changing Dimensions (SCD Type 1 & 2)
📊 Data Quality Checks & Expectations
🔄 Append Flows and Incremental Processing
🚀 End-to-End ETL Pipeline with DLT Orchestration

🏗️ Tech Stack
Databricks | Delta Live Tables | PySpark
Structured Streaming | Auto Loader
Delta Lake | SQL | Medallion Architecture

📈 Outputs
![image alt](https://github.com/Charvi-M-J/Declarative-Pipelines/blob/1f60d2f5534e5ebc5a0d991f864cac1097466e1b/Screenshot%202025-11-04%20202233.png)
![image alt](https://github.com/Charvi-M-J/Declarative-Pipelines/blob/39dd5aa42cc0ab46aed20416474516517e7a131b/Screenshot%202025-11-03%20194941.png)
![image_alt](https://github.com/Charvi-M-J/Declarative-Pipelines/blob/39dd5aa42cc0ab46aed20416474516517e7a131b/Screenshot%202025-11-03%20191432.png)
