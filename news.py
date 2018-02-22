#!/usr/bin/env python3

# Import all required modules.
import psycopg2
import datetime

# Declares name of the database.
DBNAME = "news"

# Defines SQL queries for the 3 questions.
q1 = ("""SELECT articles.title, COUNT(*) AS views FROM articles, log
        WHERE articles.slug = REPLACE(log.path, '/article/', '')
        GROUP BY articles.title
        ORDER BY views DESC LIMIT 3;""")

q2 = ("""SELECT authors.name, author_rank.views FROM authors, author_rank
        WHERE authors.id = author_rank.author
        ORDER BY author_rank.views DESC;""")

q3 = ("""SELECT err_percent.date, err_percent.percent FROM err_percent
        WHERE err_percent.percent > 1;""")


# Executes the 3 queries defined above.
def question_1(q):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(q)
    results = c.fetchall()
    db.close()
    return results


def question_2(q):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(q)
    results = c.fetchall()
    db.close()
    return results


def question_3(q):
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
    ans1 = question_1(q1)
    for a in ans1:
        print("{0} -- {1} views".format(a[0], a[1]))

    print("\nQ2. Who are the most popular article authors of all time?")
    ans2 = question_2(q2)
    for a in ans2:
        print('"{0}" -- {1} views'.format(a[0], a[1]))

    print("\nQ3. On which days did more than 1% of requests lead to errors?")
    ans3 = question_3(q3)
    for a in ans3:
        print("{} -- {:.1f}% errors".format(a[0].strftime("%B %d, %Y"), a[1]))
    print("\n--- End of Project Output. ---")
