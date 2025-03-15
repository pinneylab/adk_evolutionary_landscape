# This config file contains the paths to all relevant data objects used by the ProteinNPT codebase. Only the next two lines should be updated based on your particular setup
export adk_data_path=/scratch-ssd/pastin/ProteinNPT/ADK_repro
export adk_repo_path=/users/pastin/projects/open_source/ProteinNPT/ADK_repro
export proteinnpt_data_path=/scratch-ssd/pastin/ProteinNPT

# Reference files for substitution and indel assays
export reference_file_path=./adk_reference_file.csv
export target_seq="MIIVLLGAPGAGKGTQSVLVAEKYGLKHISTGDLLREEIANNTELGKQAKKLIDGGNLVPDEMILGLLKNAFLNRGKGVVLDGFPRTLSQAEMMHPIVKGLAEKLSAVINIKLSEDEITQRIVLRRQCKNCGNIFNLRFIKNFDGKCPKCGSTDIYQRADDNEESAKNRINVYHSQTEPVVGFYKNKTYYKEVDGSKNKEEVFEEISKFINRKK"

# Folder where ADK experimental data is stored
export adk_experimental_data_folder=$adk_data_path/adk_experimental_data
export adk_experimental_data_filename="20240822_adk_dataset_org_swap_update_expanded.csv"

# Folders containing multiple sequence alignments (MSAs) and MSA weights for all DMS assays
export MSA_data_folder=$adk_data_path/MSA_files
export MSA_weight_data_folder=$adk_data_path/MSA_weights

# Folders contraining pretrained model checkpoints
export MSA_Transformer_location=$proteinnpt_data_path/ESM/MSA_Transformer/esm_msa1b_t12_100M_UR50S.pt #Path to MSA Transformer checkpoint
export Tranception_location=$proteinnpt_data_path/Tranception/Tranception_Large #Path to Tranception checkpoint
export ESM2_650M_location=$proteinnpt_data_path/ESM/ESM2/esm2_t33_650M_UR50D.pt #Path to ESM2 checkpoint

# Folders containing hhfilter and clustal omega utils
export path_to_hhfilter=$proteinnpt_data_path/utils/hhfilter #Path to hhfilter
export path_to_clustalomega=$proteinnpt_data_path/utils/clustal-omega #Path to clustal omega

# Embedding location
export embeddings_folder=$adk_data_path/embeddings

# Folder containing zero-shot fitness predictions
export zero_shot_scores_folder=$adk_data_path/zero_shot_fitness_predictions