"""
Examples of using ping in python
"""
import os
import time
from datetime import datetime

def method_name(parameter):
    result = parameter + 1
    return result

def ping_something(ip):
    ping_command = "ping " + ip
    ping_result = os.system(ping_command)
    return ping_result


def main():
    """
    Main function to prompt for an IP address and check if the host is responding.
    """
    ips = ["127.0.0.1","192.168.10.1"]
    for ip in ips:

        current_time  = (datetime.now())
        result_from_method = ping_something("127.0.0.1")
        print(result_from_method)



if __name__ == "__main__":
    print("Hello World!")
    main()