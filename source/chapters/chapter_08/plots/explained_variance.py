"""
Functions creating plots to evaluate explained variance.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from plots.utils import organize_kwargs
from sklearn.decomposition import PCA


DEFAULT_FIG_KWARGS = {"figsize": (9, 6)}
DEFAULT_COMPONENT_AX_KWARGS = {
    "color": "purple",
    "linewidth": 2,
    "label": "Individual Component",
}
DEFAULT_CUMULATIVE_AX_KWARGS = {
    "color": "orange",
    "linewidth": 2,
    "label": "Cumulative",
}
DEFAULT_CUSTOMIZATIONS = {
    "title": "Explained Variance Ratio by Number of Principal Components",
    "xlabel": "Number of Principal Components",
    "ylabel": "Explained Variance Ratio",
}
DEFAULT_LEGEND_LOCATION = (0.85, 0.7)


def plot_explained_variance_ratio(
    pca: PCA,
    fig_kwargs: dict = None,
    component_ax_kwargs: dict = None,
    cumulative_ax_kwargs: dict = None,
    customizations: dict = None,
    legend_location: tuple = DEFAULT_LEGEND_LOCATION,
) -> tuple:
    """
    Plot explained variance by component number for a fitted PCA estimator.

    Parameters
    ----------
    pca : PCA
        Fitted PCA model
    fig_kwargs : dict
        Keyword arguments passed to the created figure
    component_ax_kwargs : dict
        Keyword arguments passed in the explained variance by individual
        component plot call
    cumulative_ax_kwargs : dict
        Keyword arguments passed in the cumulative explained variance by
        component plot call
    customizations : dict
        Keyword arguments passed to the axis' `set()` method
    legend_location: Tuple(float, float)
        Legend location within figure

    Returns
    -------
    Tuple(Figure, Axes)
        Create figure and axes
    """
    # Prepare figure and axes kwargs
    fig_kwargs = organize_kwargs(fig_kwargs, DEFAULT_FIG_KWARGS)
    component_ax_kwargs = organize_kwargs(
        component_ax_kwargs, DEFAULT_COMPONENT_AX_KWARGS
    )
    cumulative_ax_kwargs = organize_kwargs(
        cumulative_ax_kwargs, DEFAULT_CUMULATIVE_AX_KWARGS
    )
    customizations = organize_kwargs(customizations, DEFAULT_CUSTOMIZATIONS)

    # Create figure
    fig, ax = plt.subplots(**fig_kwargs)

    # Plot explained variance ratio by component
    x_range = range(1, pca.n_components_ + 1)
    ax.plot(x_range, pca.explained_variance_ratio_, **component_ax_kwargs)

    # Plot cumulative explained variance
    cumulative_sum = np.cumsum(pca.explained_variance_ratio_)
    ax.plot(x_range, cumulative_sum, **cumulative_ax_kwargs)

    #
    # Customizations
    #
    ax.set(**customizations)

    # Add legend
    fig.legend(bbox_to_anchor=legend_location)

    # Fix x-axis tick labels to show integers
    ax.set_xticks(x_range)
    ax.set_xticklabels(x_range)

    return fig, ax


def create_explained_variance_df(pca: PCA) -> pd.DataFrame:
    """
    Create a formatted dataframe to display the plot's information
    conveniently.

    Parameters
    ----------
    pca : PCA
        Fitted PCA model

    Returns
    -------
    pd.DataFrame
        Explained variance (per component and cumulative)
    """
    results_dict = {
        "Individual Component": pca.explained_variance_ratio_,
        "Cumulative": np.cumsum(pca.explained_variance_ratio_),
    }
    index = range(1, pca.n_components_ + 1)
    df = pd.DataFrame(results_dict, index=index)
    df.index.name = "# Components"
    return df
