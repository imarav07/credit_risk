import yaml
from typing import Dict, List, Optional, Tuple, Any

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

def return_config_params(primary_key: str, needed_elements: List[str], multiple: bool = False) -> Any:
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
    if multiple:
        return [config[primary_key][element] for element in needed_elements]
    else:
        return config[primary_key]