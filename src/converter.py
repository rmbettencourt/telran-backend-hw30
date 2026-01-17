# ./src/converter.py

from typing import Dict, Iterable
import pandas as pd


Enumerated = Dict[str, int]
Mappered = Dict[str, Enumerated]


def enumerator(values: Iterable[str]) -> Enumerated:
    """
    Enumerate unique values preserving their order.

    Args:
        values: Iterable of string values.

    Returns:
        Mapping from value to its integer index.
    """
    return {value: index for index, value in enumerate(values)}


def columns_mapper(columns: Iterable[str], df: pd.DataFrame) -> Mappered:
    """
    Create value-to-index mappings for selected DataFrame columns.

    Args:
        columns: Column names to enumerate.
        df: Source DataFrame.

    Returns:
        Dictionary mapping column names to enumeration mappings.
    """
    return {
        column: enumerator(df[column].unique())
        for column in columns
    }


def convert_x(df: pd.DataFrame, mapper: Mappered) -> pd.DataFrame:
    """
    Convert DataFrame categorical columns to numeric values using mapper.

    Args:
        df: Source DataFrame.
        mapper: Column-to-enumeration mapping.

    Returns:
        New DataFrame with converted columns.
    """
    converted_df = df.copy()

    for column, column_mapper in mapper.items():
        converted_df[column] = converted_df[column].map(column_mapper)

    return converted_df
