''' This file is a python program (version 3.6.2)
    which makes a connection with the database,
    creates and executes postgresql queries to get the logs information.
'''

# importing python DB-API
import psycopg2

# Connecting to the database
conn = psycopg2.connect("dbname=news")
# Getting the cursor for query execution
c = conn.cursor()

# To get the most popular 3 articles of all time
query1 = ("select a.title , count(l.path) from articles as a, log as l "
          "where '/article/'||a.slug like l.path "
          "group by a.title order by count(l.path) desc limit 3;")
c.execute(query1)
rows1 = c.fetchall()

# printing the result
print(" ")
print("The most popular three articles of all time are :")
for row in rows1:
    print('{} - {} views'.format(row[0], row[1]))

# To get most popular article authors of all time
query2 = ("select t.name, count(l.path) from authors as t "
          "join articles as a on t.id = a.author "
          "join log as l on '/article/'||a.slug = l.path "
          "group by t.name order by count(l.path) desc;")
c.execute(query2)
rows2 = c.fetchall()

# printing the result
print(" ")
print("The most popular article authors of all time are :")
for row in rows2:
    print('{} - {} views'.format(row[0], row[1]))

# To get on which days did more than 1% of requests lead to errors
query3 = ("select l1.date1, ((errors*100)/(success+errors))::float "
          "as percentage "
          "from (select date(time) as date1, count(*) as success "
          "from log where status like '%200%' group by date(time)) as l1 "
          "join (select date(time) as date2, count(*) as errors "
          "from log where status like '%404%' group by date(time)) as l2 "
          "on l1.date1 = l2.date2 "
          "where ((errors*100)/(success + errors))::float > (0.01)::float;")
c.execute(query3)
rows3 = c.fetchall()

# printing the result
print(" ")
print("Days which did more than 1% of requests lead to errors are :")
for row in rows3:
    print('{:%m/%d/%y} - {} %'.format(row[0], row[1]))

# closing the connection with databse
conn.close()
