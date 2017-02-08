import pandas

def print_excel():
    workbook = pandas.read_excel('data.xlsx')
    
    print(workbook.columns)
    
    FORMAT = ['Name', 'Status']
    
    selected = workbook[FORMAT]
    
    print(selected)

print_excel()
