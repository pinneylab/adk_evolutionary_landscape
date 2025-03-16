#!/bin/bash
source adk_config.sh
conda activate adk_pnpt_env

python $src_path/data_processing.py $adk_experimental_data_folder $adk_experimental_data_filename_raw
