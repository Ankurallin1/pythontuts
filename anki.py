import csv
with open("d1_data.csv", mode="r") as i1:
    read = csv.reader(i1)
    D1 = {col1[0]: col1[1] for col1 in read}
    # print(D3)
    i1.close()

# print("heloo")