import csv
from Classes.InitValues import InitValues as iv

class FilterCSV():

    # Filter CSV file using particular fiel
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

    # Count keys in dictionary
    def countCSV(self) -> None:
        with open(iv.filter_file_name, mode='r', encoding='utf-8') as fcsv_fh:
            dictReader_obj = csv.DictReader(fcsv_fh)

            field_list = []
            for item in dictReader_obj:
                field_list.append(item['REQUIRED PRICE TO AMAZON'])

        count_dict = {}
        for item in field_list:
            count = field_list.count(item)
            if count > 170:
                print(item, count)
                count_dict[item] = count

        pass
