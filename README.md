# Project: Log Analysis
By: Kaiwei Liang

## Overview
This is an internal reporting tool that will use information from a database to discover what kind of articles the site's readers like. The tool is a Python program using the psycopg2 module to connect to the database. It runs on command line and prints out reports (in plain text) based on the data given in the database. 

This reporting tool will answer the following 3 questions:

**Questions:**
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?


## Project Contents
The Project Submission includes the following files:
- README.md<nolink>
- news.py<nolink>
- answers.txt<nolink>
  


## Project Dependencies
This project requires your machine to have ALL of the following dependencies installed:
- [Python3](https://www.python.org/downloads/)
- [Vagrant](https://www.vagrantup.com/downloads.html) 
- [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) (Note: This project only supports Virtual Box version 5.1, please do not install any other versions.)

Once all the above dependencies are met, please continue to 'Setup Instructions' below.


## Setup Instructions
### Download Project Files
1. Download or clone the VM configuration file from [Udacity's repository](https://github.com/udacity/fullstack-nanodegree-vm). Unzip/place this folder anywhere on your machine.
2. Download or clone the project files from [this project repository](https://github.com/Kai-Wei-Liang/Project-Log-Analysis). Unzip/place this folder anywhere on your machine.
3. Download the database file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip/place this file **inside the 'vagrant' folder** from step #1.

Once setup is done, please continue to 'Launching the Virtual Machine' below.

### Launch Virtual Machine
1. From your terminal, inside the vagrant subdirectory, run the command below:

```vagrant up```

  *(This may take several minutes to finish running. Once you get your shell prompt back, proceed to the next step.)*

2. Log in to your newly installed Linux VM:

```vagrant ssh```

  *(If you are now looking at a shell prompt that starts with the word 'vagrant', congratulations — you've logged into your Linux VM successfully.)*
  
3. From your VM, change to the 'vagrant' directory:

```cd /vagrant```

Once you have successfully launched your VM and changed to the vagrant directory, please continue to 'Database Setup' below.

### Setup Database
1. Connect to the database and load all the required data:

```psql -d news -f newsdata.sql```

  *(Note: You only need to do step #1 once. For any subsequent database connections, simply run 'psql -d news')*

3. Check all the tables inside the database:

```\dt```

  *(You should be able to see 3 tables: articles, authors, log.)*
  
3. If you need to connect to the database again: 

```psql -d news```

Once you have successfully loaded the database and verified its contents, please continue to 'Create Required Views' below.

### Create Required Views

You must create **ALL** of the following views before you can successfully run the project.

While connected to the database, run the following sets of queries one by one:

**1. author_rank**

```
DROP VIEW IF EXISTS author_rank CASCADE; 
CREATE VIEW author_rank AS 
SELECT author, count(*) AS views FROM articles, log 
WHERE articles.slug = REPLACE(log.path, '/article/', '') 
GROUP BY articles.author;
```

**2. req_log**

```
DROP VIEW IF EXISTS req_log CASCADE;
CREATE VIEW req_log AS
SELECT date(time), count(*) as requests FROM log
GROUP BY date
ORDER BY requests DESC;
```

**3. err_log**

```
DROP VIEW IF EXISTS err_log CASCADE;
CREATE VIEW err_log AS
SELECT date(time), count(*) as errors FROM log
WHERE status <> '200 OK'
GROUP BY date
ORDER BY errors DESC;
```

**4. err_percent**

```
DROP VIEW IF EXISTS err_percent CASCADE;
CREATE VIEW err_percent AS
SELECT req_log.date, (err_log.errors::float / req_log.requests::float) * 100 AS percent FROM req_log, err_log
WHERE req_log.date = err_log.date;
```

Done! You are finally ready to begin running the project!
See 'Run The Project' below.


### Run The Project

While logged into the VM, from the '/vagrant' directory, run the following command:

```python3 news.py```

**Expected Output:**

From your terminal, you should be able to see output that matches the file 'answers.txt' (within the Project Output section).


## Acknowledgements

Credits to Udacity for the following:
- VM configurations
- Project questions
- Project data
















