# Evolutionary-scale enzymology enables exploration of a multi-peaked catalytic landscape
___

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/)
[![DOI:10.1101/2024.10.23.619915v1](http://img.shields.io/badge/DOI-10.1101/2024.10.23.619915v1-B31B1B.svg)](https://doi.org/10.1101/2024.10.23.619915) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is the in-progress code repository for the preprint ["Evolutionary-Scale Enzymology Enables Biochemical Constant Prediction Across a Multi-Peaked Catalytic Landscape"](https://www.biorxiv.org/content/10.1101/2024.10.23.619915v1).

### Overview
___

**As of 2024-12-16**:


This repository is in progress, and currently contains statistics, plotting, and analysis code from the assoiciated figures as jupyter notebooks.

The ProteinNPT model architecture is described in the associated [paper](https://papers.nips.cc/paper_files/paper/2023/hash/6a4d5d85f7a52f062d23d98d544a5578-Abstract-Conference.html) and code is available on [GitHub](https://github.com/OATML-Markslab/ProteinNPT).

### Contents
___
  - figures:
    - **fig1-6**: plotting and statistics
    - **fig7**: dimensionality reduction, and manifold metrics (clustering/trustworthiness)
    - **fig8**: plotting
  - notebooks:
    - **bootstrap_supervised_ml**: dataset bootstrapping, ablation, and lightweight supervised ML model training

### License
___
This code is released under the MIT License. See LICENSE file for details.

### Citation
___
```
@ARTICLE
author={Muir, Duncan F. and Asper, Garrison P. R. and Notin, Pascal and Posner, Jacob A. and Marks, Debora S. and Keiser, Michael J. and Pinney, Margaux M.},
title={Evolutionary-Scale Enzymology Enables Biochemical Constant Prediction Across a Multi-Peaked Catalytic Landscape}, 
year={2024},
DOI={10.1101/2024.10.23.619915v1}
```