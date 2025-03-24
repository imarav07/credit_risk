import yaml
from typing import Dict, List, Optional, Tuple, Any
import pandas as pd
import os

config_file_path = "C:/Aravind's File/Projects/credit_risk/config.yaml"

def load_config(path_: str = config_file_path) -> Dict:
    """
    Function that loads config file and returns config_file as required.
    
    :path_: Path where the config file is stored.
    :return: A dictionary containing the config file.
    """

    with open(path_, 'r') as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
    return config

def return_config_params(primary_key: str) -> Any:
    """
    Function that reads config file, a string, a list, and a boolean and parse yaml file and returns data as required.
    If we require only 1 element from the yaml then only string is returned
    else if we require multiple elements then multiple elements are returned as string
    
    :primary_key: A key which needs to be read
    :param needed_elements: A list of elements to be fetched from the config.
    :param multiple: A boolean flag indicating if multiple elements are needed.
    :return: A single element or a list of elements from the config.
    """
    config = load_config(config_file_path)
    return config[primary_key]

def read_data(path: str, file_name: str, data_type: str) -> pd.DataFrame:
    """
    Function that reads the data from the specified path.
    :path: Path where the data is stored.
    :file_name: Name of the file.
    :data_type: Type of the data.
    """
    if data_type == 'csv':
        data_ = pd.read_csv(os.path.join(path,file_name))
        return data_
    elif data_type == 'excel':
        data_ = pd.read_excel(os.path.join(path,file_name))
        return data_
    elif data_type == 'parquet':
        data_ = pd.read_parquet(os.path.join(path,file_name))
        return data_
    else:
        print("Invalid data type")    

def write_data(data_, path: str, file_name: str, data_type: str) -> pd.DataFrame:
    """
    Function that writes the data to the specified path.

    :data_: Data to be written.
    :path: Path where the data is to be written.
    :file_name: Name of the file.
    :data_type: Type of the data.
    """
    if data_type == 'csv':
        data_.to_csv(os.path.join(path,file_name), index=False)
    elif data_type == 'excel':
        data_.to_excel(os.path.join(path,file_name), index=False)
    elif data_type == 'parquet':
        data_.to_parquet(os.path.join(path,file_name), index=False)
    else:
        print("Invalid data type")    