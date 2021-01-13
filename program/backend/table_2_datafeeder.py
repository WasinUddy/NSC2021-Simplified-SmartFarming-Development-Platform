import pandas as pd


class ThirdTable:

    def __init__(self):
        self.table = {'INPUT': [], 'OUTPUT': []}

    def add_data(self, added_data):
        self.table['INPUT'].append(added_data['INPUT'])
        self.table['OUTPUT'].append(added_data['OUTPUT'])

    def convert_to_pandas_dataframe(self):
        return pd.DataFrame.from_dict(self.table)
