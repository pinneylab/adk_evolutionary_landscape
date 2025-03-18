#!/bin/bash
source adk_config.sh

export model_type='ESM2_650M'
export embeddings_folder_ESM2=$embeddings_folder/$model_type

uv run $src_path/embeddings.py \
    --model_type ${model_type} \
    --model_location ${ESM2_650M_location} \
    --input_data_location ${adk_experimental_data_folder} \
    --output_data_location ${embeddings_folder_ESM2} \
    --indel_mode \
    --target_seq ${target_seq} \
    --path_to_clustalomega ${path_to_clustalomega} \
    --path_to_hhfilter ${path_to_hhfilter} \
    --assay_reference_file_location ${reference_file_path}