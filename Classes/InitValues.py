class InitValues():
    input_path = "DataInputFiles\\"
    output_path = "DataOutputFiles\\"
    merge_path = "MergeFiles\\"

    csv_header = [
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

    merge_file_names = [
        "DataOutputFiles\\b2bindividuelllive_b2bexport1de.csv.mod.csv", # NOTEBOOKBILINGER
        "DataOutputFiles\\morele_offer.xml.mod.csv", # MORELE
        "DataOutputFiles\\ProductCatalogue_20230319122946.csv.mod.csv", # EPTIMO
        "DataOutputFiles\\stock_export_full_for_zygimantas@ademi.lt.xml.mod.csv" # INPRO
    ]
    merge_file_name = "MergeFiles\\b2b_morele_prodcat_stockexport.merge.csv"

    min_stock = 2
    min_price = 5.0
    threshold_price = 55.0
    low_increase_price = 1.63 # if price more then threshold
    large_increase_price = 1.98 # if price less then thershold
    uniform_increase_price = 2.3



