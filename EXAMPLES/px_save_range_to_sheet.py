#!/usr/bin/env python
"""
Copy a range from an existing spreadsheet
to a new sheet
"""
import openpyxl as px

WB = '../DATA/presidents.xlsx'

def main():
    """program entry point"""
    wb = px.load_workbook(WB)
    ws = wb['US Presidents']
    ws2 = wb.create_sheet('President Names')
    save_range_to_new_worksheet(ws, ws2)
    wb.close()

# save as:
#   wb.save("presidents4.xlsx")

def save_range_to_new_worksheet(ws, ws2):
    """Print first and last names of all presidents"""

    for row in ws['B2':'C46']:
        for col in row:
            ws2[col.coordinate] = col.value

if __name__ == '__main__':
    main()
