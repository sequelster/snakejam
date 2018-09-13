from sqlalchemy import create_engine

mysql_engine = create_engine('mysql://root:arglblargl@localhost/test_skaters', isolation_level="AUTOCOMMIT")

connection = mysql_engine.connect()
results = connection.execute("SELECT * FROM members ORDER BY id ASC")
for row in results:
    print (row)
connection.close()