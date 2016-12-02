import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect("localhost","root","","pauldatas")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print 'DataBase Version is %s' % data
    cursor.close()