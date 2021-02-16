import pandas as pd


def transpose_data(raw_data):
    data_t = pd.DataFrame(raw_data.T.stack())
    data_t = data_t.reset_index(level=2, drop=True).reset_index(level=1).reset_index(level=0)
    data_t.columns = ['obs_month', 'index', 'chain_id']
    data_t = data_t.drop_duplicates(subset=['chain_id'])
    return data_t


class OptionChainConverter:
    def __init__(self, csv_data_path='data/data.csv'):
        self.path = csv_data_path
        self.data = transpose_data(pd.read_csv(self.path, header=[0, 1], dtype='str'))

    def get_all(self, data_path="data/chains.xlsx", write_excel=False):
        if write_excel:
            self.data.to_excel(data_path, index=False)
        return self.data

    def get_calls(self, call_path='data/calls.xlsx', write_excel=False):
        calls = self.data[self.data.chain_id.str.contains('#C', regex=True, na=False)]

        if write_excel:
            calls.to_excel(call_path, index=False)
        return calls

    def get_puts(self, put_path='data/put.xlsx', write_excel=False):
        puts = self.data[self.data.chain_id.str.contains('#P', regex=True, na=False)]

        if write_excel:
            puts.to_excel(put_path, index=False)
        return puts


class OptionDescriptionExtractor:
    def __init__(self, csv_description_path):
        self.path = csv_description_path
        self.raw_data = pd.read_csv(self.path)
        # TODO split description column into strike price, strike date & index name
