import psycopg2

PG_HOST = 'localhost'
PG_USER = 'bobcat'
PG_PORT = 32770
PG_DB   = 'biqukan'

conn = psycopg2.connect(database=PG_DB, user=PG_USER, password="", host=PG_HOST, port=PG_PORT)
cur = conn.cursor()

class Sql:

    @classmethod
    def insert_novel_info(cls, name, author, novelurl, serialstatus, serialnumber, category):
        sql = "insert into novel_info (name, author, novelurl, serialstatus, serialnumber, category) VALUES (%(name)s, %(author)s, %(novelurl)s, %(serialstatus)s, %(serialnumber)s, %(category)s)"

        values = {
            'name': name,
            'author': author,
            'novelurl': novelurl,
            'serialstatus': serialstatus,
            'serialnumber': serialnumber,
            'category': category
        }

        cur.execute(sql, values)
        conn.commit()

    @classmethod
    def insert_novel_content(cls, novelurl, chaptername, chapterurl, chaptercontent, chapterorder):
        sql = "insert into novel_content (novelurl, chaptername, chapterurl, chaptercontent, chapterorder) VALUES (%(novelurl)s, %(chaptername)s, %(chapterurl)s, %(chaptercontent)s, %(chapterorder)s)"

        values = {
            'novelurl': novelurl,
            'chaptername': chaptername,
            'chapterurl': chapterurl,
            'chaptercontent': chaptercontent,
            'chapterorder': chapterorder
        }

        cur.execute(sql, values)
        conn.commit()
