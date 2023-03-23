import csv
from Classes.InitValues import InitValues as iv

class FilterCSV():

    def filterCSV(self) -> None:
        with open(iv.merge_file_name, mode='r', encoding='utf-8') as mfh:
            dictReader_obj = csv.DictReader(mfh)
            fsub_dict_list = []
            false_dict_list = []
            ean_list = []
            fail_nr = 0
            for item in dictReader_obj:
                try:
                    item['EAN'] = int(float(item['EAN']))
                    if item['EAN'] not in ean_list:
                        fsub_dict_list.append(item)
                        ean_list.append(item['EAN'])
                except:
                    fail_nr += 1
                    false_dict_list.append(item)
                    pass
        
        with open(iv.filter_file_name, mode='w', encoding='utf-8', newline='') as fcsv_fh:
            writer = csv.DictWriter(fcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(fsub_dict_list)

        pass