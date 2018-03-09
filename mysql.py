import pymysql

def sqltest(imgid1):
    db = pymysql.connect("127.0.0.1", "root", "123456", "test", port=3308)
    cursor = db.cursor()
    sql = 'select * from test.test_tabdd as tt where tt.imgid = {:s}'.format(imgid1)
    sql2 = 'INSERT INTO test.test_tabdd  (imgid, count_test) VALUES ({}, 1)'.format(imgid1)
    sql3 = 'UPDATE test_tabdd SET count_test = count_test + 1 WHERE imgid = {}' .format(imgid1)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if not results:
            cursor.execute(sql2)
            db.commit()
        else:
            cursor.execute(sql3)
            db.commit()

        db.close()
    except:
        db.rollback()
sqltest('"count"')
