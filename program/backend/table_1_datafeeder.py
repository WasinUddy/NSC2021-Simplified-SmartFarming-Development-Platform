import pandas as pd


class SecondTable:

    def __init__(self):
        self.table = {'INPUT': [], 'OUTPUT': [], 'CONDITION': [], 'VALUE': []}

    def add_data(self, added_data):
        self.table['INPUT'].append(added_data['INPUT'])
        self.table['OUTPUT'].append(added_data['OUTPUT'])
        self.table['CONDITION'].append(added_data['CONDITION'])
        self.table['VALUE'].append(added_data['VALUE'])

    def convert_to_pandas_dataframe(self):
        return pd.DataFrame.from_dict(self.table)
