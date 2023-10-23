import csv, numpy, glob
import matplotlib.pyplot as plt

def get_data(fname):
    '''read data from csv file.
    '''
    with open(fname, newline='', mode="r") as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            if "12A" in row[0]:
                data.append(list(map(float, row[1:5])))
    return numpy.array(data).T

def plot():
    # Automatic retrieve file names in data folder
    fnames =glob.glob("./data/*csv")
  
    # get data from the list of files.
    data = [get_data(s) for s in fnames]

    # a 3x1 plot
    fig, axs = plt.subplots(2, 1,
            tight_layout=True,
            sharex=True,
            figsize=(4, 5.5),
            height_ratios=[4, 1]
            )
    
    labels = [s[len("./data/"):].split("-")[0] for s in fnames]
    # color = ['#6bfa43', '#fa9a25', '#face2f', '#25f6fa', '#0f84fa', '#e9f542', '#42f5bf', '#fc1921', '#99ebf0', '#837896', '#f547cc', '#bf2cf5', '#b596a4', '#fc038c', '#e9f542', '#277a2d', '#1c5922', '#bcfc26', '#fcba03']
    # choose default colors.
    for j in range(2):
        for i, _ in enumerate(fnames):
            # axs[j].plot(data[i][0,:], data[i][j+1,:], color = color[i], label=labels[i])
            axs[j].plot(data[i][0,:], data[i][j+1,:], label=labels[i])

    axs[0].grid()
    axs[0].set_ylabel("Voltage (V)")
    axs[1].set_ylabel("Current (A)")
    axs[1].set_xlabel("Time (s)")
    axs[0].legend(fontsize = 8)
    plt.show()
    fig.savefig('batteryVI.pdf')

if __name__ == "__main__":
    plot()