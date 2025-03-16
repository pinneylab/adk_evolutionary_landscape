# This config file contains the paths to all relevant data objects used by the ProteinNPT codebase. Only the next two lines should be updated based on your particular setup
source adk_config.sh

# Environment setup - Conda
conda env create -f $adk_repo_path/adk_pnpt_env.yml

# Folders containing pretrained model checkpoints
mkdir -p $adk_data_path/ESM
mkdir -p $adk_data_path/ESM/MSA_Transformer
mkdir -p $adk_data_path/ESM/ESM2
mkdir -p $adk_data_path/Tranception
curl -o $adk_data_path/Tranception/Tranception_Large_checkpoint.zip https://marks.hms.harvard.edu/tranception/Tranception_Large_checkpoint.zip
unzip $adk_data_path/Tranception/Tranception_Large_checkpoint.zip -d $adk_data_path/Tranception && rm -f $adk_data_path/Tranception/Tranception_Large_checkpoint.zip
curl -o $MSA_Transformer_location https://dl.fbaipublicfiles.com/fair-esm/models/esm_msa1_t12_100M_UR50S.pt
curl -o $ESM2_650M_location https://dl.fbaipublicfiles.com/fair-esm/models/esm2_t33_650M_UR50D.pt

# Folder where ADK experimental data is stored (provided in data dependencies)
mkdir -p $adk_experimental_data_folder

# Folders containing multiple sequence alignments (MSAs) and MSA weights (provided in data dependencies)
mkdir -p $adk_data_path/MSA_files
mkdir -p $adk_data_path/MSA_weights

# Folders containing hhfilter and clustal omega utils (provided in data dependencies)
mkdir -p $adk_data_path/utils

# Folder containing sequence embeddings for the different models
mkdir -p $adk_data_path/embeddings

# Folder containing zero-shot fitness predictions
mkdir -p $adk_data_path/zero_shot_fitness_predictions