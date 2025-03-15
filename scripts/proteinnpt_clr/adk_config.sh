# This config file contains the paths to all relevant data objects used by the ProteinNPT codebase. Only the next two lines should be updated based on your particular setup
export adk_data_path="Set this path to a location where model checkpoints and other large files will be saved"
export adk_repo_path="Set this path to the root of the adk_evolutionary_landscape repository"
export src_path=$adk_repo_path/src/proteinnpt_clr

# Reference files for substitution and indel assays
export reference_file_path=$adk_repo_path/scripts/proteinnpt_clr/adk_reference_file.csv
export target_seq="MIIVLLGAPGAGKGTQSVLVAEKYGLKHISTGDLLREEIANNTELGKQAKKLIDGGNLVPDEMILGLLKNAFLNRGKGVVLDGFPRTLSQAEMMHPIVKGLAEKLSAVINIKLSEDEITQRIVLRRQCKNCGNIFNLRFIKNFDGKCPKCGSTDIYQRADDNEESAKNRINVYHSQTEPVVGFYKNKTYYKEVDGSKNKEEVFEEISKFINRKK"

# Folders contraining pretrained model checkpoints
export MSA_Transformer_location=$adk_data_path/ESM/MSA_Transformer/esm_msa1b_t12_100M_UR50S.pt #Path to MSA Transformer checkpoint
export Tranception_location=$adk_data_path/Tranception/Tranception_Large #Path to Tranception checkpoint
export ESM2_650M_location=$adk_data_path/ESM/ESM2/esm2_t33_650M_UR50D.pt #Path to ESM2 checkpoint

# Folder where ADK experimental data is stored (provided in data dependencies)
export adk_experimental_data_folder=$adk_data_path/adk_experimental_data
export adk_experimental_data_filename_raw="20240822_adk_dataset_org_swap_update.csv"
export adk_experimental_data_filename="20240822_adk_dataset_org_swap_update_expanded.csv"

# Folders containing multiple sequence alignments (MSAs) and MSA weights (provided in data dependencies)
export MSA_data_folder=$adk_data_path/MSA_files
export MSA_weight_data_folder=$adk_data_path/MSA_weights

# Folders containing hhfilter and clustal omega utils (provided in data dependencies)
export path_to_hhfilter=$adk_data_path/utils/hhfilter #Path to hhfilter
export path_to_clustalomega=$adk_data_path/utils/clustal-omega #Path to clustal omega

# Folder containing sequence embeddings for the different models
export embeddings_folder=$adk_data_path/embeddings

# Folder containing zero-shot fitness predictions
export zero_shot_scores_folder=$adk_data_path/zero_shot_fitness_predictions