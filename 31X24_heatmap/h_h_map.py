import numpy as np
import os
import matplotlib.pyplot as plt

def create_dashboard_occ_heatmap(heat_map_data,save_path,**kwargs):

    ## y-axis - list of ylabels : M1 , M2
    ## x-axis - list of labels : [1-24]
    ## values - array of integers : [1,3,4,0,2] - people detected hourly.(order of data should be 1 to 24)

    ''' excepted data format

        heat_map_data = {"M1":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
                        "M2":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]}
        
        
    '''

    hm_y_labels = list(heat_map_data.keys())
    hm_x_labels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

    max_hours = len(list(heat_map_data.values())[0])
    hm_x_labels = hm_x_labels[:(max_hours)]

    hm_values = np.array(list(heat_map_data.values()))
    hm_new_value = hm_values

    fig, ax = plt.subplots(figsize=(10,2))
    # FIGURE size manupilation. dynamically

    im = ax.imshow(hm_new_value, **kwargs)
    #cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)

    ax.set_xticks(np.arange(len(hm_x_labels)), labels=hm_x_labels)
    ax.set_yticks(np.arange(len(hm_y_labels)), labels=hm_y_labels)
    
    # Loop over data dimensions and create text annotations.
    for i in range(len(hm_y_labels)):
        for j in range(len(hm_x_labels)):
            text = ax.text(j, i, hm_new_value[i, j],
                        ha="center", va="center", color="b")

    ax.set_title("")
    #fig.tight_layout()
    fig_savename = os.path.join(save_path , "dash_occ_heatmap.png")
    fig.savefig(fig_savename)
    #image = Image.open(fig_savename)
    return fig
    #plt.show()