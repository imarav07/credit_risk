import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple, Any, Union
from sklearn.preprocessing import StandardScaler

def missing_values_treatment(df: pd.DataFrame, config: Dict) -> pd.DataFrame:
    """
    This function is used to treat the missing values in the dataset
    """
    columns = config.keys()
    print(columns)
    for _ in columns:
        replace_value = config.get(_)
        df[_] = df[_].fillna(replace_value)
    return df

def standardize_columns(df: pd.DataFrame, columns: Union[List[str], str]) -> pd.DataFrame:
    """
    This function applies StandardScaler to the specified columns in the dataset
    """
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df