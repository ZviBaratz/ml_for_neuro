"""
Provides utility functions for creating plots in exercise 8.
"""
from typing import Union


def organize_kwargs(
    user_kwargs: Union[dict, None], default_kwargs: dict = None
) -> dict:
    """
    Update default keyword argument configuration with user provided
    configuration.

    Parameters
    ----------
    user_kwargs: Union[dict, None]
        Dictionary of user provided keyword argument configurations, or
        None
    default_kwargs: dict
        Default keyword argument configuration to be updated with user
        configuration

    Returns
    -------
    dict
        Complete keyword argument configuration
    """
    kwargs = user_kwargs or {}
    default_kwargs = default_kwargs or {}
    return {**default_kwargs, **kwargs}
