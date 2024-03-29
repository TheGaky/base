from mysql.connector import connect, Error
import logging
from config import SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE


def insert_user(uid, briefcase):
    this_user_already_exists = False
    if not get_all_users() is None:
        for user in get_all_users():
            if uid in user:
                this_user_already_exists = True
    if not this_user_already_exists:
        insert_ratings_query = """
        INSERT INTO moneywood_users
        (uid, briefcase)
        VALUES (%s, %s)
        """
        try:
            with connect(
                    host=SQL_HOST,
                    user=SQL_USER,
                    password=SQL_PASSWORD,
                    database=SQL_DATABASE
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(insert_ratings_query, (uid, briefcase))
                    connection.commit()
                    return True
        except Error as e:
            print(e)
        return False


def get_all_users():
    try:
        with connect(
                host=SQL_HOST,
                user=SQL_USER,
                password=SQL_PASSWORD,
                database=SQL_DATABASE
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * from smth")
                return cursor.fetchall()
    except Error as e:
        print(e)


def update_value(x, v):
    x
    try:
        with connect(
                host=SQL_HOST,
                user=SQL_USER,
                password=SQL_PASSWORD,
                database=SQL_DATABASE
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(x, v)
                connection.commit()
                return True
    except Error as e:
        print(e)
    return False

x = """
    UPDATE smth
    SET smth = %s
    WHERE smth = %s;
            """
v = ()
