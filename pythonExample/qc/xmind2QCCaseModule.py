# -*- encoding:utf-8 -*-
import os
import sys

__author__ = 'bida'

import xlrd
import xlwt

def generate(path):
    sheet_original = xlrd.open_workbook(path).sheet_by_index(0)
    table_new = xlwt.Workbook()
    sheet_new = table_new.add_sheet("Qc Case Module")

    rows = sheet_original.nrows
    columns = sheet_original.ncols
    for row in range(2, rows):
        for column in range(columns):
            sheet_new.write(row-2, column, sheet_original.row(row)[column].value)

    for row in range(2, rows):
        subject = sheet_original.row(0)[0].value
        for column in range(columns - 1):
            if sheet_original.row(row)[column+1].value != '':
                subject += sheet_original.row(row)[column].value + '\\'
            else:
                break
        sheet_new.write(row-2, columns+1, subject[:-1])

    for row in range(2, rows):
        for column in range(columns):
            if sheet_original.row(row)[column].value == '':
                sheet_new.write(row-2, columns+2, sheet_original.row(row)[column-1].value)
                break
            if column == columns - 1:
                sheet_new.write(row-2, columns+2, sheet_original.row(row)[column].value)

    table_new.save('qcCaseModule.xls')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.stdout.write(u'请指定xmind导出的excel文件')
    else:
        if os.path.isfile(sys.argv[1]):
            generate(sys.argv[1])
        else:
            sys.stdout.write(u'文件不存在')

