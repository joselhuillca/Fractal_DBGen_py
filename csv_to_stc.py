
from numpy import genfromtxt
import numpy as np

class CSVtoSTC:
    def __init__(self,path,filename):
        self.path = path
        self.filename= filename
        self.set_distance = 2
        self.Matrix_csv = []
        self.shape_M = []
        self.M_norm = []
        # Omitir la ultima columna del Label, si es que tiene
        self.has_label = 1;

    def read_csv_to_matrix(self):
        self.Matrix_csv = genfromtxt(self.path+self.filename, delimiter=',')
        self.shape_M = np.shape(self.Matrix_csv)
        if self.has_label:
            self.Matrix_csv = self.Matrix_csv[:,:self.shape_M[1]-1]
            self.shape_M = np.shape(self.Matrix_csv)

    # Example to write File
    def write_file(self,file_name):
        file = open(file_name, "a")
        file.write("Hello World"  + str(1) + " holass\n")
        file.close()

    # Normalizamos la Matriz
    def matrix_normalized(self):
        mindata = self.Matrix_csv.min()
        maxdata = self.Matrix_csv.max()
        self.M_norm = ((self.Matrix_csv - mindata) / ((maxdata) - mindata))


    # Guardamos el archovo STC
    def save_matrix_stc(self,matrix,file_stc):
        fileID = open(file_stc, "w")
        fileID.write("set dimension " + str(self.shape_M[1]) + "\n")
        fileID.write("set distance " + str(self.set_distance) + "\n")
        fileID.write("set verbose graphics\n")
        fileID.write("minsert " + str(self.shape_M[0]) + "\n")

        shapeM = np.shape(matrix)
        for i in range(shapeM[0]):
            for j in range(shapeM[1]):
                fileID.write("%.3f " % matrix[i][j])
            fileID.write("\n")

        fileID.write("dex\n")
        fileID.write("close")
        fileID.close()


    def execute(self,file_stc):
        self.read_csv_to_matrix()

        self.matrix_normalized()
        self.save_matrix_stc(self.M_norm,file_stc)
