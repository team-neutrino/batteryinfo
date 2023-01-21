import csv


def get_data(fname):
    with open(f"data/{fname}", newline='') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            if "12A" in row[0]:
                data.append(list(map(float, row[1:5])))
    return data



if __name__ == "__main__":

    fnames = ["Applejack-12A-1-21-2023_Applejack-12A-1-21-2023.csv",
            "Feta-12A-1-21-2023_Feta-12A-1-21-2023.csv",
            "Swiss-12A-1-21-2023_Swiss-12A-1-21-2023.csv",
            ]
    get_data(fnames[0])
