import time

import uiautomator2 as u2

d = u2.connect()

session = d.session("com.hanlanguage.hanbook")
time.sleep(8)
print(session.app_info("com.hanlanguage.hanbook"))
print(session.app_current())
