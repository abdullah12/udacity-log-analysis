#! /usr/bin/python3

import psycopg2
db = psycopg2.connect("dbname=news")


cur = db.cursor() 

sql = "select count(log.id),title from log, articles where path like concat('%',slug) group by articles.title order by count(log.id) desc limit 3"
cur.execute(sql)
result = cur.fetchall()
print ("What are the most popular three articles of all time?")
for row in result:
    print ('"',row[1],'"','__', row[0], ' views')

print('')

sql = "select count(log.id),authors.name from log, articles,authors where path like concat('%',slug) and articles.author = authors.id group by authors.name order by count(log.id) desc limit 3"
cur.execute(sql)
result = cur.fetchall()
print ("Who are the most popular article authors of all time?")
for row in result:
    print (row[1],'__', row[0], ' views')

print('')

sql3 = """with
          dailytotalview as (select date(time) as thedate, count(*) as total from log group by thedate),
          dailytotalerrorview as ( select date(time) as thedate ,count(*) as total from log where status like '404%' group by thedate)
          select (dailytotalerrorview.total::float * 100 / dailytotalview.total::float),dailytotalview.thedate from dailytotalview,dailytotalerrorview
          where dailytotalview.thedate = dailytotalerrorview.thedate
          and (dailytotalerrorview.total * 100 / dailytotalview.total) > 1
"""
cur.execute(sql3)
result = cur.fetchall()
print ("On which days did more than 1% of requests lead to errors?")
for row in result:
    print (row[1],'__',round(row[0],2))