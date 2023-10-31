import os
import datetime as dt
print("Last accessed time= ",os.path.getatime("C:/study/TY/5thsem/python/p5"))
print("Last modified time= ",os.path.getmtime("C:/study/TY/5thsem/python/p5"))
access_date=dt.datetime.fromtimestamp(os.path.getatime("C:/study/TY/5thsem/python/p5"))
modify_date=dt.datetime.fromtimestamp(os.path.getmtime("C:/study/TY/5thsem/python/p5"))
print("Access date= ",access_date)
print("Modify date= ",modify_date)