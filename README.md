# Data Modeling and ETL with Postgres

Example process for the creation of a Postgres database using a simple star schema, and populating it with sample data.

The database describes and stores data related to an imaginary song streaming service, "Sparkify". This includes information related to songs, artists, users, and song plays.

## Files
* `data/` directory containing sample song files and logs of song play events  
* `sql_queries.py` SQL commands stored as text strings for table creation, insertion, and querying
* `create_tables.py` Initializes the sparkify database, and runs queries for table creation from `sql_queries.py`
* `etl.py` connects to sparkify db, processes files from `data/` directory, and inserts transformed data into db using queries from `sql_queries.py`
* `etl.ipynb` workbook for developing processes used in `etl.py`
* `test.ipynb` connects to sparkify db and runs test queries to confirm successful table creation and data insertion

## Process
* run `create_tables.py`
* run `etl.py`