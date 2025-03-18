#!/bin/bash
source adk_config.sh

uv run $src_path/data_processing.py $adk_experimental_data_folder $adk_experimental_data_filename_raw
