class InitValues():
    input_path = "DataInputFiles\\"
    output_path = "DataOutputFiles\\"
    temp_output_path = "DataOutputTempFiles\\"
    merge_path = "MergeFiles\\"

    csv_header = [
        "EAN",
        "ITEM SKU",
        "PRODUCT NAME",
        "BRAND NAME",
        "REQUIRED PRICE TO AMAZON" 
    ]

    #copy of csv_header
    csv_head = [
        "EAN",
        "ITEM SKU",
        "PRODUCT NAME",
        "BRAND NAME",
        "REQUIRED PRICE TO AMAZON" 
    ]

    csv_action_pricelist_head = [
        "Manufacturer\'s code",
        "Name of product",
        "Producer",
        "EAN",
        "Net price EUR"
    ]

    csv_eeteuroparts_head = [
        "Item Nr",
        "Description",
        "Brand Name",
        "EAN/UPC",
        "Price"
    ]

    csv_fregrances_head = [
        "BRAND",
        "TITLE",
        "TYPE",
        "SEX",
        "VOLUME",
        "NOTE",
        "SET",
        "STOCK",
        "PRICE",
        "CURRENCY",
        "NEWS",
        "BACK IN",
        "EAN",
        "TESTER",
        "DAMAGED",
        "SHADE",
    ]

    csv_eptimo_head = [
        "EAN",
        "ITEM SKU",
        "PRODUCT NAME",
        "BRAND NAME",
        "ORIGINAL PRICE",
        "REQUIRED PRICE TO AMAZON",
        "PRICE DEVISION",
        "STOCK"
    ]

    merge_file_names = [
        "DataOutputFiles\\b2bindividuelllive_b2bexport1de.csv.mod.csv", # NOTEBOOKBILINGER
        "DataOutputFiles\\morele_offer.xml.mod.csv", # MORELE
        "DataOutputFiles\\ProductCatalogue_20230319122946.csv.mod.csv", # EPTIMO
        "DataOutputFiles\\stock_export_full_for_zygimantas@ademi.lt.xml.mod.csv" # INPRO
    ]
    merge_file_name = "MergeFiles\\b2b_morele_prodcat_stockexport.merge.csv"
    filter_file_name = "MergeFiles\\b2b_morele_prodcat_stockexport.filter.csv"

    min_stock = 2
    min_price = 5.0
    threshold_price = 55.0
    low_increase_price = 1.63 # if price more then threshold
    large_increase_price = 1.98 # if price less then thershold
    uniform_increase_price = 2.3



