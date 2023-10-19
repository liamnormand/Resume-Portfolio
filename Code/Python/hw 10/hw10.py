import copy
def find_the_mins(dictionary):
    '''
    Purpose: Takes in a dictionary and returns a new dictionary containing the same keys but
    with the values set as the minimum value in each list associated with the key in the initial list.
    If the list empty, the key is removed from the returned dictionary
    Parameter(s): dictionary- a dictionary with strings as keys, and lists of integers as the values.
    Return Value: Returns a dictionary with strings as keys, and the minimum integer as the associated value.
    '''
    ret_dictionary = copy.copy(dictionary)
    for key in dictionary:
        if len(dictionary[key]) > 0:
            ret_dictionary[key] = min(dictionary[key])
        else:
            del ret_dictionary[key]
    return ret_dictionary

def find_the_contact(Directory, Name, Field):
    '''
    Purpose: If the string contained by Name is a key in the directory, and the field is a key in the sub-dictionary for that Name,
    then the function returns the requested value for that Name and field. If the Name is in the directory, but the field is not present,
    then None is returned. If the Name is not in the directory, it is added to the directory and given one field 'Username' which contains
    the first three characters of Name. In this final case, if the field is Username, it returns the newly created username, otherwise returning None. 
    Parameter(s):
        Directory- dictionary with string keys associated with dictionary values.
        Name- string representing the key to search directory for.
        Field- string representing the key to search the sub-directory associated with Name for
    Return Value: Returns a string containing the requested information if it is present in the directory, otherwise returning None.
    '''
    sub_dict = Directory.setdefault(Name, {'Username':Name[:3]})
    return sub_dict.get(Field, None)

def create_lists(file_name):
    '''
    Purpose: Creates a dictionary from the passed in file with each key being a store name from the first column. The values
    associated with those keys are nested dictionaries, with the keys being the name of the item to purchase. The values associated
    with these nested dictionary keys are the integer sum of the number of items to buy at that store.
    Parameter(s): file_name- String representing the file path for the checklist csv.
    Return Value: Returns a dictionary as described in the purpose section.
    '''
    with open(file_name) as file:
        dictionary = {}
        for row in file:
            split_row = row.split(',')
            dictionary.setdefault(split_row[0],{split_row[1]:0})
            dictionary[split_row[0]][split_row[1]] = dictionary[split_row[0]].get(split_row[1],0) + int(split_row[2])
    return dictionary


if __name__ == "__main__":
    '''print(find_the_mins({"One": [1, 2, 3],
    "Two": [4, 5, 6],
    "Three": [44, 41, 41]}))
    print(find_the_mins({"X": [-1, 3, -33, 100],
  "Y": [], "Z": [1, 1, 0],
  "W": [3]}))
    print(find_the_mins({
        	"In": [12, 100, 72, 74, 11, 89],
        	"Out": [14, 100],
        	"Failed": [-1, 0, 0, 1],
        	"Queued": [3],}))'''
    #End of Problem A test cases

    ''' a_dict = {'Lee': {'Phone': '643-756-5612', 'Email': 'example@umn.edu', 'Username': 'Lee'},
    'Katie': {'Email': 'test_email@gmail.com', 'Username': 'Kat'},
    'Amanda': {'Phone': '234-462-4513', 'Email':'no_email@yahoo.com',  'Username': 'Ama'},
    'Nat': {'Phone':'612-379-5234', 'Username': 'Nat'}}
    print(find_the_contact(a_dict, "Lee", "Phone"))
    print(find_the_contact(a_dict, "Nat", "Email"))
    print(find_the_contact(a_dict, "Abi", "Email"))
    print(find_the_contact(a_dict, "Abby", "Username"))
    print(a_dict)'''
    #End of Problem B test cases

    #print(create_lists('small.csv'))
    #print(create_lists('medium.csv'))
    print(create_lists('large.csv'))




