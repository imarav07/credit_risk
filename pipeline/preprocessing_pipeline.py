# importing pre-requisite libraries
import os
import sys
import pandas as pd

# Get the absolute path of the credit_risk package
project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(project_root)
print(project_root)

#importing the modules from the package
from pipeline.common_pipeline import CommonFunctions
from utils.preprocessing.preprocess import missing_values_treatment, standardize_columns

class Preprocessor():
    def __init__(self):
        common_functions = CommonFunctions()
        self.config_ = common_functions.config_
        self.data_path_list = common_functions.data_path_list
        self.preprocessing_params = common_functions.preprocessing_params
        self.credit_data = common_functions.read_data(self.data_path_list['path'], self.data_path_list['credit_data'], 'csv')
        self.missing_values = self.preprocessing_params.get('missing_values')
        self.scaling_cols = self.preprocessing_params.get('scaling')


    def preprocess_data(self):
        self.preprocess_df_1 = missing_values_treatment(self.credit_data, self.missing_values)
        self.preprocess_df_2 = standardize_columns(self.preprocess_df_1, self.scaling_cols)
        return self.preprocess_df_2