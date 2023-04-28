import csv
from Classes.InitValues import InitValues as iv

class WriteCSV():
    def writeCSV(self, file_name: str, dict_list: dict, csv_head: list) -> None:
        with open(f"{file_name}", mode='w', encoding='utf-8', newline='') as mod_csv_fh:
            writer = csv.DictWriter(mod_csv_fh, fieldnames=csv_head)
            writer.writeheader()
            writer.writerows(dict_list)

        pass