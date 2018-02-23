#!/usr/bin/env python3

# Import all required modules.
import psycopg2
import datetime

# Declares name of the database.
DBNAME = "news"

# Defines SQL queries for the 3 questions.
get_top_articles = ("""SELECT articles.title, COUNT(*) AS views FROM articles, log
        WHERE '/article/' || articles.slug = log.path
        GROUP BY articles.title
        ORDER BY views DESC LIMIT 3;""")

get_top_authors = ("""SELECT authors.name, author_rank.views FROM authors, author_rank
        WHERE authors.id = author_rank.author
        ORDER BY author_rank.views DESC;""")

get_error_percent = ("""SELECT err_percent.date, err_percent.percent FROM err_percent
        WHERE err_percent.percent > 1;""")


# Executes a predefined database query.
def execute_query(q):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(q)
    results = c.fetchall()
    db.close()
    return results


# Prints out the complete questions / answers.
if __name__ == '__main__':
    print("\n--- Project: Log Analysis (By: Kaiwei Liang) ---")
    print("\nQ1. What are the most popular three articles of all time?")
    ans1 = execute_query(get_top_articles)
    for title, views in ans1:
        print("{0} -- {1} views".format(title, views))

    print("\nQ2. Who are the most popular article authors of all time?")
    ans2 = execute_query(get_top_authors)
    for author, views in ans2:
        print('"{0}" -- {1} views'.format(author, views))

    print("\nQ3. On which days did more than 1% of requests lead to errors?")
    ans3 = execute_query(get_error_percent)
    for date, errors in ans3:
        print('{:%B %d, %Y} -- {:.1f}% errors'.format(date, errors))
    print("\n--- End of Project Output. ---")
