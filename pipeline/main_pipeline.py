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
from pipeline.preprocessing_pipeline import Preprocessor
from pipeline.feature_pipeline import FeaturePipeline   

class MainPipeline():
    def __init__(self):
        self.common_functions = CommonFunctions()
        self.preprocessor = Preprocessor()
        self.feature_processor = FeaturePipeline()
        self.config_ = self.common_functions.config_
        self.data_path_list = self.common_functions.data_path_list

    def run_pipeline(self):
        #preprocessing
        preprocessed_data = self.preprocessor.preprocess_data()
        self.common_functions.write_data(preprocessed_data, self.data_path_list['path'], self.data_path_list['preprocessed_data'], 'parquet')
        #feature engineering
        feature_engineered_data = self.feature_processor.feature_engineering()
        self.common_functions.write_data(feature_engineered_data, self.data_path_list['path'], self.data_path_list['feature_engineered_data'], 'parquet')

        return feature_engineered_data



