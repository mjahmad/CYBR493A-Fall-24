import DBConnector

# Create a new instance of the DB
my_db = DBConnector.MyDB()

# SQL command to create a new table
sqlCommand = 'CREATE TABLE IF NOT EXISTS Ahmad_Mohammad_Table (MID  VARCHAR, MName  VARCHAR);'

# Execute the SQL command.
my_db.query(sqlCommand, '')
