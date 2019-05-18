import sqlite3 as lite
import pickle
data = None
d = {}
query_string = '''
select FirstName,LastName,Phone,
(
select FirstName
from Employee
where EmployeeId = e.ReportsTo
),
(
select LastName
from Employee
where EmployeeId = e.ReportsTo
),
(
select Phone
from Employee
where EmployeeId = e.ReportsTo
)
from Employee as e
'''
try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()
    cur.execute(query_string)
    data = cur.fetchall()
    for item in data:
        d[item[0],item[1],item[2]] = item[3],item[4],item[5]
    pickle_out = open("data.pickle", "wb")
    pickle.dump(d, pickle_out)
    pickle_out.close()
except Exception as e:
    print(e)
finally:
    if con is not None:
        con.close()