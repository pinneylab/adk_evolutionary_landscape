#!/bin/bash
source adk_config.sh
source activate adk_env

export model_type='Tranception'
export embeddings_folder_Tranception=$embeddings_folder/$model_type

python embeddings.py \
    --model_type ${model_type} \
    --model_location ${Tranception_location} \
    --input_data_location ${adk_experimental_data_folder} \
    --output_data_location ${embeddings_folder_Tranception} \
    --indel_mode \
    --target_seq ${target_seq} \
    --path_to_clustalomega ${path_to_clustalomega} \
    --path_to_hhfilter ${path_to_hhfilter} \
    --assay_reference_file_location ${reference_file_path}