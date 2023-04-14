import csv

class ReadCSV():
    def readCSV(self, file_path: str, file_name: str) -> dict:
        with open(f"{file_path}{file_name}", mode='r', encoding='utf8') as csv_fh:
            dictReader_obj = csv.DictReader(csv_fh)
            sub_dict_list = []
            for item in dictReader_obj:
                sub_dict_list.append(item)
        
        return sub_dict_list
