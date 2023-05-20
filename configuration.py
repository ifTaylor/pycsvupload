from csv_upload import Columns

class CSVSettings:
    file = f'./file_to_upload.csv'
    columns = {
            Columns.Col1: 'ColA',
            Columns.Col2: 'ColB',
            Columns.Col3: 'ColC',
            Columns.Col4: 'ColD'
        }