import csv
genres = ['Drama.csv', 'Fantansy.csv', 'Historical.csv', 'Mystery.csv', 'Satire.csv', 'Sci-fi.csv','Social.csv', 'Superhero.csv', 'Thriller.csv','Tear-Jeak.csv','Urban.csv', 'Western.csv']

for filename in genres:
    with open(filename, 'w') as new_file:
        csv_write = csv.writer(new_file)