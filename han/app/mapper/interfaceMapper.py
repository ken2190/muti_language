import pymysql


def get_interface_by_project(project_id):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='t1')
    cursor = conn.cursor()
    cursor.execute("select * from interface_ where project_id=?".format(project_id))
    res = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return res
