import csv
from Classes.InitValues import InitValues as iv

class FilterCSV():

    def filterCSV(self) -> None:
        with open(iv.merge_file_name, mode='r', encoding='utf-8') as mfh:
            dictReader_obj = csv.DictReader(mfh)

            fsub_dict_list = []
            ean_list = []
            match_nr = 0
            for item in dictReader_obj:
                if item['EAN'] == '' or not item['EAN'].isdigit():
                    continue
                elif item['EAN'] not in ean_list:
                    item['EAN'] = int(float(item['EAN']))
                    fsub_dict_list.append(item)
                    ean_list.append(item['EAN'])
                else:
                    match_nr += 1
                    continue
        
        with open(iv.filter_file_name, mode='w', encoding='utf-8', newline='') as fcsv_fh:
            writer = csv.DictWriter(fcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(fsub_dict_list)

        pass