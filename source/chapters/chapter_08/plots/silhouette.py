"""
Functions to plot silhouette scores by either number of principal components
used to reduce the dataset's dimensionality or number of clusters used by
`KMeans`.
"""

import matplotlib.pyplot as plt
import numpy as np

from plots.utils import organize_kwargs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from typing import Iterable, Tuple


#
# Silhouette scores by number of principal components
#

DEFAULT_FIGURE_KWARGS = {"figsize": (10, 5)}
DEFAULT_AXES_KWARGS = {"marker": "o"}
DEFAULT_CUSTOMIZATIONS = {
    "title": "Silhouette Score by Number of Principal Components",
    "xlabel": "Number of Principal Components",
    "ylabel": "Silhouette Score",
}


def plot_silhouette_scores_by_pc(
    X_reduced: np.ndarray,
    classification_labels: Iterable[np.ndarray],
    fig_kwargs: dict = None,
    ax_kwargs: dict = None,
    customizations: dict = None,
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plots silhouette score by number of included principal components.

    Parameters
    ----------
    X_reduced : np.ndarray
        Dimensionality-reduced dataset
    classification_labels : Iterable[np.ndarray]
        Classification results by number of principal components
    fig_kwargs : dict, optional
        Keyword arguments passed to the created figure, by default None
    ax_kwargs : dict, optional
        Keyword arguments passed to the created axis, by default None
    customizations : dict, optional
        Keyword arguments passed to the axis' set() method, by default None,
        by default None

    Returns
    -------
    Tuple[plt.Figure, plt.Axes]
        Created figure and axis
    """
    fig_kwargs = organize_kwargs(fig_kwargs, DEFAULT_FIGURE_KWARGS)
    ax_kwargs = organize_kwargs(ax_kwargs, DEFAULT_AXES_KWARGS)
    customizations = organize_kwargs(customizations, DEFAULT_CUSTOMIZATIONS)
    scores = []
    x_range = range(1, len(classification_labels) + 1)
    for i in x_range:
        X_subset = X_reduced[:, :i]
        labels = classification_labels[i - 1]
        score = silhouette_score(X_subset, labels)
        scores.append(score)
    fig, ax = plt.subplots(**fig_kwargs)
    ax.plot(x_range, scores, **ax_kwargs)
    ax.set(xticks=x_range, xticklabels=x_range)
    ax.set(**customizations)
    return fig, ax


#
# Silhouette scores by number of K-means clusters
#

DEFAULT_K_FIGURE_KWARGS = {"figsize": (8, 5)}
DEFAULT_K_CUSTOMIZATION_KWARGS = {
    "title": "Silhouette Score by $k$",
    "xlabel": "$k$",
    "ylabel": "Silhouette Score",
}


def plot_silhouette_scores_by_k(
    X: np.ndarray, max_k: int = 10
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plot silhouette scores by k.

    Parameters
    ----------
    X : np.ndarray
        The dataset to fit
    max_k : int, optional
        Maximal number of clusters, by default 10

    Returns
    -------
    Tuple[plt.Figure, plt.Axes]
        Created figure and axis
    """
    models = [KMeans(n_clusters=i).fit(X) for i in range(2, max_k + 1)]
    scores = [silhouette_score(X, model.labels_) for model in models]
    fig, ax = plt.subplots(**DEFAULT_K_FIGURE_KWARGS)
    ax.plot(range(2, max_k + 1), scores, marker="o")
    ax.set(**DEFAULT_K_CUSTOMIZATION_KWARGS)
    return fig, ax
