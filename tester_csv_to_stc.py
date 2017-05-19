import csv_to_stc

if __name__=="__main__":
    csvTostc = csv_to_stc.CSVtoSTC("data_csv/","test_file.csv")
    csvTostc.execute("data_stc/test_file.stc")