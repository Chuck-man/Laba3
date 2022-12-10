import os
import shutil
import csv

def copying_dataset(path: str, path_copier: str):

    """Функция принимает путь к файлам: path и путь к новой директории: path_new"""

    if not os.path.exists("dataset_copier"):
        os.mkdir("dataset_copier")

    source = os.listdir(path + "/")
    data = []

    for i in source:
        source_data = os.listdir(path + "/" + i)

        for j in source_data:
            shutil.copy(os.path.join(path + "/" + i, j), os.path.join(path_copier + "/", i + "__" + j))
            absolute = os.path.abspath(path + "/" + i + "/" + j)
            regarding = os.path.relpath(path + "/" + i + "/" + j)
            data.append([absolute, regarding, i])

    with open(path_copier + ".csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)

def main():
    copying_dataset("dataset", "dataset_copier")

if __name__ == "__main__":
    main()
