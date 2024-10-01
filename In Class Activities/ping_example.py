"""
Examples of using ping in python
"""
import os
def ping_target(ip_address):
    ping_command = "ping " + ip_address
    exit_code = os.system(ping_command)
    return exit_code


def main():
    """
    Main function to prompt for an IP address and check if the host is responding.
    """
    ip_address = input("Enter the IP address or hostname to ping: ")
    result = ping_target(ip_address)

    if result == 0:
        print(f"{ip_address} is responding.")
    else:
        print(f"{ip_address} is not responding.")


if __name__ == "__main__":
    main()