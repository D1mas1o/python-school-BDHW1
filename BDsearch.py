import sqlite3 as lite

data = None
query_string = '''
 
 select CustomerId,FirstName,Phone,Company
 from Customer
 where SupportRepId in (
 select EmployeeId
  from Employee 
  where BirthDate between '1900-12-08 00:00:00' and '1967-12-08 00:00:00')
  and CustomerId in (
    select CustomerId
    from Invoice
    where InvoiceId in(
        select InvoiceId	
        from InvoiceLine
        where TrackId in (
            select TrackId
                from Track
            where GenreId in (
             select GenreId 
             from Genre
                 where Name != 'Rock')
)
)    

  )
 order by City asc, Email DESC 
 limit 10
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