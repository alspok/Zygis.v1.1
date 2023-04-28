import csv
import codecs
from Classes.InitValues import InitValues as iv

class ReadCSV():
    def readCSV(self, file_name: str) -> dict:
        with codecs.open(file_name, mode='r', encoding='utf-8', errors='ignore') as csv_fh:
            dictReader_obj = csv.DictReader(csv_fh)
            sub_dict_list = []
            for item in dictReader_obj:
                sub_dict_list.append(item)
        
        return sub_dict_list
