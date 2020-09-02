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
)


def remove_x_ray_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Removes radiology information columns from the dataset.

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
        if column_name.startswith("cxr_")
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

    urls = [CSV_URL_PATTERN.format(week_id=week_id) for week_id in WEEK_IDS]
    dataframes = [
        pd.read_csv(url, parse_dates=True, error_bad_lines=False)
        for url in urls
    ]
    data = pd.concat(dataframes, ignore_index=True)
    data.replace(REPLACE_DICT, inplace=True)
    data = remove_x_ray_columns(data)
    data.dropna(axis=0, subset=[TARGET_COLUMN_NAME], inplace=True)
    return data
