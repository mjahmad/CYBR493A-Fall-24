"""
MJ Ahmad
9/24/2024
Activity #2 like a pro
"""
import os

import DBConnector


def CreateTheTable(my_db):
    """
    This method creates the table we need for this activity
    :return: N/A
    """
    # SQL command to create a new table
    sqlCommand = 'CREATE TABLE IF NOT EXISTS Ahmad_Mohammad_HW1_IPs(IP  VARCHAR, Time_Stamp  VARCHAR, Status VARCHAR);'

    # Execute the SQL command.
    my_db.query(sqlCommand, '')


def ping_target(ip_address):
    """
    This methods pings IPs
    :param ip_address: The IP address to ping
    :return: ping_result: The status of the ping
    """
    ping_command = "ping " + ip_address
    ping_result = os.system(ping_command)
    return ping_result



def main():
    # Create a new instance of the DB
    #my_db = DBConnector.MyDB()
    #CreateTheTable(my_db)
    ips = ["127.0.0.1","127.1.1.1","127.2.2.2","199.199.0.0"]
    for ip in ips:
        print("The status is: ",ping_target(ip))


if __name__ == "__main__":
    main()
