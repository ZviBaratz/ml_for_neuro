"""
read_data.py

Definition of the `read_data()` function, used to retrieve the raw
dataset from it's remote location, as defined in *configuration.py*.
"""

import pandas as pd

from configuration import (
    CSV_URL_PATTERN,
    REPLACE_DICT,
    TARGET_COLUMN_NAME,
    WEEK_IDS,
    X_RAY_COLUMN_PREFIX,
)


def remove_x_ray_columns(
    data: pd.DataFrame, prefix: str = X_RAY_COLUMN_PREFIX
) -> pd.DataFrame:
    """
    Removes radiology results columns from the dataset.

    Parameters
    ----------
    data : pd.DataFrame
        Input dataset

    Returns
    -------
    pd.DataFrame
        Dataset without X-ray data
    """

    xray_columns = [
        column_name
        for column_name in data.columns
        if column_name.startswith(prefix)
    ]
    return data.drop(xray_columns, axis=1)


def read_data() -> pd.DataFrame:
    """
    Returns the public COVID-19 PCR test dataset from the *covidclinicaldata*
    repository.

    Returns
    -------
    pd.DataFrame
        COVID-19 PCR test dataset
    """

    # Read CSVs from remote location as a single dataframe.
    urls = [CSV_URL_PATTERN.format(week_id=week_id) for week_id in WEEK_IDS]
    dataframes = [pd.read_csv(url, error_bad_lines=False) for url in urls]
    data = pd.concat(dataframes, ignore_index=True)

    # Convert COVID-19 test results to boolean values.
    data.replace(REPLACE_DICT, inplace=True)

    # Remove x-ray data.
    data = remove_x_ray_columns(data)

    # Remove the batch date column.
    data.drop("batch_date", axis=1, inplace=True)

    # Remove rows with no test results.
    data.dropna(axis="rows", subset=[TARGET_COLUMN_NAME], inplace=True)
    return data
