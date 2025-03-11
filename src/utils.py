import matplotlib.pyplot as plt
import matplotlib
import numpy as np

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

def plot_confidence_interval(ax: plt.Axes, 
                             x: list, 
                             y_mean: np.ndarray,
                             y_ci: np.ndarray, 
                             color, 
                             label, 
                             linewidth=4,
                             point_size=100, 
                             alpha=0.2,):

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