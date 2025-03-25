import pandas as pd
import numpy as np

from typing import Dict, List, Optional, Tuple, Any, Union

def custom_one_hot_encoding(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    This function applies one-hot encoding to the specified columns in the dataset.
    
    :param df: Input DataFrame.
    :param columns: List of columns to apply one-hot encoding.
    :return: DataFrame with one-hot encoded columns.
    """
    df = pd.get_dummies(df, columns=columns, drop_first=True)
    return df