import sqlite3 as lite

data = None
query_string = '''
select FirstName,LastName,Phone
from Customer
where CustomerId in
(
select CustomerId
from Invoice
where InvoiceId in
(
select InvoiceId
from InvoiceLine
where UnitPrice =(Select max(UnitPrice) from InvoiceLine)
)
)
'''
try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()
    cur.execute(query_string)
    data = cur.fetchall()
    for item in data:
        print(item)
except Exception as e:
    print(e)
finally:
    if con is not None:
        con.close()