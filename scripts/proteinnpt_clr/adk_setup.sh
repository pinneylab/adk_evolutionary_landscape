# This config file contains the paths to all relevant data objects used by the ProteinNPT codebase. Only the next two lines should be updated based on your particular setup
source adk_config.sh

# Folders containing pretrained model checkpoints
mkdir -p $adk_data_path/pnpt/ESM
mkdir -p $adk_data_path/pnpt/ESM/MSA_Transformer
mkdir -p $adk_data_path/pnpt/ESM/ESM2
mkdir -p $adk_data_path/pnpt/Tranception
curl -o $adk_data_path/pnpt/Tranception/Tranception_Large_checkpoint.zip https://marks.hms.harvard.edu/tranception/Tranception_Large_checkpoint.zip
unzip $adk_data_path/pnpt/Tranception/Tranception_Large_checkpoint.zip -d $adk_data_path/pnpt/Tranception && rm -f $adk_data_path/pnpt/Tranception/Tranception_Large_checkpoint.zip
curl -o $MSA_Transformer_location https://dl.fbaipublicfiles.com/fair-esm/models/esm_msa1_t12_100M_UR50S.pt
curl -o $ESM2_650M_location https://dl.fbaipublicfiles.com/fair-esm/models/esm2_t33_650M_UR50D.pt

# Folder containing sequence embeddings for the different models
mkdir -p $adk_data_path/pnpt/embeddings

# Folder containing zero-shot fitness predictions
mkdir -p $adk_data_path/pnpt/zero_shot_fitness_predictions