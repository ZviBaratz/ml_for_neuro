"""
get_scattered_chunks.py

Definition of the `get_scattered_chunks()` function, used to generate
a subsample of rows for manual review of the dataset.
"""

import numpy as np
import pandas as pd


def get_scattered_chunks(
    data: pd.DataFrame, n_chunks: int = 5, chunk_size: int = 3
) -> pd.DataFrame:
    """
    Returns a subsample of equally scattered chunks of rows.

    Parameters
    ----------
    data : pd.DataFrame
        Input dataset
    n_chunks : int
        Number of chunks to collect for the subsample
    chunk_size : int
        Number of rows to include in each chunk

    Returns
    -------
    pd.DataFrame
        Subsample data
    """

    endpoint = len(data) - chunk_size
    sample_indices = np.linspace(0, endpoint, n_chunks, dtype=int)
    sample_indices = [
        index for i in sample_indices for index in range(i, i + chunk_size)
    ]
    return data.iloc[sample_indices, :]
