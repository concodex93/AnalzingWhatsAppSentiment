# import FileHandler
import re
from FileHandler import read_file
from WhatsApp import WhatsApp


class FileParserHandler:

    # content = []
    all_extra_removed_list = []
    # split_dash_list = []
    # black_space = []
    # result = []
    # name_list = []
    # message_list = []
    # package_list = []


    whats_app_list = []


    def __init__(self):
        pass
    # Splits string at dash
    # Allows access to name and message data in line
    def split_at_regex(self):

        content = read_file()

        pattern = r"\d{2}\/\d{2}\/\d{4}, \d{2}:\d{2} - "

        temp_list = re.split(pattern, content)

        for t in temp_list:
            index = t.find(":")
            name = t[:index]
            message = t[index + 1:]
            whats_app = WhatsApp(name, message)
            self.whats_app_list.append(whats_app)

            # print("name: " + str(name))
            # print("message: " + str(message))

        return self.whats_app_list

if __name__ == "__main__":
    file_parser_handler = FileParserHandler()
    result1 = file_parser_handler.split_at_regex()
    for o in result1:
        print(o.get_name())



