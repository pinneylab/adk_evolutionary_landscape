#!/bin/bash
source adk_config.sh
conda activate adk_pnpt_env

export model_config_location=$src_path/model_configs/PNPT_ESM2_650M.json
export embeddings_folder_ESM2_650M=$embeddings_folder/ESM2_650M

# Select one target config depending on experimental values to train model on
# Possible values are:
# - kinase_single_log10-kcat.json
# - kinase_single_log10-km.json
# - kinase_multi_log10-kcat_temp.json
# - kinase_multi_log10-kcat_temp_lid.json
# - kinase_multi_log10-kcat_log10-km_temp_lid.json
export target_config_location=$src_path/target_configs/kinase_multi_log10-kcat_log10-km_temp_lid.json

export model_name_suffix='adk_multi4_PNPT_ESM2' # Give a name to the model
export fold_index=0   # Integer included in [0,29] specifying the fold index
export train_size=140 # Size of training data [20|40|60|80|100|120|140]
export fold_variable_name=$fold_index"_train_size_"$train_size

python $src_path/train.py \
    --data_location ${adk_data_path} \
    --model_config_location ${model_config_location} \
    --embedding_model_location ${ESM2_650M_location} \
    --fold_variable_name ${fold_variable_name} \
    --target_config_location ${target_config_location} \
    --zero_shot_fitness_predictions_location ${zero_shot_scores_folder} \
    --training_fp16 \
    --sequence_embeddings_folder ${embeddings_folder_ESM2_650M} \
    --model_name_suffix ${model_name_suffix} \
    --indel_mode \
    --assay_data_location $adk_experimental_data_folder/$adk_experimental_data_filename \
    --target_seq ${target_seq} \
    --augmentation "None" \
    --test_fold_index 1