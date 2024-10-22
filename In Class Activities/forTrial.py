# for loop 1: lines 3-5
# for n in range(10):
#     # print this the value of the counter n, and then the word howdy
#     print ("{0}".format(n),"Howdy")
# print("end of the first for loop.")
#
# while loop 1: lines 9-13

# while n <= 10:
#     print("{0}".format(n),"Second loop - Howdy")
#     n = n+1
# print("end of the second for loop.")
# print("Here it is {0}".format(n))

# list and while to iterate through lines 17-23

list_of_names = ["Erica", "John", "Hilary", "mj"]
# print(list_of_names[2])
find_name = "MJ"
for name in list_of_names:
    if find_name.lower() == name.lower():
        print("found at {0} location".format(name))
        #("found")
