import matplotlib.pyplot as plt
import numpy as np

from itertools import permutations
from plots.utils import organize_kwargs
from sklearn.metrics import accuracy_score
from typing import Iterable, Tuple

DEFAULT_FIGURE_KWARGS = {"figsize": (10, 5)}
DEFAULT_AXES_KWARGS = {"marker": "o"}
DEFAULT_CUSTOMIZATIONS = {
    "title": "Accuracy by Number of Principal Components",
    "xlabel": "Number of Principal Components",
    "ylabel": "Accuracy Score",
}


def plot_accuracy_by_pc(
    classification_labels: Iterable,
    true_labels: np.ndarray,
    fig_kwargs: dict = None,
    ax_kwargs: dict = None,
    customizations: dict = None,
) -> Tuple[plt.Figure, plt.Axes]:
    """
    Plot accuracy scores by number of principal components.

    Parameters
    ----------
    classification_labels : Iterable
        Classification labels estimated by clustering each subset of principal
        components
    true_labels : np.ndarray
        True classification classes
    fig_kwargs : dict, optional
        Keyword arguments passed to the created figure, by default None
    ax_kwargs : dict, optional
        Keyword arguments passed to the created axis, by default None

    Returns
    -------
    Tuple[plt.Figure, plt.Axes]
        Created figure and axis
    """
    fig_kwargs = organize_kwargs(fig_kwargs, DEFAULT_FIGURE_KWARGS)
    ax_kwargs = organize_kwargs(ax_kwargs, DEFAULT_AXES_KWARGS)
    customizations = organize_kwargs(customizations, DEFAULT_CUSTOMIZATIONS)
    distinct_labels = sorted(set(true_labels))
    scores = []
    for labels_array in classification_labels:
        permuted_scores = []
        for permutation in permutations(distinct_labels):
            permuted_true_labels = true_labels.copy()
            for i in range(len(permutation)):
                permuted_true_labels[true_labels == i] = permutation[i]
            permuted_scores.append(
                accuracy_score(labels_array, permuted_true_labels)
            )
        scores.append(np.max(permuted_scores))
    fig, ax = plt.subplots(**fig_kwargs)
    x_range = range(1, len(scores) + 1)
    ax.plot(x_range, scores, **ax_kwargs)
    ax.set(xticks=x_range, xticklabels=x_range, **customizations)
    return fig, ax
