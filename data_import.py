class DataImporter():

    def __init__(self, data_file, ftype = "csv", sep = " ", dtype = None, ncols = 1):
        self.data_file = data_file
        self.ftype = ftype ##TODO: infer that from the file name!
        self.sep = sep
        self.dtype = dtype
        self.ncols = ncols

    def read(self):
        ## First we import everything blindly into a list, line by line, and also stripping the "\n" at the end
        ## And we try to separate data into columns, if there are more than one.
        file_path = "data/" + self.data_file
        data = []
        with open(file_path) as file:
            line = True
            while line:
                line = file.readline()
                sline = line.rstrip()
            ## Split columns if user indicates more than 1
                if self.ncols > 1: sline = sline.split(self.sep)
                data.append(sline)
        file.close()
        return (data)

    # def clean(self):
    #     new_lines = []
    #         lines = [int(line.rstrip()) for line in lines]
