import shutil
from os import rename
import csv_to_stc
import run_exe_DBGen as DBGen



# file_stc contiene extencion, y debe estar separado de su path
# Hacemos una copia de PlotDEX.plt y le cambiamos de nombre
def save_PlotDEX(file_stc,file_plotDEX,path_plot):
    name_plot = str(file_stc).split(".")
    name_plot = name_plot[0]

    shutil.copy(file_plotDEX, path_plot)
    rename(path_plot+file_plotDEX,path_plot + name_plot + ".plt")

# RETORNAMOS: Dimension del Fractal y
#
def read_plot(path, filename):
    file = open(path + filename, "r")
    text = file.readlines()
    # Sacamos la dimension fractal del archivo
    dimension_fractal = str(text[2]).split("*")
    dimension_fractal = dimension_fractal[0].split(" ")
    pos = len(dimension_fractal)
    dimension_fractal = float(dimension_fractal[pos-1])

    # Sacamos el Log(R)
    log_R = str(text[5]).split(" ")
    log_R = float(log_R[0])

    file.close()

    return  dimension_fractal,log_R

# ------------------------------ MAIN ----------------------------------
if __name__ == "__main__":
    path_csv = "data_csv/"
    path_stc = "data_stc/"
    file_csv = "test_file.csv"
    file_name = file_csv.split(".")[0]
    exe_mde = "mde2.exe"

    pathPlot = "data_plot/"
    filePlotDEX = "PlotDEX.plt"

    # Convertir un archivo CSV a STC
    csvTostc = csv_to_stc.CSVtoSTC(path_csv, file_csv)
    csvTostc.execute(path_stc + file_name + ".stc")

    # Correr MDE2 para generar el PLT, donde estara la dimension fractal
    DBGenObj = DBGen.RunDBGen(path_stc, exe_mde)
    DBGenObj.execute(path_stc + file_name + ".stc")

    save_PlotDEX(file_stc=file_name + ".stc",file_plotDEX=filePlotDEX,path_plot=pathPlot)
    dim_f,logR = read_plot(pathPlot,file_name + ".plt")
    print(dim_f,logR)