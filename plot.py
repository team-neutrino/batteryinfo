import csv, numpy
import matplotlib.pyplot as plt
import os

def get_data(fname):
    '''read data from csv file.
    '''
    with open(f"data/{fname}", newline='') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            if "12A" in row[0]:
                data.append(list(map(float, row[1:5])))
    return numpy.array(data).T


def plot():
    fnames = os.listdir('data')
    del_ls = []

    fnames = [i for i in fnames if i not in del_ls]
    # get data from the list of files.
    data = [get_data(s) for s in fnames]

    print(data[0][0, :])
    print(data[0][1, :])
    # a 3x1 plot
    fig, axs = plt.subplots(2, 1,
            tight_layout=True,
            sharex=True,
            figsize=(4, 5.5),
            height_ratios=[4, 1]
            )
    
    labels = [s.split("-")[0] for s in fnames]
    color = ['#6bfa43', '#fa9a25', '#face2f', '#25f6fa', '#0f84fa', '#be11f2', '#1c5922', '#fc1921', '#99ebf0', '#837896', '#f547cc', '#bf2cf5', '#b596a4', '#a3c2a8', '#c2bf67', '#fa43776', '#825621', '#21211c']
    for j in range(2):
        for i, fname in enumerate(fnames):
            print(i)
            axs[j].plot(data[i][0,:], data[i][j+1,:], color = color[i], label=labels[i])

    axs[0].grid()
    axs[0].set_ylabel("Voltage (V)")
    axs[1].set_ylabel("Current (A)")
    axs[1].set_xlabel("Time (s)")
    axs[0].legend(fontsize = 8)
    plt.show()
    fig.savefig('batteryVI.pdf')

if __name__ == "__main__":
    plot()
