"""
Mohammad J Ahmad
HW1 - Answer Key
"""
from datetime import datetime
import DBConnector
import os

def create_table(connection):
    """
    This method creates the table for this activity
    """
    # SQL statement to create the table
    create_tale_sql= 'CREATE TABLE IF NOT EXISTS HW1_IPS (IP  VARCHAR, TimeStamp  VARCHAR, Status VARCHAR);'
    connection.query(create_tale_sql, '')

def ping_target(ip):
    """

    """
    ping_command = "ping " + ip
    ping_result = os.system(ping_command)
    return ping_result

def main():
    # Create DBConnector class
    my_db = DBConnector.MyDB()

    # Call the method that creates the needed tables
    create_table(my_db)
    # List of ips, add more
    ips=["127.0.0.1","192.0.0.1"]

    #Variables to track numbers of responding and non-responding IPs
    total_responding=0
    total_not_responding=0

    # Iterate through IPS
    for ip in ips:
        # Get the result of ping and change it to not responding if the status is 1, responding otherwise.
        status = "Not Responding" if ping_target(ip)==1 else "Responding"

        # Increment numbers of variables that track responding and non-responding variables
        if status == "Not Responding":
            total_not_responding+=1
        else:
            total_responding+=1

        # SQL statement to add data
        insert_sql = f"INSERT INTO HW1_IPS values (%s,%s,%s);"

        # Add teh data to the table
        my_db.query(insert_sql,(ip,datetime.now(),status))
    # Display Summary
    print("Total responding: " + str(total_responding))
    print("Total not responding: " + str(total_not_responding))
if __name__ == "__main__":
    main()



