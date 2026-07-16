## Architecture Overview

DataForge Platform is designed as a modern enterprise data platform composed of multiple layers, where each layer has a specific responsibility within the data lifecycle.

The process begins with the Data Ingestion Layer, which collects data from multiple external sources such as APIs, CSV files, JSON files, and relational databases. The ingested data is then processed by Python pipelines responsible for validation, logging, and initial data preparation.

After the ingestion process, the raw data is stored in Azure Data Lake Storage, providing a scalable and reliable cloud storage layer.

The core processing is performed in Azure Databricks using the Medallion Architecture (Bronze, Silver, and Gold layers), where data is progressively cleaned, transformed, and prepared for business consumption.

Finally, curated data is exposed through a SQL Server Data Mart and consumed by Power BI dashboards, enabling business users to analyze information and support data-driven decision-making.