''' A simple Python table creation libary '''

__author__ = 'Lotus'
__version__ = '0.1'

class Table:
    """ Class responsible for
    constructing tables. """
    def __init__(self):
        self.length = 0
        self.content_count = 0

    def __repr__(self):
        return 'Table() class'

    def get_length(self):
        # len getter
        return self.length

    def get_content_count(self):
        # content count getter
        return self.content_count

    def repeat_char(self, char: str, n: int):
        return char*n

    def create_table(self, table_dict: dict):
        ''' Method responsible for mainly creating table '''
        # Creating string to be returned in this method
        full_table = ''

        # Getting longest key and item in given dict [@param(table_dict)]
        longest_key, longest_item = self.get_longest_elements(table_dict)
        longest_item

        # Constructing table closers [sep]
        h_closer1: str = '+' + self.repeat_char('=', longest_key+2) + '='
        h_closer2: str = self.repeat_char('=', longest_item+2) + '+'
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

    def get_longest_elements(self, dictionary: dict) -> int:
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
        print(key_list)
        print(item_list)

        # Index[0] -> longest key in dict; index[1] -> longest item in dict
        return [key_list[-1], item_list[-1]]


# appending sample dictionary [DEL]
sample_dictionary = {}
sample_dictionary['MyReally LONG value!'] = 'MY REALLY LOdaNG ITEM'
sample_dictionary['MyReally LONG valSAdasdasdue!'] = 'MY REALLY dasLONG ITEM'
sample_dictionary['MyReally LONG valsadaue!'] = 'MY REALLY LONGsdas ITEM'
sample_dictionary['MyReally LONG valasdasdasdasdadaue!'] = 'MY REALLYsda LONG ITEM'
sample_dictionary['MyReally LONG valuasdasdae!'] = 'MY REALLY LONGdasda ITEM'

# Creating a table
constructor = Table()
first_table = constructor.create_table(table_dict = sample_dictionary)

# Outputting table as well as checking table attributes (of most recent table)
print(first_table)
print('Dictionary Length: ', constructor.length)
print('Count of all items in table: ', constructor.content_count)
