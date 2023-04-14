import csv

class Semicolumn():
    def semicolumn(file_name: str) -> None:
        output_file_name = f"{file_name}.csv"
        with open (f"{file_name}", mode='r', encoding='utf8') as scsv_fh, \
             open (f"{output_file_name}", mode='w', encoding='utf8', newline='') as ccsv_fh:
            for line in scsv_fh:
                mod_line = line.replace(',', '.').replace(';', ',')
                ccsv_fh.write(mod_line)
        
        pass
