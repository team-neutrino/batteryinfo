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
    del_ls = ["Applejack-12A-2-4-2023_Applejack-12A-2-4-2023.csv"]

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
            )
    labels = [s.split("-")[0] for s in fnames]
    for j in range(2):
        for i, fname in enumerate(fnames):
            axs[j].plot(data[i][0,:], data[i][j+1,:], label=labels[i])

    axs[0].grid()
    axs[0].set_ylabel("Voltage (V)")
    axs[1].set_ylabel("Current (A)")
    axs[1].set_xlabel("Time (s)")
    axs[0].legend()
    plt.show()
    fig.savefig(f'batteryVI.pdf')


if __name__ == "__main__":
    plot()
