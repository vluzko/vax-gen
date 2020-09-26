# vax-gen

vax-gen is a tool for designing vaccines given the sequence of a pathogen and HLA-typing for a population. It is *not* intended for any kind of serious use, and *certainly* not for use without expert oversight. The prediction tools it depends on are simply not good enough.

The pipeline is inspired by (but does not directly use) pipelines for personalized cancer vaccine design.

## Setup

### Getting test data
* Download the test BAM files from https://ftp.ncbi.nlm.nih.gov/toolbox/gbench/tutorial/Tutorial6/BAM_Test_Files.zip
* Unzip the file into tests/data


## Input features
* Peptide sequence
* HLA-typing
* RNA counts
* DNA counts
* Chopping probability
* MHC binding prediction
    * Mass-spec based probability
    * IC50
* T-cell binding prediction

## Peptide selection
* Length and number of sequences
* Is there immuno-dominance?
* Select for multiple different MHC targets


## Papers
* http://tools.iedb.org/main/tcell/
* [https://www.frontiersin.org/articles/10.3389/fimmu.2019.00298/full](Antibody Specific B-Cell Epitope Predictions: Leveraging Information From Antibody-Antigen Protein Complexes)