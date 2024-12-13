import xml.etree.ElementTree as ET
import csv

class DataReader:
    def read_xml(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = []
        for item in root.findall('item'):
            city = item.get('city')
            street = item.get('street')
            house = item.get('house')
            floor = item.get('floor')
            data.append((city, street, house, floor))
        return data

    def read_csv(self, file_path):
        data = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                city = row['city']
                street = row['street']
                house = row['house']
                floor = row['floor']
                data.append((city, street, house, floor))
        return data
