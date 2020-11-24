import numpy as np
import pandas as pd


def append_intercept(X: pd.DataFrame) -> pd.DataFrame:
    """
    Append a column of ones to the beginning of the dataset.

    Parameters
    ----------
    X : pd.DataFrame
        Observed features data

    Returns
    -------
    pd.DataFrame
        Design matrix
    """
    intercept = np.ones((len(X), 1))
    return np.hstack([intercept, X])


def estimate_coefficients(X: pd.DataFrame, y: np.ndarray) -> np.ndarray:
    """
    Returns the estimated beta hat vector.

    Parameters
    ----------
    X : pd.DataFrame
        Observed features data
    y : np.ndarray
        Target vector

    Returns
    -------
    np.ndarray
        Estimated coefficients
    """
    X = append_intercept(X)
    return np.linalg.inv(X.T @ X) @ (X.T @ y)


def calculate_predictions(X: pd.DataFrame, beta_hat: np.ndarray) -> np.ndarray:
    """
    Returns the predicted values for a test set of observations (X) using a
    vector of the estimated coefficients.

    Parameters
    ----------
    X : pd.DataFrame
        Test features data
    beta_hat : np.ndarray
        Estimated coefficients vector

    Returns
    -------
    np.ndarray
        Estimated coefficients
    """
    X = append_intercept(X)
    return X @ beta_hat


class ManualLinearRegression:
    """
    Manual implementation of an Ordinary Least Squares (OLS) linear regression
    model.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the ManualLinearRegression model.
        """
        self.beta_hat = None

    def append_intercept(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Append a column of ones to the beginning of the dataset.

        Parameters
        ----------
        X : pd.DataFrame
            Observed features data

        Returns
        -------
        pd.DataFrame
            Design matrix
        """
        intercept = np.ones((len(X), 1))
        return np.hstack([intercept, X])

    def estimate_coefficients(
        self, X: pd.DataFrame, y: np.ndarray
    ) -> np.ndarray:
        """
        Returns the estimated beta hat vector.

        Parameters
        ----------
        X : pd.DataFrame
            Observed features data
        y : np.ndarray
            Target vector

        Returns
        -------
        np.ndarray
            Estimated coefficients
        """
        X = self.append_intercept(X)
        return np.linalg.inv(X.T @ X) @ (X.T @ y)

    def fit(self, X: pd.DataFrame, y: np.ndarray) -> None:
        """
        Calculate the estimated coefficients vector (beta hat).

        Parameters
        ----------
        X : pd.DataFrame
            Observed features data
        y : np.ndarray
            Target vector
        """
        self.beta_hat = self.estimate_coefficients(X, y)

    def predict(self, X: pd.DataFrame):
        """
        Returns the predicted values for a test set of observations (X) using a
        vector of the estimated coefficients.

        Parameters
        ----------
        X : pd.DataFrame
            Test features data
        beta_hat : np.ndarray
            Estimated coefficients vector

        Returns
        -------
        np.ndarray
            Estimated coefficients
        """
        if self.beta_hat is not None:
            X = self.append_intercept(X)
            return X @ self.beta_hat
        raise RuntimeError("Please fit the model before calling predict().")
