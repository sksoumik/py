import os

os.getcwd()
path = "./set 5/"
destination_path = "./renamed/"
for i, filename in enumerate(os.listdir(path)):
    os.rename(path + filename, destination_path + "0" + str(i + 56) + ".jpg")
