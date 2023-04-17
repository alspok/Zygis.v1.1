from Classes.ReadCSV import ReadCSV
from Classes.WriteCSV import WriteCSV
from Classes.InitValues import InitValues as iv


class MergeFilter():
    def mergeFilter(self, file_list: list) -> None:
        merge_dict_list = []
        count_same = 0
        for file in file_list:
            sub_dict_list = ReadCSV().readCSV(file)
            for item in sub_dict_list:
                try:
                    merge_dict_list.append(item)
                except:
                    pass

        fmerge_dict_list = []
        filter_dict_list = []
        for item in merge_dict_list:
            if item['EAN'] not in filter_dict_list:
                fmerge_dict_list.append(item)
                filter_dict_list.append(item['EAN'])
            else:
                count_same += 1
                continue
        
        merge_file_name = f"{iv.merge_path}{iv.merge_file}.filter"
        key_list_head = list(item.keys())
        WriteCSV().writeCSV(merge_file_name, fmerge_dict_list, key_list_head)

        pass
