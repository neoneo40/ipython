# os.makedirs test purpose
import csv
import os
import platform

def ensure_dir(dir_):
    if not os.path.exists(dir_):
        os.makedirs(dir_)

python_version = int(platform.python_version_tuple()[0])
if python_version == 3: 
    os.makedirs('headerRemoved', exist_ok=True)
else:
    ensure_dir('headerRemoved')

# Looop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files
    print('Removing header from {}...'.format(csvFilename))
    
    # TODO: Read the CSV file in (skipping first row).
    csvRows = []
    with open(csvFilename) as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRows.append(row)
    
    # TODO: Write out the CSV file.
    with open(os.path.join('headerRemoved', csvFilename), 'w') as csvFileObj:
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)