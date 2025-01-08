import DBConnector

# Create a new instance of the DB
my_db = DBConnector.MyDB()

# SQL command to create a new table
sqlCommand = 'DROP TABLE Ahmad_Mohammad_Table;'

# Execute the SQL command.
my_db.query(sqlCommand, '')
