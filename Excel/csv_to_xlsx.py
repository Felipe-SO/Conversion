import pandas as pd
import os

# Converts .csv to .xlsx.
# Insert the path (as a string) to the exact folder where your files are.
def csv_xlsx(path):
    for file in os.listdir(path):
        lencsv=len(file)
        if file.endswith(".csv")==True:
            if "%s.xlsx"%(file[0:lencsv-4]) in os.listdir(path):
                print("%s.xlsx already exists." %(file[0:lencsv-4]))
            else:
                os.chdir(path)
                Data = pd.read_csv(file,index_col=0)
                Data.to_excel("%s.xlsx"%(file[0:lencsv-4]))
                print("Created %s.xlsx from %s." % (file[0:lencsv-4],file))
            
