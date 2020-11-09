"""
calculate_nan_fractions.py

Definition of the `calculate_nan_fractions()` function.
"""

import pandas as pd

from configuration import NAN_FRACTION_THRESHOLD, TARGET_COLUMN_NAME


def calculate_nan_fractions(
    data: pd.DataFrame, target_column: str = TARGET_COLUMN_NAME
) -> pd.DataFrame:
    """
    Calculates the fraction of missing values within each column
    in the dataset.

    Parameters
    ----------
    data : pd.DataFrame
        Input dataset
    target_column : str, optional
        Boolean target column name, by default TARGET_COLUMN_NAME

    Returns
    -------
    pd.DataFrame
        Missing value fractions
    """

    # Extract columns with null values.
    nan_columns = data.columns[data.isnull().any()]
    nan_data = data[nan_columns]

    # Calculate fractions of null values.
    nan_counts = nan_data.isnull().sum()
    fraction_missing = nan_counts / len(nan_data)
    positives_nan_counts = nan_data[data[target_column]].isnull().sum()
    negatives_nan_counts = nan_data[~data[target_column]].isnull().sum()
    fraction_missing_positives = positives_nan_counts / nan_counts
    fraction_missing_negatives = negatives_nan_counts / nan_counts

    # Create dataframe.
    fraction_missing_df = pd.DataFrame(
        {
            "Total Missing": fraction_missing,
            "Negatives Fraction": fraction_missing_negatives,
            "Positives Fraction": fraction_missing_positives,
        }
    )
    fraction_missing_df.index.name = "Column Name"
    return fraction_missing_df.sort_values("Total Missing", ascending=False)


def remove_missing_data_columns(
    data: pd.DataFrame,
    threshold: float = NAN_FRACTION_THRESHOLD,
    target_column: str = TARGET_COLUMN_NAME,
) -> pd.DataFrame:
    """
    Removes columns where the fraction of missing values is greater than
    *threshold*.

    Parameters
    ----------
    data : pd.DataFrame
        Input data
    threshold : float, optional
        Fraction of missing values to use as threshold, by default
        NAN_FRACTION_THRESHOLD
    target_column : str, optional
        Boolean target column name, by default TARGET_COLUMN_NAME

    Returns
    -------
    pd.DataFrame
        Dataframe without missing data columns
    """

    missing_fractions = calculate_nan_fractions(
        data, target_column=target_column
    )
    flagged = missing_fractions[
        missing_fractions["Total Missing"] > threshold
    ].index
    return data.drop(flagged, axis=1)


def clean_missing_values(
    data: pd.DataFrame,
    threshold: float = NAN_FRACTION_THRESHOLD,
    target_column: str = TARGET_COLUMN_NAME,
) -> pd.DataFrame:
    """
    Cleans missing values from the dataset.

    Parameters
    ----------
    data : pd.DataFrame
        Input dataset
    threshold : float, optional
        Fraction of missing values to use as threshold for feature removal,
        by default NAN_FRACTION_THRESHOLD
    target_column : str, optional
        Boolean target column name, by default TARGET_COLUMN_NAME

    Returns
    -------
    pd.DataFrame
        NaN-free dataset
    """

    data = remove_missing_data_columns(
        data, threshold=threshold, target_column=target_column
    )
    return data.dropna(axis=0, how="any").reset_index(drop=True)