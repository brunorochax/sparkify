# Sparkify Analytics - Udacity Project 1           ![Postgresql Logo](postgresql.jpg)

On Sparkify, we had a challenge in our data team and needed to build an environment to provide faster analises.
Our analysts were interested in understanding what songs users are listening to and with this, providing a recommendation program 
and suggest songs according to the musical type most heard.

All data was stored in different places and on different formats like JSON and CSV.

With this project, we will be able to centralize and organize all data, turning access easy and providing a self service analytics. 
We've built our data warehouse and our data team can execute queries on a single source of truth.
Also they can use tools like power bi and tableau to create dashboards and reports.

## Getting Started

These instructions will help you to execute our ETL pipeline and prepare database with all needed data.

## Prerequisites

Our environment is using Python and Postgres, you can download both on links above:

[Python 3.6.3](https://www.python.org/downloads/release/python-363/) <br>
[Postgres 9.5.19](https://www.postgresql.org/download/)

We suppose that you are familiar with python and postgres and can configure both alone.

## Files

To build this environment, we need to work with two datasets:

* Song Dataset
* Log Dataset

They are published on data folder:

* data/song_data/ <br>
* data/log_data/

## Scripts

We have just two scripts to run:

* create_tables.py
* etl.py

The first script, will create our sparkify database, import create_table_queries and drop_table_queries modules from **sql_queries.py**, 
drop (if already exists) and create all tables that you need to import song and log data, they are:

#### Fact Table
1. **songplays** - records in log data associated with song plays i.e. records with page NextSong
* songplay_id (primary key)
* start_time (foreign key to time table)
* user_id (foreign key to users table)
* level
* song_id (foreign key to songs table)
* artist_id (foreign key to artists table)
* session_id
* location
* user_agent

#### Dimension Tables
2. **users** - users in the app
* user_id (primary key)
* first_name
* last_name
* gender
* level
3. **songs** - songs in music database
* song_id (primary key)
* title
* artist_id
* year
* duration
4. **artists** - artists in music database
* artist_id (primary key)
* name
* location
* latitude
* longitude
5. **time** - timestamps of records in songplays broken down into specific units
* start_time (primary key)
* hour
* day
* week
* month
* year
* weekday

The second script, will prepare and import all data with the follow functions:

1. process_song_file() - _Read and import all songs and artists data._
2. process_log_file() - _Read and import all users and log data._
3. process_data() - _Will describe the progress of ETL on command line._
4. main() - _The main task that will call all ETL functions and execute it._

It will use some modules of **sql_queries.py** too.

## Running the Scripts

First we need to create our tables, then you need to execute the create tables script:

> python create_tables.py

Now, we need to import all data with the etl script:

> python etl.py

In a few seconds all data will be imported and ready to use.

## Authors

This project and data were created and provisioned by udacity.com on Data Engineering Nanodegree.
