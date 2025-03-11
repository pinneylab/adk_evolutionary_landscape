import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from sklearn.manifold import trustworthiness

#https://stackoverflow.com/questions/7404116/defining-the-midpoint-of-a-colormap-in-matplotlib
def shifted_color_map(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    '''
    Function to offset the "center" of a colormap. Useful for
    data with a negative min and positive max and you want the
    middle of the colormap's dynamic range to be at zero.
    Input
    -----
      cmap : The matplotlib colormap to be altered
      start : Offset from lowest point in the colormap's range.
          Defaults to 0.0 (no lower offset). Should be between
          0.0 and `midpoint`.
      midpoint : The new center of the colormap. Defaults to
          0.5 (no shift). Should be between 0.0 and 1.0. In
          general, this should be  1 - vmax / (vmax + abs(vmin))
          For example if your data range from -15.0 to +5.0 and
          you want the center of the colormap at 0.0, `midpoint`
          should be set to  1 - 5/(5 + 15)) or 0.75
      stop : Offset from highest point in the colormap's range.
          Defaults to 1.0 (no upper offset). Should be between
          `midpoint` and 1.0.
    '''
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }
    # regular index to compute the colors
    reg_index = np.linspace(start, stop, 257)
    # shifted index to match the data
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False),
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])
    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)
        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))
    newcmap = matplotlib.colors.LinearSegmentedColormap(name, cdict)
    #plt.register_cmap(cmap=newcmap)
    return newcmap

def format_pval(p):
    if p > 0.01:
        return f"p = {p:.2f}"
    else:
        return f"p < 10^" + str(int(np.ceil(np.log10(p))))
    
def confidence_interval(data, z=1.96):
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
