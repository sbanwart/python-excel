from openpyxl import load_workbook

wb = load_workbook(filename='data.xlsx')

games = wb['Sheet1']

for x in range(1, 8):
    print(games['A' + str(x)].value + ' ' + games['B' + str(x)].value)
