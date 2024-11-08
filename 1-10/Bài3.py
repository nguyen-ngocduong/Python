import zipfile
import pandas as pd
from io import TextIOWrapper 
def extract_files(zip_file):
    with zipfile.ZipFile("test.zip", 'r') as zip_ref:
        file_list = zip_ref.namelist()
        for file in file_list:
            with zip_ref.open(file) as f:
                text = f.read().decode('utf-8')
                label = 1
                yield {'text': text, 'label': label}
def write_to_csv(data, output_file):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
def process_zip_file(zip_file, output_file):
    data = [x for x in extract_files(zip_file)]
    write_to_csv(data, output_file)
process_zip_file('test.zip', 'data.csv')