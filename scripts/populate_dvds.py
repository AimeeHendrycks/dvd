#!/usr/bin/env python
#populating default and additional ones
import csv
import sys
import os
from unidecode import unidecode
sys.path.append('..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


from main.models import Dvd, Genre, Studio


print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "dvd_csv.csv"

#print "%s%s" % (dir_name, file_name)
#print "{0}/{1}".format(dir_name, file_name)

dvd_csv = os.path.join(dir_name, file_name)

print dvd_csv
csv_file = open(dvd_csv, 'r')

reader = csv.DictReader(csv_file)
print reader

inc = 1
for row in reader:
    inc += 1
    print inc
    #mysql START
    new_genre, created = Genre.objects.using('mysql').get_or_create(genre=unidecode(row['Genre']))
    new_studio, created = Studio.objects.using('mysql').get_or_create(studio=unidecode(row['Studio']))

    new_mysql_dvd, created = Dvd.objects.using('mysql').get_or_create(dvd_id=row['ID'])
    new_mysql_dvd.title = unidecode(row['DVD_Title'])
    print 'MySQL: ' + str(new_mysql_dvd.title) + ', ' + str(new_mysql_dvd.id)
    new_mysql_dvd.released = row['Released']
    new_mysql_dvd.status = row['Status']
    new_mysql_dvd.sound =  row['Sound']
    new_mysql_dvd.versions = row['Versions'] 
    new_mysql_dvd.price = row['Price']
    new_mysql_dvd.rating = row['Rating']
    new_mysql_dvd.year = row['Year']
    new_mysql_dvd.genre = new_genre
    new_mysql_dvd.studio = new_studio
    new_mysql_dvd.aspect = row['Aspect']
    new_mysql_dvd.upc = row['UPC']
    new_mysql_dvd.dvd_release_date = row['DVD_ReleaseDate']
    new_mysql_dvd.timestamp = row['Timestamp']
# mysql STOP


    new_mysql_dvd.save()



csv_file.close()






