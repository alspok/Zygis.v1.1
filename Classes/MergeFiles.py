from Classes.InitValues import  InitValues as iv
import pandas as pd

class MergeFiles():

    def mergeFiles(self, merge_files: list) -> None:
        file_count = True
        for file in iv.merge_files:
            if file_count:
                with open(file, mode='r', encoding='latin-1') as fh, \
                     open(iv.merge_file_name, mode='w', encoding='latin', newline='') as mfh:
                    mfile = fh.read()
                    mfh.write(mfile)
                    file_count = False
            else:
                with open(file, mode='r', encoding='latin-1') as fh, \
                     open(iv.merge_file_name, mode='a', encoding='latin-1', newline='') as mfh:
                    for line in fh:
                        if "ITEM SKU" in line and "BRAND NAME" in line:
                            continue
                        else:
                            mfh.write(line)
        
        pass

    def mergeCSVFiles(self) -> None:
        csv_merge = pd.DataFrame()
        for file in iv.merge_file_names:
            temp_file = pd.read_csv(file)
            csv_merge = csv_merge.append(temp_file, ignore_index=True)
        
        csv_merge.to_csv(iv.merge_file_name, index=False)
        # with open(f"{iv.merge_path}{iv.merge_file}", mode='w', encoding='utf-8', newline='') as csv_fh:
            # csv_fh.write(csv_merge.to_csv())