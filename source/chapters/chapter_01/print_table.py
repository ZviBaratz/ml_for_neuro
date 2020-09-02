"""
print_table.py

Defines a set of styling parameters and functions for the dataset's
table display.
"""

import math
import pandas as pd

from configuration import TARGET_COLUMN_NAME
from typing import Any


def highlight_nan(value: Any) -> str:
    """
    Highlight NaN values in grey.

    Parameters
    ----------
    value : Any
        Cell value

    Returns
    -------
    str
        Cell background color definition
    """

    try:
        value = float(value)
    except ValueError:
        color = "white"
    else:
        color = "grey" if math.isnan(value) else "white"
    finally:
        return f"background-color: {color}"


def highlight_positives(test_result: bool) -> str:
    """
    Highlight positive values in red.

    Parameters
    ----------
    test_result : bool
        Observed test result

    Returns
    -------
    str
        Cell background color definition
    """

    color = "red" if test_result else "white"
    return f"background-color: {color}"


def get_table_styles(
    header_font_size: int = 12, cell_font_size: int = 11
) -> list:
    """
    Creates a table styles definition to be used by the
    `set_table_styles()` method.

    References
    ----------
    * Pandas' table styles documentation:
      https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html#Table-styles

    Parameters
    ----------
    header_font_size : int
        Header text font size in pixels (px)
    cell_font_size : int
        Cell text font size in pixels (px)

    Returns
    -------
    list
        Table styles definition
    """

    heading_properties = [("font-size", f"{header_font_size}px")]
    cell_properties = [("font-size", f"{cell_font_size}px")]
    return [
        dict(selector="th", props=heading_properties),
        dict(selector="td", props=cell_properties),
    ]


def print_table(
    data: pd.DataFrame,
    header_font_size: int = 12,
    cell_font_size: int = 11,
    text_align: str = "center",
) -> pd.DataFrame.style:
    """
    Returns a styled representation of the dataframe.

    Parameters
    ----------
    data : pd.DataFrame
        Input data
    header_font_size : int
        Header text font size in pixels (px)
    cell_font_size : int
        Cell text font size in pixels (px)
    text_align : str
        Any of the CSS text-align property options, defaults to "center"

    Returns
    -------
    pd.DataFrame.style
        Styled dataframe representation
    """

    table_styles = get_table_styles(
        header_font_size=header_font_size, cell_font_size=cell_font_size
    )
    return (
        data.style.set_table_styles(table_styles)
        .applymap(highlight_nan)
        .applymap(highlight_positives, subset=[TARGET_COLUMN_NAME])
        .set_properties(**{"text-align": text_align})
    )
