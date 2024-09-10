def firstMethod():
    """
    This method prints a simple message
    :return:
    """
    print("You are in the first method")


def secondMethod():
    """
    This method returns a message
    :return:  confirming something
    """
    message = "You are in the second method"
    return message


def thirdMethod(data):
    """
    This method accepts a word and reverse it
    :param data: The word to reverse. Comes from the outside.
    :return: The reversed data
    """
    reversedData = data[::-1]
    return reversedData


def fourthMethod(cat):
    """
    This method prints out the name of the cat passed
    :param cat: The cat name
    :return: N/A
    """
    print("You provided me with a kittie name ", format(cat))


def fifthMethod():
    """
    Given a list of names, check whether a cat is in tht list or not.
    :return: True if the cat is found, otherwise false.
    """
    # defined a list of cats' names
    cats = ["cat1", "cat2", "cat3"]
    catCheck = "Whisper"
    if catCheck in cats:
        return True
    else:
        return False
