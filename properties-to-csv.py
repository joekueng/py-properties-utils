import csv
import os

def convert_properties_to_excel(input_file):

    csv_filepath = 'temp.csv'

    with open(input_file, 'r', encoding='utf-8') as prop_file, \
         open(csv_filepath, 'w', newline='', encoding='utf-8') as csv_file:

        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['Chiave', 'Valore'])

        for line in prop_file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                writer.writerow([key, value])


    os.system(f'start excel "{csv_filepath}"')
    input("Press Enter after saving the file")
    os.remove(csv_filepath)

if __name__ == '__main__':
    input_file = 'C:\\work\\project\\opc\\hybris\\bin\\custom\\opc\\opccore\\resources\\localization\\opccore-locales_en.properties'
    convert_properties_to_excel(input_file)

