# pip3 install glob2
# pip install pandas

import os, glob
import pandas as pd

def merge_csv(file_path):
    # setting the path for joining multiple files
    files = os.path.join(file_path, "*.csv")

    # list of merged files returned
    files = glob.glob(files)

    # joining files with concat and read_csv
    df = pd.concat(map(pd.read_csv, files), ignore_index=True)

    # sắp xếp lại theo cột Keyword, nếu muốn sắp xếp theo cột nào thì điền tên cột đó vô phần này và bỏ dấu # đi để chạy
    # df.sort_values("Keyword", inplace = True)

    # xoá trùng lập theo cột keyword
    df.drop_duplicates(subset ="Keyword", keep = 'first', inplace = True)
    print(df)

    # Tạo ra file csv mới
    df.to_csv( "output_csv/merge_file_csv.csv", index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    file_path = "file_csv"
    merge_csv(file_path)