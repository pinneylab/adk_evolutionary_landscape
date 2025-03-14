import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import json
from argparse import ArgumentParser
import os
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)

# models
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR


def fit_model_eval_spearman(model, X_train, y_train, X_test, y_test,):    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return spearmanr(y_test, y_pred)[0]

def main():
    parser = ArgumentParser()
    parser.add_argument("--split_dict", type=str, required=True, help="Path to the split dictionary JSON file")
    parser.add_argument("--ohe_df", type=str, required=True, help="Path to the one-hot encoding csv file")
    parser.add_argument("--esm_df", type=str, required=True, help="Path to the ESM embedding csv file")
    parser.add_argument("--dataset", type=str, required=True, help="Path to the dataset csv file containing acitvity data")
    parser.add_argument("--out_dir", type=str, default=Path(parent_dir)/ "data", help="Output directory for results")
    args = parser.parse_args()

    dataset = pd.read_csv(args.dataset)
    dataset.set_index("org_name", inplace=True)

    one_hot_encodings = pd.read_csv(args.ohe_df)
    one_hot_encodings.set_index("org_name", inplace=True)

    esm_embeddings = pd.read_csv(args.esm_df)
    esm_embeddings.set_index("org_name", inplace=True)

    split_dict = json.load(open(args.split_dict, 'rb'))
    models = [("SVR", SVR()), ("RF", RandomForestRegressor(random_state=314))]
    features = [("one-hot", one_hot_encodings), ("esm", esm_embeddings)]
    targets = ["log10_kcat", "log10_km"]

    result_rows = []

    for kv in list(split_dict.items()):
        split_num = kv[0]
        print(f"Start split {split_num}")
        np.random.seed(int(split_num))
        test_train_dict = kv[1]

        for feature_name, feature_df in features:
            for target in targets:
            
                test = feature_df.loc[test_train_dict['test']]
                X_test = test.values
                y_test = dataset.loc[test_train_dict['test'], target].values

                for train_subset_id, train_subset_orgs in test_train_dict.items():
                    
                    if train_subset_id == "test":
                        continue
                    
                    for model_name, model in models:
                        
                        split_size = int(train_subset_id.split("_")[-1])
                        
                        train = feature_df.loc[train_subset_orgs]
                        X_train = train.values
                        y_train = dataset.loc[train_subset_orgs, target].values

                        test_spearman = fit_model_eval_spearman(model, X_train, y_train, X_test, y_test)

                        result_rows.append({
                        "split_num": split_num,
                        "model": model_name,
                        "target": target,
                        "feature": feature_name,
                        "spearman": test_spearman,
                        "train_size": split_size
                        })
        print(f"Done with split {split_num}")
    result_df = pd.DataFrame(result_rows)
    result_df.to_csv(Path(args.out_dir) / "bootstrapped_ml_titration_results.csv", index=False)

if __name__ == "__main__":
    main()