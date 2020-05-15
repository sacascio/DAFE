#!/usr/bin/env python3
import read_dafe

excel_file = 'DC2_SOE.xlsx'

excel_obj = read_dafe.Dafe(excel_file)
print (excel_obj.show())