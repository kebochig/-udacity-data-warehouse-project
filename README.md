# Data Warehouse on the Cloud (AWS Redshift)

Introduction: A startup called Sparkify has grown their user base and song database and want to move their data process onto 
the cloud. Their data resides in AWS S3 including user activity logs and song metadata in *JSON* format.<br/>

## Business Process / Data Requirements
- Analytics team wants to understand **what songs** their **users** are listening to by analyzing a set of dimensional tables.
- Analytics team wants a **Data warehouse on the cloud** with tables designed to **optimize queries** and gain insights on song plays.

## Engineering Task
- Create and launch a Redshift cluster on AWS 
  - Create a Redshift cluster and IAM role to grant access to S3
- Create a star schema and ETL pipeline to prepare the data for analytics team
  - Explore & load raw data (*JSON*) in S3 to Redshift staging tables
  - Define fact & dimension tables for a star schema for this particular analytic purpose
  - Write an ETL pipeline to load data from staging tables to analytics tables on Redshift
- Connect to the Redshift cluster and run some test queries

## Database Schema (Data Warehousing) Design
A **user** plays a **song** whose artist is **artist_name** at time **start_time** using **agent**.<br/>
From the above story, we can extract the necessary information/dimensions:

- **Who**: **users** dimension
- **What**: **songs** and **artists** dimension
- **When**: **time** dimension
- **How (many)**: **songplays** fact
- (More possible dimensions but not used in this project):
    - **Where**: **locations** dimension
    - **How**: **agents** dimension

Since the core business process/metric is a user playing a song, the fact table should store the song play records with user/song identifier together with related information about the how and where the song is played. Based on the data and tables 
given in the project, the star schema will have **songplays** as the fact table and **users** , **time**, **songs** and **artists** as dimension tables.

## ETL Process

## Usage and Sample Results
### Setup & Configuration
1. Fill the **HOST** and **ARN** in ``dwh.cfg``. 
2. Run ``create_tables.py``.
3. Run ``etl.py`` to load data from S3 into staging tables and then transfer into target tables (fact and dimension tables). 
