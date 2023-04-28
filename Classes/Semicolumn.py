import csv

class Semicolumn():
    def semicolumn(self, file_name: str) -> str:
        output_file_name = f"{file_name}.csv"
        with open (f"{file_name}", mode='r', encoding='UTF-8') as scsv_fh, \
             open (f"{output_file_name}", mode='w', encoding='utf-8', newline='') as ccsv_fh:
            
            for line in scsv_fh:
                # mod_line = line.replace(',', '.').replace(';', ',').replace('Û', '€')
                mod_line = line.replace(',', '.').replace(';', ',')
                ccsv_fh.write(mod_line)
        
        return f"{output_file_name}"
    

    #{'ï»¿ItemId': '1584-50463', 'Brand': '226ers', 'Category': 'Sports nutrition', 'Name': 'ISOTONIC DRINK bebida isotÃ³nica #limÃ³n 1000 gr', 'Description': '', 'EAN': '8436567350463', 'RSP â\x82¬': '23.64', 'Special offer': 'No', 'Stock clearances': 'No', 'Stock': '0', 'Price from 1 unit â\x82¬': '20.18', 'Price from 24 units â\x82¬': '20.01', 'Price from 60 units â\x82¬': '19.75', 'Price from 120 units â\x82¬': '19.24'}
    # item['Price from 1 unit â\x82¬']#