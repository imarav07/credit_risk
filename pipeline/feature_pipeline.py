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
from utils.feature_engineering.features import custom_one_hot_encoding

class FeaturePipeline():
    def __init__(self):
        common_functions = CommonFunctions()
        self.config_ = common_functions.config_
        self.data_path_list = common_functions.data_path_list
        self.feature_engineering_params = common_functions.feature_engineering_params
        self.one_hot_encoding = self.feature_engineering_params.get('one_hot_encoding')
        self.preprocessed_data = common_functions.read_data(self.data_path_list['path'], self.data_path_list['preprocessed_data'], 'parquet')

    def feature_engineering(self):
        print(self.one_hot_encoding)
        self.feature_df_1 = custom_one_hot_encoding(self.preprocessed_data, self.one_hot_encoding)
        return self.feature_df_1