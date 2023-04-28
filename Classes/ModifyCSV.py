import csv
# import xmltodict
import pprint
from Classes.InitValues import InitValues as iv
from xml.etree import ElementTree
from Classes.Semicolumn import Semicolumn
from Classes.ReadCSV import ReadCSV
from Classes.WriteCSV import WriteCSV

class ModifyCSV():

################################################ CSV modification ################################################

    # File to modify DataInputFiles\Action_PriceList_2_1_2023_EN.csv
    def actionPrice(self, file_name: str) -> None:
        # with open(f"{iv.input_path}{file_name}", mode='r', encoding='utf-8') as csv_fh:
        #     dictReader_obj = csv.DictReader(csv_fh)
        #     sub_dict_list = []
        #     for item in dictReader_obj:
        #         if float(item['Net price EUR']) >= iv.min_price:
        #             sub_dict_list.append(item)
        temp_file_name = f"{iv.input_path}{file_name}"
        sub_dict_list = ReadCSV().readCSV(temp_file_name)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            if item['EAN'] == '':
                continue
            else:
                sub_dict['EAN'] = int(item['EAN'])

            sub_dict['ITEM SKU'] = item['Manufacturer\'s code']
            sub_dict['PRODUCT NAME'] = item['Name of product']
            sub_dict['BRAND NAME'] = item['Producer']

            if float(item['Net price EUR']) <= iv.threshold_price:
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['Net price EUR']) * iv.large_increase_price, 2)
            else:
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['Net price EUR']) * iv.low_increase_price, 2)
            
            msub_dict_list.append(sub_dict)

        with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
            writer = csv.DictWriter(tcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(msub_dict_list)

        pass
    
    # Filie to modify DataInputFiles\eeteuroparts.csv
    def eeteuroparts(self, file_name: str) -> None:
        with open(f"{iv.input_path}{file_name}", mode='r', encoding='utf-8') as ssv_fh, \
                open(f"{iv.temp_output_path}{file_name}.temp.csv", mode='w', encoding='utf-8') as csv_fh:
            for line in ssv_fh:
                # mod_line = line.replace('\";\"', ',')
                mod_line = line.replace(',', '.').replace(';', ',')
                csv_fh.write(mod_line)

        with open(f"{iv.temp_output_path}{file_name}.temp.csv", mode='r', encoding='utf-8') as ssv_fh:
            dictReader_obj = csv.DictReader(ssv_fh)
            sub_dict_list = []
            for item in dictReader_obj:
                if float(item['Price']) >= iv.min_price:
                    sub_dict_list.append(item)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            if item['EAN/UPC'] == '':
                continue
            else:
                sub_dict['EAN'] = int(item["EAN/UPC"])

            sub_dict['ITEM SKU'] = item["Item Nr"]
            sub_dict['PRODUCT NAME'] = item["Description"]
            sub_dict['BRAND NAME'] = item["Brand Name"]
            if float(item['Price']) <= float(iv.threshold_price):
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item["Price"]) * iv.large_increase_price, 2)
            else:
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item["Price"]) * iv.low_increase_price, 2)
            msub_dict_list.append(sub_dict)

        with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
            writer = csv.DictWriter(tcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(msub_dict_list)

        pass




    # File to modify FRAGNANCES.csv
    def fragnances(self, file_name: str) -> None:
        with open(f"{iv.input_path}{file_name}", mode='r', encoding='utf-8') as csv_fh, \
                open(f"{iv.temp_output_path}{file_name}.temp.csv", mode='w', encoding='utf-8') as wcsv_fh:
            for line in csv_fh:
                mod_line = line.replace(',', '.').replace(';', ',')
                wcsv_fh.write(mod_line)

        with open(f"{iv.temp_output_path}{file_name}.temp.csv", mode='r', encoding='utf-8') as ssv_fh:
            dictReader_obj = csv.DictReader(ssv_fh)
            sub_dict_list = []
            for item in dictReader_obj:
                if float(item['PRICE']) >= iv.min_price:
                    sub_dict_list.append(item)
        
        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            if item['EAN'] == '':
                continue
            else:
                sub_dict['EAN'] = int(item['EAN'])
        
            sub_dict['ITEM SKU'] = item['\ufeff"id"']
            sub_dict['PRODUCT NAME'] = item['TITLE']
            sub_dict['BRAND NAME'] = item['BRAND']
            sub_dict['REQUIRED PRICE TO AMAZON'] = float(item['PRICE'])
            if sub_dict['REQUIRED PRICE TO AMAZON'] <= float(iv.threshold_price):
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] * iv.large_increase_price, 2)
            else:
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] * iv.low_increase_price, 2)
            
            if int(item['STOCK']) > iv.min_stock:
                msub_dict_list.append(sub_dict)

        with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
            writer = csv.DictWriter(tcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(msub_dict_list)

        pass

    # 
    def fragnancesSelect(self, file_name: str, column_name: str) -> None:
        """
        Args:
            file_name (str): csv file name.
            column_name (str): column name to select in csv file.
        Returns:
            Save results in file.
        """
        with open(f"{iv.input_path}{file_name}", mode='r', encoding='utf-8') as csv_fh, \
                open(f"{iv.temp_output_path}{file_name}.selected.temp.csv", mode='w', encoding='utf-8', newline='') as wcsv_fh:
            for line in csv_fh:
                mod_line = line.replace(',', '.').replace(';', ',')
                wcsv_fh.write(mod_line)

        with open(f"{iv.temp_output_path}{file_name}.selected.temp.csv", mode='r', encoding='utf-8') as ssv_fh:
            dictReader_obj = csv.DictReader(ssv_fh)
            item_select = []
            selected_list = []
            for item in dictReader_obj:
                if item[column_name] not in item_select:
                    item_select.append(item["BRAND"])
                    del item['\ufeff"id"']
                    del item[""]
                    selected_list.append(item)

        with open(f"{iv.output_path}{file_name}.selected.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
            writer = csv.DictWriter(tcsv_fh, fieldnames=iv.csv_fregrances_head)
            writer.writeheader()
            writer.writerows(selected_list)

        pass

    # File to modify DataInputFiles\ProductCatalogue_20230319122946.csv
    def productCatalogue_20230319122946(self, file_name: str) -> None:
        incrase_price = 1.42

        with open(f"{iv.input_path}{file_name}", mode='r', encoding = 'unicode_escape') as csv_fh, \
                open(f"{iv.temp_output_path}{file_name}.temp.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
            for line in csv_fh:
                mod_line = line.replace(',', '.').replace(';', ',')
                tcsv_fh.write(mod_line)

        with open(f"{iv.temp_output_path}{file_name}.temp.csv", mode='r', encoding='unicode_escape') as temp_csv_fh:
            dictReader_obj = csv.DictReader(temp_csv_fh)
            sub_dict_list = []
            for item in dictReader_obj:
                sub_dict_list.append(item)

            msub_dict_list = []
            for item in sub_dict_list:
                sub_dict = dict()
                try:
                    sub_dict['EAN'] = item['ItemEAN']
                    sub_dict['ITEM SKU'] = item['ItemPartNumber']
                    sub_dict['PRODUCT NAME'] = item['Name']
                    sub_dict['BRAND NAME'] = item['BrandName']
                    sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['PriceNett']) * incrase_price, 2)
                    # sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['PriceNett'] * incrase_price), 2)

                    msub_dict_list.append(sub_dict)
                except:
                    pass
            
        with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as mcsv_fh:
            writer = csv.DictWriter(mcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(msub_dict_list)

        pass

    # File to nodify DataInputFiles\b2bindividuelllive_b2bexport1de.csv
    def b2bindividuelllive(self, file_name: str) -> None:
        threshold_price = 70.0
        low_increase_price = 1.8 # if price more then threshold
        large_increase_price = 1.42 # if price less then thershold

        with open(f"{iv.input_path}{file_name}", mode='r', encoding = 'unicode_escape') as csv_fh, \
             open(f"{iv.temp_output_path}{file_name}.temp.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
            for line in csv_fh:
                mod_line = line.replace(',', '.').replace(';', ',')
                tcsv_fh.write(mod_line)

        with open(f"{iv.temp_output_path}{file_name}.temp.csv", mode='r', encoding='unicode_escape') as temp_csv_fh:
            dictReader_obj = csv.DictReader(temp_csv_fh)
            sub_dict_list = []
            for item in dictReader_obj:
                sub_dict_list.append(item)

            msub_dict_list = []
            for item in sub_dict_list:
                sub_dict = dict()
                try:
                    sub_dict['EAN'] = item['products_ean']
                    sub_dict['ITEM SKU'] = item['SKU']
                    sub_dict['PRODUCT NAME'] = item['productName']
                    sub_dict['BRAND NAME'] = item['manufacturer']
                    sub_dict['REQUIRED PRICE TO AMAZON'] = float(item['NetPrice'])
                    # stock_value = int(item['stock'])

                    if sub_dict['REQUIRED PRICE TO AMAZON'] < threshold_price:
                        sub_dict['REQUIRED PRICE TO AMAZON'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] * low_increase_price, 2)
                    else:
                        sub_dict['REQUIRED PRICE TO AMAZON'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] * large_increase_price, 2)
                    
                    msub_dict_list.append(sub_dict)
                except:
                    pass

        with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as mcsv_fh:
            writer = csv.DictWriter(mcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(msub_dict_list)

        pass

    #File to modify DataInputFiles\EPTIMO_InventoryReport_20230412191230.csv
    def eptimo(self, file_name: str) -> None:
        increase_price = 1.42
        limit_price = 15
        available_qty = 5

        temp_file_name = f"{iv.input_path}{file_name}"
        # temp_file_name = Semicolumn().semicolumn(temp_file_name) # EPTIMO_InventoryReport_20230412191230.csv
        sub_dict_list = ReadCSV().readCSV(temp_file_name)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = int(item['ItemEAN'])
                sub_dict['ITEM SKU'] = item['ItemPartNumber']
                sub_dict['PRODUCT NAME'] = item['Name']
                sub_dict['BRAND NAME'] = item['BrandName']
                sub_dict['ORIGINAL PRICE'] = float(item['PriceNett'])
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['PriceNett']) * increase_price, 2)
                sub_dict['PRICE DEVISION'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] / sub_dict['ORIGINAL PRICE'], 2)
                if int(float(item['AvailableQty'])) >= available_qty and int(sub_dict['REQUIRED PRICE TO AMAZON']) >= limit_price:
                    sub_dict['STOCK'] = int(float(item['AvailableQty']))
                    msub_dict_list.append(sub_dict)
                else:
                    continue
            except:
                pass
        
        mod_file_name = f"{iv.temp_output_path}{file_name}.temp"
        key_list_head = list(sub_dict.keys())
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, key_list_head)

        sub_dict_list = ReadCSV().readCSV(mod_file_name)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['ITEM SKU']
                sub_dict['PRODUCT NAME'] = item['PRODUCT NAME']
                sub_dict['BRAND NAME'] = item['BRAND NAME']
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['ORIGINAL PRICE']) * increase_price, 2)
                # sub_dict['STOCK'] = int(item['STOCK'])
                if int(item['STOCK']) >= available_qty:
                    msub_dict_list.append(sub_dict)
            except:
                pass
                
        mod_file_name = f"{iv.output_path}{file_name}.mod"
        key_list_head = list(sub_dict.keys())
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, key_list_head)

        pass

    def novaengel(self, file_name: str) -> None:
        increase_price = 1.52
        limit_price = 15
        available_qty = 5

        temp_file_name = f"{iv.input_path}{file_name}"
        temp_file_name = Semicolumn().semicolumn(temp_file_name) # 'DataOutputTempFiles\\NOVAENGEL.csv.csv'
        sub_dict_list = ReadCSV().readCSV(temp_file_name)

        msub_dict_list = []
        ean_count = 0
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['\ufeffItemId'] #'\ufeffItemId'
                sub_dict['PRODUCT NAME'] = item['Name']
                sub_dict['BRAND NAME'] = item['Brand']

                sub_dict['ORIGINAL PRICE'] = float(item['Price from 1 unit €'])
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['Price from 1 unit €']) * increase_price, 2)
                sub_dict['PRICE DEVISION'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] / sub_dict['ORIGINAL PRICE'], 2)
                if int(item['Stock']) >= available_qty and int(sub_dict['REQUIRED PRICE TO AMAZON']) >= limit_price:
                    sub_dict['STOCK'] = item['Stock']
                    msub_dict_list.append(sub_dict)
            except:
                pass

        mod_file_name = f"{iv.temp_output_path}{file_name}.temp"
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, iv.csv_temp_head)

        sub_dict_list = ReadCSV().readCSV(mod_file_name)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['ITEM SKU']
                sub_dict['PRODUCT NAME'] = item['PRODUCT NAME']
                sub_dict['BRAND NAME'] = item['BRAND NAME']
                sub_dict['REQUIRED PRICE TO AMAZON'] = float(item['REQUIRED PRICE TO AMAZON'])
                msub_dict_list.append(sub_dict)
            except:
                pass

        out_file_name = f"{iv.output_path}{file_name}.mod"
        WriteCSV().writeCSV(out_file_name, msub_dict_list, iv.csv_head)

        pass

    def ab_pl(self, file_name: str) -> None:
        increase_price = 1.42
        limit_price = 100

        temp_file_name = f"{iv.input_path}{file_name}"
        temp_file_name = Semicolumn().semicolumn(temp_file_name) # AB_PL.csv.csv
        sub_dict_list = ReadCSV().readCSV(temp_file_name)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['SKU']
                sub_dict['PRODUCT NAME'] = item['TITLE']
                sub_dict['BRAND NAME'] = item['BRAND']
                sub_dict['ORIGINAL PRICE'] = float(item['PRICE'])
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float( item['PRICE']) * increase_price, 2)
                sub_dict['PRICE DEVISION'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] / sub_dict['ORIGINAL PRICE'], 2)
                msub_dict_list.append(sub_dict)
            except:
                pass

        mod_file_name = f"{iv.temp_output_path}{file_name}.temp"
        key_list_head = list(sub_dict.keys())
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, key_list_head)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['SKU']
                sub_dict['PRODUCT NAME'] = item['TITLE']
                sub_dict['BRAND NAME'] = item['BRAND']
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float( item['PRICE']) * increase_price, 2)
                if int(sub_dict['REQUIRED PRICE TO AMAZON']) >= limit_price:
                    msub_dict_list.append(sub_dict)
            except:
                pass

        mod_file_name = f"{iv.output_path}{file_name}.mod"
        key_list_head = list(sub_dict.keys())
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, key_list_head)

        pass


    def skorpionas(self, file_name: str) -> None:
        increase_price = 1.48
        limit_price = 100

        temp_file_name = f"{iv.input_path}{file_name}"
        temp_file_name = Semicolumn().semicolumn(temp_file_name) # AB_PL.csv.csv
        sub_dict_list = ReadCSV().readCSV(temp_file_name)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['SKU']
                sub_dict['PRODUCT NAME'] = item['TITLE']
                sub_dict['BRAND NAME'] = item['BRAND']
                sub_dict['ORIGINAL PRICE'] = float(item['PRICE'])
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float( item['PRICE']) * increase_price, 2)
                sub_dict['PRICE DEVISION'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] / sub_dict['ORIGINAL PRICE'], 2)
                msub_dict_list.append(sub_dict)
            except:
                pass

        mod_file_name = f"{iv.temp_output_path}{file_name}.temp"
        key_list_head = list(sub_dict.keys())
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, key_list_head)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['SKU']
                sub_dict['PRODUCT NAME'] = item['TITLE']
                sub_dict['BRAND NAME'] = item['BRAND']
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float( item['PRICE']) * increase_price, 2)
                if int(sub_dict['REQUIRED PRICE TO AMAZON'] >= limit_price):
                    msub_dict_list.append(sub_dict)
            except:
                pass

        mod_file_name = f"{iv.output_path}{file_name}.mod"
        key_list_head = list(sub_dict.keys())
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, key_list_head)

        pass

    def elko(self, file_name: str) -> None:
        increase_price = 1.42
        limit_price = 100

        temp_file_name = f"{iv.input_path}{file_name}"
        temp_file_name = Semicolumn().semicolumn(temp_file_name) # AB_PL.csv.csv
        sub_dict_list = ReadCSV().readCSV(temp_file_name)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['SKU']
                sub_dict['PRODUCT NAME'] = item['TITLE']
                sub_dict['BRAND NAME'] = item['BRAND']
                sub_dict['ORIGINAL PRICE'] = float(item['PRICE'])
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float( item['PRICE']) * increase_price, 2)
                sub_dict['PRICE DEVISION'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] / sub_dict['ORIGINAL PRICE'], 2)
                msub_dict_list.append(sub_dict)
            except:
                pass

        mod_file_name = f"{iv.temp_output_path}{file_name}.temp"
        key_list_head = list(sub_dict.keys())
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, key_list_head)

        msub_dict_list = []
        for item in sub_dict_list:
            sub_dict = dict()
            try:
                sub_dict['EAN'] = item['EAN']
                sub_dict['ITEM SKU'] = item['SKU']
                sub_dict['PRODUCT NAME'] = item['TITLE']
                sub_dict['BRAND NAME'] = item['BRAND']
                sub_dict['REQUIRED PRICE TO AMAZON'] = round(float( item['PRICE']) * increase_price, 2)
                if int(sub_dict['REQUIRED PRICE TO AMAZON']) >= limit_price:
                    msub_dict_list.append(sub_dict)
            except:
                pass

        mod_file_name = f"{iv.output_path}{file_name}.mod"
        key_list_head = list(sub_dict.keys())
        WriteCSV().writeCSV(mod_file_name, msub_dict_list, key_list_head)

        pass


