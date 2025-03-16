import os,sys
import pandas as pd
import json

adk_data_path = sys.argv[1]
input_data_name = sys.argv[2]
data = pd.read_csv(os.path.join(adk_data_path,input_data_name))

with open("20240717_bootstrap_stratified_split.json", 'r') as file:
    folds = json.load(file)
    
# Collect all possible species and create the DataFrame columns
species_set = set()
train_sizes = ['train_size_20', 'train_size_40', 'train_size_60', 'train_size_80', 'train_size_100', 'train_size_120', 'train_size_140']
all_sizes = train_sizes + ['test']
for fold in folds:
    for size in all_sizes:
        species_set.update(folds[fold].get(size, []))

# Create empty DataFrame
species_set = list(species_set)
columns = [f"{fold}_{size}" for fold in folds.keys() for size in train_sizes if size!='test']
df = pd.DataFrame(index=species_set, columns=columns)

# Fill the DataFrame
for fold in folds:
    for size in train_sizes:
        column_name = f"{fold}_{size}"
        species_list = folds[fold].get(size, [])
        for species in species_list:
            df.loc[species, column_name] = 0
        species_list = folds[fold].get('test', [])
        for species in species_list:
            df.loc[species, column_name] = 1

data = pd.merge(data,df,how="left",left_on="org_name", right_index=True)
data.rename(columns={"sequence": "mutated_sequence"}, inplace=True)
output_filename = os.path.splitext(input_data_name)[0] + "_expanded.csv"
data.to_csv(os.path.join(adk_data_path,output_filename), index=False)