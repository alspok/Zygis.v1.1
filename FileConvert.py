from Classes.ModifyCSV import ModifyCSV
from Classes.MergeFiles import MergeFiles
from Classes.FilterCSV import FilterCSV
from Classes.InitValues import InitValues as iv

def FileConvert():
    modifyCSV = ModifyCSV()

    # modifyCSV.actionPrice("Action_PriceList_2_1_2023_EN.csv")
    # modifyCSV.eeteuroparts("eeteuroparts.csv")
    # modifyCSV.stockExportFull("stock_export_full_for_zygimantas@ademi.lt.xml")
    # modifyCSV.fragnances("FRAGNANCES.csv")
    # modifyCSV.productCatalogue_20230319122946("ProductCatalogue_20230319122946.csv")
    # modifyCSV.b2bindividuelllive("b2bindividuelllive_b2bexport1de.csv")
    # modifyCSV.morele("morele_offer.xml")

    # MergeFiles().mergeCSVFiles()
    # FilterCSV().filterCSV()
    # FilterCSV().countCSV()
    # modifyCSV.fragnancesSelect("fragnances.csv", "BRAND")
    # modifyCSV.eptimo('EPTIMO_InventoryReport_20230412191230.csv')
    modifyCSV.novaengel("NOVAENGEL.csv")

if __name__ == "__main__":
    FileConvert()