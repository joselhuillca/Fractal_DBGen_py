import run_exe_DBGen as DBGen

if __name__ == "__main__":
    DBGenObj = DBGen.RunDBGen("data_stc/","mde2.exe")
    DBGenObj.execute("data_stc/cities.stc")