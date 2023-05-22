import pandas as pd
from enum import Enum
import csv

class Columns(Enum):
    Col1 = 'col1'
    Col2 = 'col2'
    Col3 = 'col3'
    Col4 = 'col4'

class CsvUpload:
    def __init__(self, file_path, columns):
        self.file_path = file_path
        self.columns = columns
        self.df = pd.DataFrame()

    def unpack_csv(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = [row for row in reader]

        self.df = pd.DataFrame(data, columns=headers)

        unpacked_data = [
            {
                'ID': index + 1,
                **{
                    column_name: row[column_name]
                    for column_name in self.columns.values()
                }
            }
            for index, row in self.df.iterrows()
        ]

        return unpacked_data

    def get_ids_by_column_value(self, column_name, value):
        matched_ids = []
        for index, row in self.df.iterrows():
            if row[column_name] == value:
                matched_ids.append(row['ID'])
        return matched_ids