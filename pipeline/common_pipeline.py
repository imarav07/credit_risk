# importing pre-requisite libraries
import os
import sys
import pandas as pd

# Get the absolute path of the credit_risk package
project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(project_root)
print(project_root)

#importing the modules from the package
from utils.utils import load_config, return_config_params, read_data, write_data

class CommonFunctions:
    def __init__(self):
        self.config_ = load_config()
        self.data_path_list = return_config_params('data')
        self.preprocessing_params = return_config_params('preprocessing')
        self.feature_engineering_params = return_config_params('feature_engineering')

    def read_data(self, data_path, file_name, data_type):
        return read_data(data_path, file_name, data_type)

    def write_data(self, data_, data_path, file_name, data_type):
        write_data(data_, data_path, file_name, data_type)