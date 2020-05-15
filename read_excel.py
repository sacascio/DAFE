#!/usr/bin/env python3
import read_dafe

excel_file = 'DC2_SOE.xlsx'
# this will be expanded on
excel_obj = read_dafe.Dafe(excel_file)
print (excel_obj.show())