################################################ XML modification ################################################

    # File to modify DataInputFiles\stock_export_full_for_zygimantas@ademi.lt.xml
    def stockExportFull(self, file_name: str) -> None:
        threshold_price = 70.0
        low_increase_price = 1.8 # if price more then threshold
        large_increase_price = 1.42 # if price less then thershold

        with open(f"{iv.input_path}{file_name}", mode='r', encoding='utf-8') as xml_fh:
            xml_date = xml_fh.read()
            xml_dict = xmltodict.parse(xml_date)

        xml_dict_list =[]
        [xml_dict_list.append(dict(x)) for x in xml_dict['offer']['products']['product']]

        mod_dict_list = []
        for item in xml_dict_list:
            sub_dict_list = {}
            try:
                sub_dict_list['EAN'] = item['sizes']['size']['@iaiext:code_external']
                sub_dict_list['ITEM SKU'] = item['sizes']['size']['@code_producer']
                sub_dict_list['BRAND NAME'] = item['producer']['@name']
                sub_dict_list['PRODUCT NAME'] = item['description']['name'][0]['#text']
                sub_dict_list['REQUIRED PRICE TO AMAZON'] = float(item['price']['@net'])
                stock_value = int(float(item['sizes']['size']['stock']['@available_stock_quantity']))
                if stock_value < iv.min_stock or sub_dict_list['REQUIRED PRICE TO AMAZON'] < float(iv.min_price):
                    continue
                else:
                    if sub_dict_list['REQUIRED PRICE TO AMAZON'] <= threshold_price:
                        sub_dict_list['REQUIRED PRICE TO AMAZON'] = round(sub_dict_list['REQUIRED PRICE TO AMAZON'] * large_increase_price, 2)
                        mod_dict_list.append(sub_dict_list)
                    else:
                        sub_dict_list['REQUIRED PRICE TO AMAZON'] = round(sub_dict_list['REQUIRED PRICE TO AMAZON'] * low_increase_price, 2)
                        mod_dict_list.append(sub_dict_list)
            except:
                pass

        with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
            writer = csv.DictWriter(tcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(mod_dict_list)

    # File to modify DataInputFiles\morele_offer.xml
    def morele(self, file_name: str) -> None:
        threshold_price = 70.0
        low_increase_price = 1.8 # if price more then threshold
        large_increase_price = 1.42 # if price less then thershold

        with open(f"{iv.input_path}{file_name}", mode='r', encoding='utf-8') as xml_fh:
            xml_date = xml_fh.read()
            xml_dict = xmltodict.parse(xml_date)

        xml_dict_list =[]
        [xml_dict_list.append(dict(x)) for x in xml_dict['products']['product']]

        msub_dict_list = []
        for item in xml_dict_list:
            sub_dict = {}
            try:
                sub_dict['EAN'] = item['productEan']
                sub_dict['ITEM SKU'] = item['productCode']
                sub_dict['BRAND NAME'] = item['brandName']
                sub_dict['PRODUCT NAME'] = item['productFullName']
                sub_dict['REQUIRED PRICE TO AMAZON'] = float(item['productEuroPriceNetto'])

                if sub_dict['REQUIRED PRICE TO AMAZON'] < threshold_price:
                    sub_dict['REQUIRED PRICE TO AMAZON'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] * low_increase_price, 2)
                else:
                    sub_dict['REQUIRED PRICE TO AMAZON'] = round(sub_dict['REQUIRED PRICE TO AMAZON'] * large_increase_price, 2)
                    
                msub_dict_list.append(sub_dict)
            except:
                pass

        with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as mcsv_fh:
            writer = csv.DictWriter(mcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(msub_dict_list)

        pass
            