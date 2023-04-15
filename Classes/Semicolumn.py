from Classes.InitValues import InitValues as iv

class Semicolumn():
    def semicolumn(self, file_name: str) -> str:
        output_file_name = f"{file_name}.csv"
        with open (f"{file_name}", mode='r', encoding='utf8') as scsv_fh, \
             open (f"{output_file_name}", mode='w', encoding='utf8', newline='') as ccsv_fh:
            for line in scsv_fh:
                mod_line = line.replace(',', '.').replace(';', ',')
                ccsv_fh.write(mod_line)
        
        return f"{output_file_name}"
