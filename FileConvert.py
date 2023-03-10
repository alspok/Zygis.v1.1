from Classes.ModifyCSV import ModifyCSV
from Classes.MergeFiles import MergeFiles
from Classes.FilterCSV import FilterCSV
from Classes.InitValues import InitValues as iv

def FileConvert():
    modifyCSV = ModifyCSV()
    
    modifyCSV.actionPrice("Action_PriceList_2_1_2023_EN.csv")
    modifyCSV.eeteuroparts("eeteuroparts.csv")
    modifyCSV.stockExportFull("stock_export_full_for_zygimantas@ademi.lt.xml")


    # MergeFiles().mergeFiles()
    # FilterCSV().filterCSV()

if __name__ == "__main__":
    FileConvert()