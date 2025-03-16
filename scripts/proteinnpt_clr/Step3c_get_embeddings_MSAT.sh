#!/bin/bash
source adk_config.sh
conda activate adk_env

export model_type='MSA_Transformer'
export embeddings_folder_MSAT=$embeddings_folder/$model_type
export num_MSA_sequences=384

python $src_path/embeddings.py \
    --model_type ${model_type} \
    --model_location ${MSA_Transformer_location} \
    --input_data_location ${adk_experimental_data_folder} \
    --output_data_location ${embeddings_folder_MSAT} \
    --indel_mode \
    --target_seq ${target_seq} \
    --path_to_clustalomega ${path_to_clustalomega} \
    --path_to_hhfilter ${path_to_hhfilter} \
    --MSA_data_folder ${MSA_data_folder} \
    --MSA_weight_data_folder ${MSA_weight_data_folder} \
    --num_MSA_sequences ${num_MSA_sequences} \
    --assay_reference_file_location ${reference_file_path}