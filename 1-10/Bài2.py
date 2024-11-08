import zipfile
import pandas as pd
from io import TextIOWrapper 
#TextIOWrapper được sử dụng để xử lý các luồng văn bản. 
#Module io trong Python cung cấp các công cụ để làm việc với I/O (input/output), bao gồm cách xử lý và mở các luồng dữ liệu.
# Giải nén các files từ file zip
def extract_files(zip_file):
    with zipfile.ZipFile("test.zip", 'r') as zip_ref:
        file_list = zip_ref.namelist()
        for file in file_list:
            with zip_ref.open(file) as f:
                text = f.read().decode('utf-8')
                label = 1 if 'spam' in file else 0
                yield {'text': text, 'label': label}
#Hàm sử dụng thư viện Pandas để chuyển đổi dữ liệu từ generator thành DataFrame và ghi vào file CSV.
def write_to_csv(data, output_file):
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
#Hàm này kết hợp các bước trên để xử lý ZIP file và ghi dữ liệu vào file CSV.
def process_zip_file(zip_file, output_file):
    data = [x for x in extract_files(zip_file)]
    write_to_csv(data, output_file)
#Xử lý file zip chứa văn bản, đánh dấu là spam or not spam rồi ghi dữ liệu vào file CSV
process_zip_file('test.zip', 'test.csv')
    