import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="NewDatabase"
)
Cursor = database.cursor()

def create_Schema():
    Cursor.execute("DROP DATABASE IF EXISTS LAB")
    sql = '''CREATE DATABASE LAB'''
    Cursor.execute(sql)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="NewDatabase"
    )
    if connection.is_connected():
        Info = connection.get_server_info()
        print("Connected to MySQL Server version", Info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


def create_Table():
    Cursor.execute("DROP TABLE IF EXISTS Marvel")
    mysql_Create_Table = '''CREATE TABLE Marvel(
                      ID INT,
                      MOVIE VARCHAR(50),
                      DATE VARCHAR(50),
                      MCU_PHASE VARCHAR(50)
                    )'''
    Cursor.execute(mysql_Create_Table)


def insert(address):
    path = open("C:\\Desktop\\Marvel.txt")
    try:
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="NewDatabase"
        )
        while path:
            marvel = path.readline()
            if marvel == "":
                break
            splitLines = marvel.split()
            mysql_ınsert_table = """INSERT INTO Marvel(ID,MOVIE,DATE,MCU_PHASE) VALUES (%s,%s,%s,%s)"""
            record = (splitLines[0], splitLines[1], splitLines[2], splitLines[3])
            Cursor.execute(mysql_ınsert_table, record)
            database.commit()

    except mysql.connector.Error as error:
        print("Failed to insert into MySql Table {}".format(error))
    finally:
        if database.is_connected():
            Cursor.close()
            database.close()
            print("MYSQL connection is closed")


def print_all_movies():
    query = "SELECT * FROM Marvel"
    Cursor.execute(query)
    rows = Cursor.fetchall()
    for row in rows:
        print(row)

    database.close()


def delete_from_table(name):
    q = "DELETE FROM Marvel WHERE MOVIE = %s"
    data = (name,)
    Cursor.execute(q, data)
    database.commit()
    database.close()


def phase_2():
    query = "SELECT * FROM Marvel WHERE MCU_PHASE = 'Phase2'"
    Cursor.execute(query)
    rows = Cursor.fetchall()
    for row in rows:
        print(row)

    database.close()


def fix_Thor():
    query = "UPDATE Marvel SET DATE = 'November3,2017' WHERE MOVIE = 'Thor:Ragnarok'"
    Cursor.execute(query)
    database.commit()
    database.close()


def main():
    create_Schema()
    create_Table()
    insert("C:\\Desktop\\Marvel.txt")
    print("ALL MOVIES ")
    print_all_movies()
    delete_from_table('TheIncredibleHulk')
    print("ALL MOVIES AFTER DELETE PROCESS")
    print_all_movies()
    print("PHASE 2 MOVIES")
    phase_2()
    fix_Thor()
    print("AFTER THOR HAS BEEN FIXED")
    print_all_movies()


if __name__ == '__main__':
    main()
