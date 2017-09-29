import csv

with open('Team_2_ISR.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['StoryPoints'])

