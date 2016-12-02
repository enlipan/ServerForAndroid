import MySQLdb


def printDBVersion(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print 'DataBase Version is %s' % data
    cursor.close()



def createTables(db):
    sql = """CREATE TABLE STUDENT (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         GRADE INT )"""
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        cursor.close()

def insertData(db):
    sql = """INSERT INTO STUDENT(FIRST_NAME,
         LAST_NAME, AGE, SEX, GRADE)
         VALUES ('Mac', 'Mohan', 15, 'M', 9)"""
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        cursor.close()


if __name__ == '__main__':
    db = MySQLdb.connect("localhost","root","","pauldatas")
    printDBVersion(db)
    createTables(db)
    insertData(db)

