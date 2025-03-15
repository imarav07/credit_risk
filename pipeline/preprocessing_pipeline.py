# importing pre-requisite libraries
import os
import sys
import pandas as pd

# Get the absolute path of the credit_risk package
project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(project_root)
print(project_root)

#importing the modules from the package
from utils.utils import *
from utils.preprocessing.preprocess import *

class Preprocessor:
    def __init__(self):
        self.config_ = load_config()
        self.data_path_list = return_config_params('data')
        self.credit_data = pd.read_csv(os.path.join(self.data_path_list['path'], self.data_path_list['credit_data']))
        self.missing_values = self.config_.get('preprocessing').get('missing_values')
        self.scaling_cols = self.config_.get('preprocessing').get('scaling')


    def preprocess_data(self):
        self.preprocess_df_1 = missing_values_treatment(self.credit_data, self.missing_values)
        self.preprocess_df_2 = standardize_columns(self.preprocess_df_1, self.scaling_cols)
        return self.preprocess_df_2