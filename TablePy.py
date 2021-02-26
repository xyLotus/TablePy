''' A simple Python table creation libary '''

__author__ = 'Lotus'
__version__ = '0.3'

def repeat_char(char: str, n_times: int):
    """ This function repeats the given char [@param1]
    n-times [@param2] """
    return char*n_times

def get_longest_elements(dictionary: dict) -> int:
    """ Method responsible for returning longest
    key & value in given dict [@param] """

    # appending both tuples with dictionary key 'n corresponding item
    key_list = []
    item_list = []
    for key in dictionary.keys():
        key_list.append(len(key))

    for key in dictionary.keys():
        item_list.append(len(dictionary[key]))

    # Sorting the, now appended, lists the easy way...
    key_list.sort()
    item_list.sort()

    # Index[0] -> longest key in dict; index[1] -> longest item in dict
    return [key_list[-1], item_list[-1]]


class Table:
    """ Class responsible for
    constructing tables. """
    def __init__(self, table_dict):
        self.table_dict = table_dict
        self.length = 0
        self.content_count = 0

    def __repr__(self):
        return 'Table() class'

    def __str__(self):
        return self.create_table(self.table_dict)

    def get_length(self):
        """ Method getting length attr """
        # len getter
        return self.length

    def get_content_count(self):
        """ Method getting content_count attr """
        # content count getter
        return self.content_count

    def create_table(self, table_dict: dict):
        ''' Method responsible for mainly creating table '''
        # Creating string to be returned in this method
        full_table = ''

        # Getting longest key and item in given dict [@param(table_dict)]
        longest_key, longest_item = get_longest_elements(table_dict)

        # Constructing table closers [sep]
        h_closer1: str = '+' + repeat_char('=', longest_key+2) + '='
        h_closer2: str = repeat_char('=', longest_item+2) + '+'
        full_h_closer: str = h_closer1 + h_closer2 + '\n'

        # appending top hCloser to return value
        full_table += full_h_closer

        # Writing each line in table iterative and appending to return value
        for key in table_dict.keys():
            # calculating spaces needed for every seperator to be evenly spaced
            key_spaces = longest_key - len(key)
            value_spaces = longest_item - len(table_dict[key])

            # constructing current line
            line_part1 = '| ' + key + ' '*key_spaces + ' | '
            line_part2 = table_dict[key] + ' '*value_spaces + ' |'
            full_line = line_part1 + line_part2 + '\n'

            # appending each line to return value
            full_table += full_line

        # appending bottom hCloser to return value
        full_table += full_h_closer

        # setting class attributes
        self.length = len(table_dict.keys())
        self.content_count = len(table_dict.keys()) * 2

        return full_table

