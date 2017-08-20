"""To dos!
- Make date optional
- Mix up the output formats and names of the different accounts
"""

import petl


def bank_main(table):
    print('main')
    return table


def bank_savings(table):
    print('savings')
    return table


def bank_credit(table):
    print('credit')
    return table


def split_table(table, column):
    values = set(table[column])
    for v in values:
        yield v, table.select(column, lambda r: r == v).cut(*range(4))


def main():
    """The main function which extracts the data from the sample-data
    spreadsheet and splits it to a csv per account"""

    bank_lookup = {
        'Spending': bank_main,
        'Income': bank_main,
        'Saving': bank_savings,
        'Credit card': bank_credit,
    }

    sheet_data = petl.fromxlsx('sample-data.xlsx', sheet='Data')
    data = sheet_data.cut(*range(5))
    early_data = data.select('Date', lambda r: r.month <= 2)

    for account, table in split_table(early_data, 'Account'):
        modified_table = bank_lookup[account](table)
        # modified_table.tocsv(table['Account'][0]+'.csv')
        print(modified_table)


if __name__ == '__main__':
    main()
