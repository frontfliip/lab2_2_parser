"""
A module to parse the json file
"""
import json


def get_keys(dict):
    '''
    Parses the dict and returns the keys
    (dict) -> list
    >>> get_keys({1: "ho", 2: "ho", 3: "ho"})
    [1, 2, 3]
    '''

    list = []
    for key in dict.keys():
        list.append(key)
    return list

def open_file(json_file_name):
    """
    Opens the file and creates the dict
    (str) -> dict
    """

    with open(json_file_name, encoding="utf-8") as file:
        info = json.load(file)
    return info

def print_start():
    """
    Prints the first two lines
    """

    print("Hi, you can start the review")
    print("\n")

def good_parse(json):
    """
    Navigates the user through the json file
    """

    if type(json) == dict:
        print("Choose the key you want to discover and write it(format: str), or write <exit> to finish review")
        print("\n")
        keys = get_keys(json)
        print(keys)
        print("\n")
        user_input = input()
        indicator = 0
        if user_input == "exit":
            exit()
        for key in keys:
            if user_input == key:
                indicator = 1
        if indicator != 1:
            print("There is no such key")
            print("\n")
            print("Reboot the progarm and try again")
            print("\n")
            exit()
        
        good_parse(json[user_input])

    if type(json) == list:
        length = len(json)
        print("\n")
        print("Which of", length, "options (dicts) do you want to access? (write a number), or write <exit> to exit")
        print("\n")
        user_number = input()
        if str(user_number) == "exit":
            exit()
        if int(user_number) < 0 or int(user_number) > length:
            print("There is no such index")
            print("\n")
            print("Reboot the progarm and try again")
            print("\n")
            exit()
        correct_num = int(user_number) - 1
        print("\n")
        good_parse(json[correct_num])

    if type(json) == int or type(json) == str:
        print("\n")
        print("Here is what you've been looking for:")
        print("\n")
        print(json)
        print("\n")

# good_parse(open_file("kved.json"))
def main(file_name):
    """
    Main func
    """
    json_f = open_file(file_name)
    print_start()
    good_parse(json_f)


main("facebook.json")