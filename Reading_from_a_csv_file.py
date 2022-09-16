#We import the CSV Python library
import csv
serials = []
with open('Sample_Inventory.csv') as csv_file: 
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                serials.append(row["serial_number"])
                    
print(serials)


