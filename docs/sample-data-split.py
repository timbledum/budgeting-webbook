"""To dos!
- Make date optional
- Mix up the output formats and names of the different accounts
"""

import petl


def split_table(table, column):
    values = set(table[column])
    for v in values:
        yield table.select(column, lambda r: r == v)


def main():
    """The main function which extracts the data from the sample-data
    spreadsheet and splits it to a csv per account"""

    sheet_data = petl.fromxlsx('sample-data.xlsx', sheet='Data')
    data = sheet_data.cut(*range(5))
    early_data = data.select('Date', lambda r: r.month <= 2)

    for table in split_table(early_data, 'Account'):
        table.tocsv(table['Account'][0]+'.csv')


if __name__ == '__main__':
    main()
