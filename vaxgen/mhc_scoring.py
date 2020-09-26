"""Make MHC binding predictions for all peptides"""
import pandas as pd


def predict(epitopes: pd.DataFrame, hla_types: pd.DataFrame) -> pd.DataFrame:
    """Make MHC binding predictions for all epitopes and all MHCs present.

    Args:
        epitopes:   The full table of epitope sequences
        hla_types:  The full table of population level HLA typing information.

    Returns:
        (pd.DataFrame): A table whose columns are individual MHC molecules, rows are
            individual peptides, and entries are the corresponding binding prediction.
    """

    raise NotImplementedError