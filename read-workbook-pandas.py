import pandas

def process_excel():
    df = pandas.read_excel('data.xlsx')
    
    print(df.columns)
    
    FORMAT = ['Name', 'Status']
    
    selected = df[FORMAT]
    
    print(selected)

    print(df.iloc[0]['Name'])

    df['Achievements'] = df.index
    df['Completed'] = df.index

    df.loc[1, 'Achievements'] = 20
    df.loc[1, 'Completed'] = 30

    writer = pandas.ExcelWriter('data.xlsx', engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Sheet1')

    writer.save()

process_excel()
