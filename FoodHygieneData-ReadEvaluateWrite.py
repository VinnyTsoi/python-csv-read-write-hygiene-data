import csv
from datetime import date

with open('foodhygienedata.csv','r') as file:
    reader = csv.DictReader(file, delimiter = ',')
    
#   fieldnames = reader.fieldnames
    fieldnames = ['establishmentname','inspectiondate','dayssinceinspection']
    
    with open('daysSinceInspection.csv','w') as newFile:
        writer = csv.DictWriter(newFile, fieldnames = fieldnames, delimiter = ',')
        writer.writeheader()
        
        newDict = {}
        
        for row in reader:
            inspectiondate = row['inspectiondate']
            if not (row['inspectiondate']):
                continue
            else:
                day, month, year = inspectiondate.split('/')
                d0 = date(int(year), int(month), int(day))
                d1 = date.today()
                delta = d1 - d0
                print("{0} was inspected on {1}. {2} days since inspection".format(row['establishmentname'], inspectiondate, delta.days))
                newDict['establishmentname'] = row['establishmentname']
                newDict['inspectiondate'] = inspectiondate
                newDict['dayssinceinspection'] = delta.days
                writer.writerow(newDict)