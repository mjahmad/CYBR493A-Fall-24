"""
MJ Ahmad
An example of if statements in Python
In class activity 2
9/11/2023
"""

def main():
    print("Hello World!")
    # Accept the first value
    value1=input('Give me value1')

    # Accept the second value
    value2 = input('Give me value1')

    # check whether value1 is greater than or equal to value2
    if value1 >= value2:
        # print message indicating value1 is greater than or equal to value2
        print(value1 + " is greater than or equal to " + value2)
    else:
        # print that value2 is greate than value1
        # print that value2 is greate than value1
        print(value2 + " is greater than " + value1)

if __name__ == "__main__":
    print('do you see this')
    main()