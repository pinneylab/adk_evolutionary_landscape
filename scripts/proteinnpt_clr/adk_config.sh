# This config file contains the paths to all relevant data objects used by the ProteinNPT codebase. Only the next two lines should be updated based on your particular setup
export adk_data_path="/srv/home/dmuir/code/adk_evolutionary_landscape/data" 
export adk_repo_path="/srv/home/dmuir/code/adk_evolutionary_landscape"
export src_path=$adk_repo_path/src/proteinnpt_clr

# Reference files for substitution and indel assays
export reference_file_path=$adk_data_path/pnpt/adk_reference_file.csv
export target_seq="MIIVLLGAPGAGKGTQSVLVAEKYGLKHISTGDLLREEIANNTELGKQAKKLIDGGNLVPDEMILGLLKNAFLNRGKGVVLDGFPRTLSQAEMMHPIVKGLAEKLSAVINIKLSEDEITQRIVLRRQCKNCGNIFNLRFIKNFDGKCPKCGSTDIYQRADDNEESAKNRINVYHSQTEPVVGFYKNKTYYKEVDGSKNKEEVFEEISKFINRKK"

# Folders contraining pretrained model checkpoints
export MSA_Transformer_location=$adk_data_path/pnpt/ESM/MSA_Transformer/esm_msa1b_t12_100M_UR50S.pt #Path to MSA Transformer checkpoint
export Tranception_location=$adk_data_path/pnpt/Tranception/Tranception_Large #Path to Tranception checkpoint
export ESM2_650M_location=$adk_data_path/pnpt/ESM/ESM2/esm2_t33_650M_UR50D.pt #Path to ESM2 checkpoint

# Folder where ADK experimental data is stored (provided in data dependencies)
export adk_experimental_data_folder=$adk_data_path
export adk_experimental_data_filename_raw="adk_ml_dataset.csv"
export adk_experimental_data_filename="adk_ml_dataset_expanded.csv"

# Folders containing multiple sequence alignments (MSAs) and MSA weights (provided in data dependencies)
export MSA_data_folder=$adk_data_path/pnpt/MSA_files
export MSA_weight_data_folder=$adk_data_path/pnpt/MSA_weights

# Folders containing hhfilter and clustal omega utils (provided in data dependencies)
export path_to_hhfilter=$adk_data_path/pnpt/utils/hhfilter #Path to hhfilter
export path_to_clustalomega=$adk_data_path/pnpt/utils/clustal-omega #Path to clustal omega

# Folder containing sequence embeddings for the different models
export embeddings_folder=$adk_data_path/pnpt/embeddings

# Folder containing zero-shot fitness predictions
export zero_shot_scores_folder=$adk_data_path/pnpt/zero_shot_fitness_predictions