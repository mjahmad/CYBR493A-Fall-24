"""
MJ Ahmad
9/24/2024
Activity #2 like a pro
"""
import DBConnector


def CreateTheTable(my_db):
    """
    This method creates the table we need for this activity
    :return: N/A
    """
    # SQL command to create a new table
    sqlCommand = 'CREATE TABLE IF NOT EXISTS Ahmad_Mohammad_Table (MID  VARCHAR, MName  VARCHAR);'

    # Execute the SQL command.
    my_db.query(sqlCommand, '')


def DropTheTable(my_db):
    """
    This method drps the table we created earlier in this activity
    :return: N/A
    """

    # SQL command to create a new table
    sqlCommand = 'DROP TABLE Ahmad_Mohammad_Table;'

    # Execute the SQL command.
    my_db.query(sqlCommand, '')


def main():
    # Create a new instance of the DB
    my_db = DBConnector.MyDB()

    CreateTheTable(my_db)
    sqlStatement = 'INSERT INTO AHMAD_MOHAMMAD_TABLE VALUES(%s,%s);'
    my_db.query(sqlStatement, ('1', 'One'))
    my_db.query(sqlStatement, ('2', 'IPs'))
    my_db.query(sqlStatement, ('3', 'Dogs'))
    my_db.query(sqlStatement, ('4', 'Cats'))
    my_db.query(sqlStatement, ('5', 'fIVE'))

    DropTheTable(my_db)


if __name__ == "__main__":
    main()
