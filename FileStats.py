import pandas as pd
from textblob import TextBlob
from FileParserHander import FileParserHandler

class FileStats:

    whats_app_list = []

    def __init__(self):
        pass

    # Control Test
    def control_test(self):
        convo_to_analyze1 = "I am happy today!"
        convo_to_analyze2 = "I am sad today!"
        tb1 = TextBlob(convo_to_analyze1)
        tb2 = TextBlob(convo_to_analyze2)
        print("This is a test:")
        print(tb1.sentiment)
        print(tb2.sentiment)

    # Sentiment cal eval
    # Calculated using TextBlob
    def sentiment_eval(self):
        convo_to_analyze = ""
        fph = FileParserHandler()
        whats_app_list = fph.split_at_regex()
        for o in whats_app_list:
            if o.get_name() == "Eoin Payne In The Ass":
                convo_to_analyze = convo_to_analyze + o.get_message()

        tb = TextBlob(convo_to_analyze)
        print("Convo analysis: ")
        print(tb.sentiment)




if __name__ == "__main__":

    fs = FileStats()
    fs.control_test()
    fs.sentiment_eval()















