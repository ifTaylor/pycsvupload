from configuration import CSVSettings
from csv_upload import CsvUpload

if __name__ == "__main__":
    csv = CsvUpload(
        file_path=CSVSettings.file,
        columns=CSVSettings.columns
    )

    data = csv.unpack_csv()

    for row in data:
        print(row)