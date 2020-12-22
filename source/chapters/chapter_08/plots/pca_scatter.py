import matplotlib.pyplot as plt
import numpy as np

from ipywidgets import interact


DEFAULT_TITLE = "Dataset Projected Over {n_dimensions} Dimensions Using PCA"
PCA_AXIS_LABELS_2D = {
    "xlabel": "Principal Component #1",
    "ylabel": "Principal Component #2",
}
PCA_AXIS_LABELS_3D = {
    "xlabel": "Principal Component #1",
    "ylabel": "Principal Component #2",
    "zlabel": "Principal Component #3",
}


def plot_reduced(
    X_reduced: np.ndarray,
    classification_labels: np.ndarray = None,
    true_labels: np.ndarray = None,
    title: str = None,
) -> None:
    """
    Plots a 3D or 2D scatter plot of *X_reduced*, potentially colored by
    *classification_labels* and marked by equality with *true_labels* (if
    provided).

    Parameters
    ----------
    X_reduced : np.ndarray
        Dimensionality-reduced dataset
    classification_labels : np.ndarray, optional
        Classification results to use for color mapping, by default None
    true_labels : np.ndarray, optional
        Real labels to use for marker styling, by default None
    title : str, optional
        Custom title, by default None
    """
    # Generate a default title if required
    n_dimensions = X_reduced.shape[1]
    title = title or DEFAULT_TITLE.format(n_dimensions=n_dimensions)

    # Create a classification_success mask array if required
    classification_success = None
    if true_labels is not None and classification_labels is not None:
        classification_success = true_labels == classification_labels

    # Create color mapping arrays
    color = "blue" if classification_labels is None else classification_labels
    if classification_success is not None:
        c_1 = (
            color if isinstance(color, str) else color[classification_success]
        )
        c_2 = (
            color if isinstance(color, str) else color[~classification_success]
        )

    # Generate plot by number of dimensions
    if n_dimensions == 3:
        # Create 3D scatter plot
        def plot_3d_scatter(elev=10, azim=-90):
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, projection="3d")
            if classification_success is None:
                ax.scatter(*X_reduced.T, c=color)
            else:
                # Plot correct labels
                ax.scatter(*X_reduced[classification_success].T, c=c_1, s=60)
                # Plot incorrect labels
                ax.scatter(
                    *X_reduced[~classification_success].T,
                    c=c_2,
                    s=60,
                    marker="x",
                )
            ax.set(**PCA_AXIS_LABELS_3D)
            ax.set_title(title)
            ax.view_init(elev, azim)

        interact(plot_3d_scatter)

    elif n_dimensions == 2:
        # Create 2D scatter plot
        fig, ax = plt.subplots(figsize=(6, 4))
        if classification_success is None:
            ax.scatter(*X_reduced.T)
        else:
            success = X_reduced[classification_success]
            failure = X_reduced[~classification_success]
            # Plot correct labels
            ax.scatter(
                *success.T,
                c=c_1,
                label="Corrent Label",
            )
            # Plot incorrect labels
            ax.scatter(
                *failure.T,
                c=c_2,
                marker="x",
                label="Incorrent Label",
            )
            ax.legend(loc="upper center")
        ax.set(
            title=title,
            **PCA_AXIS_LABELS_2D,
        )
