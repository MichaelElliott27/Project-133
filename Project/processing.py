import csv

data=[]
with open ("merged_dataset.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planet_data=data[1:]

for data_point in planet_data:
    data_point[2]=data_point[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])
with open ("final.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerrows(planet_data)

with open ("final.csv") as input,open("final.csv","w",newline="") as output:
    writer=csv.writer(output)
for row in csv.reader(input):
    if any(field.strip() for field in row):
        writer.writerow(row)