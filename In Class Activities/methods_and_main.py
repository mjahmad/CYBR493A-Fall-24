"""
Examples of using ping in python
"""
import os
def method_name(parameter):
    result = parameter + 1
    return result


def main():
    """
    Main function to prompt for an IP address and check if the host is responding.
    """
    value_to_pass = int(input("Enter a value: "))
    method_call = method_name(value_to_pass)

    if method_call == 0:
        print(f"{method_call} is zero.")
    else:
        print(f"{method_call} is not zero.")


if __name__ == "__main__":
    main()