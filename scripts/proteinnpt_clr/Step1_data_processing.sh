#!/bin/bash
source adk_config.sh
source activate adk_env

python data_processing.py $adk_experimental_data_folder $adk_experimental_data_filename
