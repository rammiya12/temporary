# The 'read_files' module allows you to:
#  - Read a CSV file (= comma-separated values) from the internet
#  - Build a Python address book from the CSV file. The address book will
#    allow you to quickly look up email addresses for all the Santas!


from urllib.request import urlopen


#####################
# Week 4, or after learning about dictionaries
#####################

# Given a dictionary, a key, and a value, adds the key and value to the
# dictionary.
#
# So if we have a dictionary:
# >>> address_book = {'Robin': 'robin@example.com', 'Ash': 'ash@example.com'}
#
# And then call this function with a new key and value:
# >>> add_to_dictionary(address_book, 'Meghana', 'meghana@example.com')
#
# The key and value get added to the dictionary:
# >>> address_book
# {'Robin': 'robin@example.com', 'Ash': 'ash@example.com', 'Meghana': 'meghana@example.com'}
def add_to_dictionary(dictionary, key, value):
    dictionary[key] = value

# Given a dictionary and a string with comma-separated key and value, adds the
# key and value to the dictionary.
#
# So if we have a dictionary:
# >>> address_book = {'Robin': 'robin@example.com', 'Ash': 'ash@example.com'}
#
# And then call this function with the dictionary and a string, like:
# >>> add_text_entry_to_dictionary(address_book, 'Meghana,meghana@example.com')
#
# The key and value extracted from the string get added to the dictionary:
# >>> address_book
# {'Robin': 'robin@example.com', 'Ash': 'ash@example.com', 'Meghana': 'meghana@example.com'}
def add_text_entry_to_dictionary(dictionary, text_with_comma):
    splitted = text_with_comma.split(',')
    dictionary[splitted[0]] = splitted[1]

# Builds a dictionary from scratch from a list of comma-separated text entries.
# Text entries are of the form "name,email".
#
# So if we have a list of text entries:
# >>> entries = ['Robin,robin@example.com', 'Ash,ash@example.com', 'Meghana,meghana@example.com']
#
# And we call this function with the list, we get a dictionary:
# >>> text_entries_to_dictionary(entries)
# {'Robin': 'robin@example.com', 'Ash': 'ash@example.com', 'Meghana': 'meghana@example.com'}
def text_entries_to_dictionary(participant_list):
    dct = {}
    for participant_csv in participant_list:
        add_text_entry_to_dictionary(dct, participant_csv)
    return dct

#####################
# Week 6, or after learning about reading from files and the web
#####################

# Given the name of a file, returns a list of strings. Each string corresponds
# to one line in the file.
#
# So if the file 'test.csv' contains:
# Robin,robin@example.com
# Ash,ash@example.com
# Meghana,meghana@example.com
#
# Then we get:
# >>> to_list_of_lines('test.csv')
# ['Robin,robin@example.com', 'Ash,ash@example.com', 'Meghana,meghana@example.com']
#
# Note that there are no new-line characters at the end of each entry!
def to_list_of_lines(input_file):
    pass

# Given a URL, returns a list of strings. Each string corresponds to one line
# read from the URL.
#
# For an example, see comment on to_list_of_lines.
def url_to_list_of_lines(url):
    pass

# Given a URL pointing to a CSV file (containing "name,email" on each line),
# builds an address book in dictionary form. The keys in the address book are
# names, and the values are the matching email addresses.
#
# Implement this by calling a couple of functions implemented earlier in this
# file.
def build_address_book(url):
    pass