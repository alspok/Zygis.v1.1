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

    min_stock = 2
    min_price = 5
    threshold_price = 55.0
    low_increase_price = 1.42 # if price more then threshold
    large_increase_price = 1.8 # if price less then thershold



