import pandas as pd
import matplotlib.pyplot as plt

# intialise data of lists.
data = {'Column1':['True', 'False', 'True', 'True'],
        'Column2':['True', 'False', 'False', 'True'],
        'Column3':['True', 'False', 'True', 'True']}
df = pd.DataFrame(data)

def make_graph(df):
    # df will be the csv file from where we are selecting data in tru false format.
    data_new = pd.DataFrame({'True':[sum(df.Column1 == 'True'),sum(df.Column2 == 'True'),sum(df.Column3 == 'True')],
            'False':[sum(df.Column1 == 'False'),sum(df.Column2 == 'False'),sum(df.Column3 == 'False')],
                }, index = ['Column1', 'Column2','Column3'])

    # print(df)
    # print(data_new)

    # create stacked bar chart for data_new DataFrame
    data_new.plot.barh(stacked=True, color=['red', 'pink'])
    
    # Add Title and Labels
    plt.title('True False Result')
    plt.xlabel('Number of Ocurances')
    plt.legend(bbox_to_anchor=(0.9, 1))
    plt.savefig("graph.png")

make_graph(df)