"""Make MHC binding predictions for all peptides"""
import numpy as np
import pandas as pd
from mhcflurry import Class1PresentationPredictor




def score_with_mhcflurry(peptides: np.ndarray, alleles: np.ndarray):
    predictor = Class1PresentationPredictor.load()
    predictor_scores = predictor.predict(
        peptides=peptides,
        alleles=alleles,
        verbose=0)



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