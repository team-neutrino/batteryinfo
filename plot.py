import csv, numpy
import matplotlib.pyplot as plt


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
    # list of file names.
    fnames = [
            "Applejack-12A-1-21-2023_Applejack-12A-1-21-2023.csv",
            "Feta-12A-1-21-2023_Feta-12A-1-21-2023.csv",
            "Swiss-12A-1-21-2023_Swiss-12A-1-21-2023.csv",
            "Battery1-12A_1_23_2023_Battery1-12A_1_23_2023.csv",
            "Camembert-12A-1-21-2023_Camembert-12A-1-21-2023.csv",
            "Battery2-12A-1-21-2023_Battery2-12A-1-21-2023.csv",
            "RainbowDash-12A-1-24-2023_RainbowDash-12A-1-24-2023.csv",
            "Swiss-12A-1-24-2023_Swiss-12A-1-24-2023.csv",
            "Fluttershy-12A-1-25-2023_Fluttershy-12A-1-25-2023.csv",
            "BatteryC-12A-1-25-2023_BatteryC-12A-1-25-2023.csv",
            "BatteryD-12A-1-25-2023_BatteryD-12A-1-25-2023.csv",
            "CDia-12A-1-25-2023_CDia-12A-1-25-2023.csv",
            "BatteryC-12A-1-28-2023_BatteryC-12A-1-28-2023.csv",
            "CDia-12A-1-28-2023_CDia-12A-1-28-2023.csv",
            "BatteryD-12A-1-30-2023_BatteryD-12A-1-30-2023.csv",
            "BatteryC-12A-1-30-2023_BatteryC-12A-1-30-2023.csv",
            "BatteryC-12A-1-31-2023_BatteryC-12A-1-31-2023.csv",
            "Battery1-12A-1-31-2023_Battery1-12A-1-31-2023.csv",
            "Battery1-12A-2-1-2023_Battery1-12A-2-1-2023.csv",
            "BatteryC-12A-2-1-2023_BatteryC-12A-2-1-2023.csv",
            "BatteryD-12A-2-2-2023_BatteryD-12A-2-2-2023.csv",
            "BatteryC-12A-2-2-2023_BatteryC-12A-2-2-2023.csv",
            "BatteryC-12A-2-4-2023_BatteryC-12A-2-4-2023.csv",
            "BatteryD-12A-2-4-2023_BatteryD-12A-2-4-2023.csv",
            "Battery1-12A-2-4-2023_Battery1-12A-2-4-2023.csv",
            # "Applejack-12A-2-4-2023_Applejack-12A-2-4-2023.csv",
            "BatteryD-12A-2-6-2023_BatteryD-12A-2-6-2023.csv",
            "Battery1-12A-2-6-2023_Battery1-12A-2-6-2023.csv",
            "Battery1-12A-2-7-2023_Battery1-12A-2-7-2023.csv",
            "Mercury-12A-2-7-2023_Mercury-12A-2-7-2023.csv",
            "Applejack-12A-2-22-2023_Applejack-12A-2-22-2023.csv",
            ]
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
