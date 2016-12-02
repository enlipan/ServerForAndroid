import MySQLdb


def printDBVersion(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print 'DataBase Version is %s' % data
    cursor.close()


if __name__ == '__main__':
    db = MySQLdb.connect("localhost","root","","pauldatas")
    printDBVersion(db)


def createTables(db):
    sql = """CREATE TABLE STUDENT (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        cursor.close()