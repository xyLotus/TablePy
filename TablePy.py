''' A simple Python table creation libary '''

class Table:
    def __init__(self):
        self.length = 0
        self.content_count = 0
        self.repeat_char('=', 10000)

    def repeat_char(self, char: str, n: int):
        return char*n

    def create_table(self, table_dict: dict):
        ''' Method responsible for creating table '''
        # Creating string to be returned in this method
        full_table = ''

        # Getting longest key and item in given dict [@param(table_dict)]
        longest_key, longest_item = self.get_longest_elements(table_dict)
        longest_item

        # Constructing table closers [sep]
        h_closer1: str = '+' + self.repeat_char('=', longest_key+2) + '='
        h_closer2: str = self.repeat_char('=', longest_item+2) + '+'
        full_h_closer: str = h_closer1 + h_closer2 + '\n'

        full_table += full_h_closer

        for key in table_dict.keys():
            key_spaces = longest_key - len(key)
            value_spaces = longest_item - len(table_dict[key])

            line_part1 = '| ' + key + ' '*key_spaces + ' | '
            line_part2 = table_dict[key] + ' '*value_spaces + ' |'
            full_line = line_part1 + line_part2 + '\n'

            full_table += full_line
        
        full_table += full_h_closer
        
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


table_dictionary = {}
table_dictionary['MyReally LONG value!'] = 'MY REALLY LOdaNG ITEM'
table_dictionary['MyReally LONG valSAdasdasdue!'] = 'MY REALLY dasLONG ITEM'
table_dictionary['MyReally LONG valsadaue!'] = 'MY REALLY LONGsdas ITEM'
table_dictionary['MyReally LONG valasdasdasdasdadaue!'] = 'MY REALLYsda LONG ITEM'
table_dictionary['MyReally LONG valuasdasdae!'] = 'MY REALLY LONGdasda ITEM'


my_table = Table()
table = my_table.create_table(table_dict = table_dictionary)

print(table)
print('Dictionary Length: ', my_table.length)
print('Count of all items in table: ', my_table.content_count)