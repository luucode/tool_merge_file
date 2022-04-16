# pip3 install glob2
# pip install pandas
# pip install openpyxl

import os, glob
import pandas as pd


def merge_excel(file_path):
    # setting the path for joining multiple files
    files = os.path.join(file_path, "*.xlsx")

    # list of merged files returned
    files = glob.glob(files)

    # joining files with concat and read_excel
    df = pd.concat(map(pd.read_excel, files), ignore_index=True)

    # sắp xếp lại theo cột Keyword, nếu muốn sắp xếp theo cột nào thì điền tên cột đó vô phần này và bỏ dấu # đi để chạy
    # df.sort_values("Keyword", inplace = True)

    # xoá trùng lập theo cột keyword
    df.drop_duplicates(subset ="Keyword", keep = 'first', inplace = True)
    print(df)

    # Tạo ra file excel mới
    df.to_excel( "output_excel/merge_file_excel.xlsx", index=False, encoding='utf-8-sig')


if __name__ == '__main__':
    file_path = "file_excel"
    merge_excel(file_path)