from han.app import db


def run_project():
    pass


def run_case(case_id):
    sql = "select * from request where testcase_id={}".format(case_id)
    cur = db.session.execute(sql).cursor
    cases = cur.fetchall()
    pass
