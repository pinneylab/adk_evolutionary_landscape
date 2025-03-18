import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
from typing import List

def plot_barplot_trust_by_lidtype(method_trust_dict: dict, 
                                  lid_types: List[str], 
                                  k: int,
                                  title: str):
    """
    Plot a barplot of trustworthiness by lidtype.

    Parameters
    ----------
    method_trust_dict : dict
        A dictionary containing trustworthiness values for different methods.
    lid_types : List[str]
        A list of lid types.
    k : int
        The number of neighbors to consider.
    title : str
        The title of the plot.

    Returns
    -------
    None
    """

    fig, ax = plt.subplots(figsize=(10, 8))

    idx = k - 3
    df_dict = {"Lidtype": ["All"] + lid_types}
    for method, trust_dict in method_trust_dict.items():
        df_dict[method] = [trust_dict[lidtype][idx] for lidtype in ["all"] + lid_types]

    trustworthiness_df = pd.DataFrame(df_dict)

    trustworthiness_df = trustworthiness_df.melt(id_vars="Lidtype", var_name="Method", value_name="Trustworthiness")
    sns.barplot(data=trustworthiness_df, x="Lidtype", y="Trustworthiness", hue="Method", ax=ax, palette="colorblind")

    # set one-hot to be hatched
    for i, bar in enumerate(ax.patches):
        print(i, bar)
        if 8 > i > 3:
            bar.set_hatch("//")
        if i == 9:
            bar.set_hatch("//")

    ax.set_xlabel("Lid-Type")
    ax.set_ylabel("Trustworthiness")
    
    ax.axhline(y=method_trust_dict["ESM-2"]["perfect"][2], color='r', linestyle='--', label="Perfect")
    ax.axhline(y=method_trust_dict["ESM-2"]["shuffled"][2], color='grey', linestyle='--', label="Random")

    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    plt.show()
    #plt.savefig("../data/fig_pdfs/esm_onehot_lidtype_trustworthiness.pdf")

def plot_confidence_interval(ax: plt.Axes, 
                             x: list, 
                             y_mean: np.ndarray,
                             y_ci: np.ndarray, 
                             color, 
                             label, 
                             linewidth=4,
                             point_size=100, 
                             alpha=0.2,):
    """
    Plot a line plot with points and a confidence interval on a given axis.

    Parameters
    ----------
    ax : plt.Axes
        The axis to plot on.
    x : list
        The x-values for the plot.
    y_mean : np.ndarray
        The mean y-values for the plot.
    y_ci : np.ndarray
        The confidence interval for the y-values.
    color : str
        The color of the plot.
    label : str
        The label for the plot.
    linewidth : int, optional
        The width of the line (default is 4).
    point_size : int, optional
        The size of the points (default is 100).
    alpha : float, optional
        The transparency of the confidence interval (default is 0.2).
    Returns
    -------
    None

    """

    ax.plot(x,
            y_mean, 
            linewidth=linewidth, 
            label=label, 
            color=color)
    ax.scatter(x, 
               y_mean, 
               s=point_size, 
               color=color)
    ax.fill_between(x, 
                    y_mean - y_ci,
                    y_mean + y_ci, 
                    alpha=alpha, color=color)
    
def generate_col_colors(labels, palette='husl'):
    """
    Generate an array of colors based on string labels for use in Seaborn's clustermap.
    
    Parameters
    ----------
    labels : list of str
        A list of string labels.
    palette : str, optional
        The name of a Seaborn palette to generate colors from.
        
    Returns
    -------
    col_colors : list of RGB tuples
        A list of colors corresponding to the labels.
    """
    unique_labels = np.unique(labels)
    n_unique_labels = len(unique_labels)
    
    # Generate a color palette
    colors = sns.color_palette(palette, n_unique_labels)
    
    # Map labels to colors
    label_to_color = dict(zip(unique_labels, colors))
    col_colors = [label_to_color[label] for label in labels]
    
    return col_colors, label_to_color


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