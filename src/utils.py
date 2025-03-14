import numpy as np
from sklearn.manifold import trustworthiness
from Bio import SeqIO
from typing import List
import pandas as pd
from evcouplings.couplings import CouplingsModel

def format_pval(p):
    """
    Format p-value for display.

    Parameters
    ----------
    p : float
        The p-value to format.
    Returns
    -------
    str
        Formatted p-value as a string.
    """
    if p > 0.01:
        return f"p = {p:.2f}"
    else:
        return f"p < 10^" + str(int(np.ceil(np.log10(p))))
    
def confidence_interval(data, z=1.96):
    """
    Calculate the confidence interval for a given dataset.

    Parameters
    ----------
    data : array-like
        The data for which to calculate the confidence interval.
    z : float, optional
        The z-score for the confidence level (default is 1.96 for 95% confidence).
    Returns
    -------
    np.ndarray
        The confidence interval for the data.
    """
    n = len(data)
    std_err = np.std(data)/np.sqrt(n)
    return z*std_err

def compute_trustworthiness_by_lidtype(df, lid_types, col_name, embedding_start_idx, embedding_end_idx, top_n_neighbors, metric="euclidean", random_shuffle_n=30):
    np.random.seed(314)

    trust_result_dict = {
        "perfect": [],
        "shuffled": [],
        "all": [],

    }
    for lidtype in lid_types:
        trust_result_dict[lidtype] = []
        trust_result_dict[lidtype + "_shuffled"] = []

    subset_dfs = []
    for lidtype in lid_types:
        subset_dfs.append(df[df["lid_type"] == lidtype])

    for k in range(3, top_n_neighbors+1):
        trust_result_dict["perfect"].append(trustworthiness(df[col_name].to_numpy().reshape(-1,1), df[col_name].to_numpy().reshape(-1,1), n_neighbors=k))
        trust_result_dict["all"].append(trustworthiness(df.iloc[:, embedding_start_idx:embedding_end_idx], df[col_name].to_numpy().reshape(-1,1), n_neighbors=k, metric=metric))
    
        for i, lidtype in enumerate(lid_types):
            lidtype_df = subset_dfs[i]
            trust_result_dict[lidtype].append(trustworthiness(lidtype_df.iloc[:, embedding_start_idx:embedding_end_idx], lidtype_df[col_name].to_numpy().reshape(-1,1), n_neighbors=k, metric=metric))
            lidtype_random = []
            for i in range(random_shuffle_n):
                lidtype_random.append(trustworthiness(lidtype_df.iloc[:, embedding_start_idx:embedding_end_idx], np.random.permutation(lidtype_df[col_name].to_numpy()).reshape(-1,1), n_neighbors=k, metric=metric))
            trust_result_dict[lidtype + "_shuffled"].append(np.mean(lidtype_random))
            
      
        all_random = []
        for i in range(random_shuffle_n):
            all_random.append(trustworthiness(df.iloc[:, embedding_start_idx:embedding_end_idx], np.random.permutation(df[col_name].to_numpy()).reshape(-1,1), n_neighbors=k, metric=metric))

        trust_result_dict["shuffled"].append(np.mean(all_random))
    return trust_result_dict

def seq_dict_from_fasta(fasta_path: str) -> dict:
    """
    Read a FASTA file and return a dictionary with sequence IDs as keys and sequences as values.

    Parameters
    ----------
    fasta_path : str
        Path to the FASTA file.
    Returns
    -------
    dict
        Dictionary with sequence IDs as keys and sequences as values.
    """
    seq_dict = dict()
    with open(fasta_path) as f:
        for record in SeqIO.parse(f, "fasta"):
            seq_dict[record.id] = str(record.seq)
    return seq_dict

def compute_hamiltonians(coupling_model_path: str,
                         model_name: str, 
                         seq_list: List[str],
                         org_name_list: List[str]) -> pd.DataFrame:
    """
    Compute global hamiltonians for a list of sequences using a specified coupling model.

    Parameters
    ----------
    coupling_model_path : str
        Path to the coupling model file.
    model_name : str
        Name of the model to be used.
    seq_list : List[str]
        List of sequences for which to compute the global hamiltonians.
    org_name_list : List[str]
        List of organism names corresponding to the sequences.
    Returns
    -------
    pd.DataFrame
        DataFrame containing the organism names and their corresponding global hamiltonians.
    """
    
    # read in couplings model
    model = CouplingsModel(coupling_model_path)

    # compute global hamiltonians across sequence
    hamiltonian_array = model.hamiltonians(seq_list)

    # convert to DataFrame with org_name and global hamiltonian
    hamiltonian_df = pd.DataFrame(hamiltonian_array[:,0], index=org_name_list)
    hamiltonian_df.reset_index(inplace=True)
    hamiltonian_df.rename(columns={"index": "org_name", 0: model_name}, inplace=True)
    
    return hamiltonian_df

def filter_msa_to_ref_seq(sequence_dictionary: dict, 
                          ref_seq_name: str) -> pd.DataFrame:
    
    """
    Filter a multiple sequence alignment (MSA) to remove columns with gaps in a specified reference sequence.

    Parameters
    ----------
    sequence_dictionary : dict
        Dictionary with sequence IDs as keys and sequences as values.
    ref_seq_name : str
        Name of the reference sequence to filter against.
    Returns
    -------
    pd.DataFrame
        DataFrame containing the filtered sequences.
    """
    
    # convert sequence dictionary to DataFrame
    df = pd.DataFrame(list(sequence_dictionary.items()), columns=["org_name", "seq"])
    
    # split seq into columns
    split_seq = df["seq"].str.split("", expand=True).iloc[:, 1:-1]

    # add org_names back
    df = pd.concat([df, split_seq], axis=1)

    # remove original seq column
    df.drop(columns=["seq"], inplace=True)

    # drop any column where reference sequence has a gap
    ref_index = df[df["org_name"] == ref_seq_name].index[0]
    ref_gaps = df.iloc[ref_index, 1:] == "-"
    df.drop(columns=df.columns[1:][ref_gaps], inplace=True)

    # merge seq into one column
    df["seq"] = df.iloc[:, 1:].apply(lambda x: "".join(x), axis=1)

    return df