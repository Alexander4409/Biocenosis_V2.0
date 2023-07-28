import sqlite3
from time import time
class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_objects(self, table):
        try:
            self.__cur.execute(f'SELECT * from {table}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Data read error")
        return []

    def get_menu(self):
        return self.get_objects("menu")

    def get_posts(self):
        return self.get_objects("posts")

    def add_post(self, title, text, url):
        try:
            self.__cur.execute(f'SELECT COUNT() as "count" FROM posts WHERE url =="{url}"')
            res = self.__cur.fetchone()
            if res["count"] > 0:
                print("Article with such url already exist!")
                return False

            tm = time()
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)",(title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Add post error", e)
            return False
        return True

    def get_post(self,post_id):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE url =="{post_id}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Get data error from data base", e)
        return None, None