# Evolutionary-scale enzymology enables exploration of a rugged catalytic landscape

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/)
[![DOI:10.1101/2024.10.23.619915v1](http://img.shields.io/badge/DOI-10.1101/2024.10.23.619915v1-B31B1B.svg)](https://doi.org/10.1101/2024.10.23.619915) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is the in-progress code repository for the preprint ["Evolutionary-Scale Enzymology Enables Biochemical Constant Prediction Across a Multi-Peaked Catalytic Landscape"](https://www.biorxiv.org/content/10.1101/2024.10.23.619915v1).

## Installation and Setup

### Install uv

Curl:

    curl -LsSf https://astral.sh/uv/install.sh | sh

Homebrew:

    brew install uv

### Clone the repository

    git clone git@github.com:pinneylab/adk_evolutionary_landscape.git

### Navigate to the repository, create virtual environment

    cd adk_evolutionary_landscape

    uv sync

    uv pip install . --python .venv

### Download and unpack source data

Source data files are hosted in a Zenodo repository: https://zenodo.org/records/15022271

In main repo dir:

    curl -o data.zip https://zenodo.org/records/15022271/files/data.zip

    unzip data.zip

## Usage

### To run python scripts, run uv with the script name

For example, to run the `run_adk_bootstrapped_ml_titration.py` script:

    uv run scripts/run_adk_bootstrapped_ml_titration.py \
      --split_dict data/adk_175_org_bootstrap_stratified_split.json \
      --ohe_df data/one_hot_msa_175_orgs.csv \
      --esm_df data/adk_esm_650M_layer33_embeddings.csv \
      --dataset data/adk_ml_dataset.csv

### To run jupyter notebooks, run jupyter-lab with UV

    uv run --with jupyter jupyter lab

### To run ProteinNPT scripts (Cuda/GPU required)

The ProteinNPT model architecture is described in the associated [paper](https://papers.nips.cc/paper_files/paper/2023/hash/6a4d5d85f7a52f062d23d98d544a5578-Abstract-Conference.html) and code is available on [GitHub](https://github.com/OATML-Markslab/ProteinNPT).

From main repo dir, navigate to ProteinNPT script folder:

    cd scripts/proteinnpt_clr

You will need to edit and configure two variables at the top of the `adk_config.sh` script in scripts/proteinnpt_clr:

```
adk_repo_path
adk_data_path
```
These should be absolute paths to the corresponding repo and data folders.

After configuring these variables, run the following script to setup and download necessary dependencies:

    bash adk_setup.sh

Then you can run scripts `StepX.sh` in numerical order to train and evaulate the deep learning models. However, a results file is provided in
the source data files should you wish to skip this step and visualize the results.

## License
This code is released under the MIT License. See LICENSE file for details.

## Citation
```
@ARTICLE
author={Muir, Duncan F. and Asper, Garrison P. R. and Notin, Pascal and Posner, Jacob A. and Marks, Debora S. and Keiser, Michael J. and Pinney, Margaux M.},
title={Evolutionary-Scale Enzymology Enables Biochemical Constant Prediction Across a Multi-Peaked Catalytic Landscape}, 
year={2024},
DOI={10.1101/2024.10.23.619915v1}
```

