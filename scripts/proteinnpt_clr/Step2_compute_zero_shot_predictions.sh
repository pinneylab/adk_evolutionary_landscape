#!/bin/bash
source adk_config.sh
source activate adk_env

export DMS_index=0
export batch_size_inference=1

python zero_shot_fitness_tranception.py \
    --checkpoint ${Tranception_location} \
    --batch_size_inference ${batch_size_inference} \
    --DMS_reference_file_path ${reference_file_path} \
    --DMS_data_folder ${adk_experimental_data_folder} \
    --DMS_index ${DMS_index} \
    --output_scores_folder $zero_shot_scores_folder/Tranception \
    --indel_mode \
    --clustal_omega_location ${path_to_clustalomega} \
    --scoring_window 'optimal'

python merge_zero_shot.py \
    --DMS_reference_file_path ${reference_file_path} \
    --DMS_mutants_folder ${adk_experimental_data_folder} \
    --zero_shot_scores_folder ${zero_shot_scores_folder} \
    --DMS_index ${DMS_index} \
    --indel_mode
