import pandas as pd


class OptionChain:
    def __init__(self, csv_data_path='data/data.csv'):
        self.path = csv_data_path
        raw_data = pd.read_csv(self.path, header=[0, 1])
        data_transposed = pd.DataFrame(raw_data.T.stack())
        data_transposed = data_transposed.reset_index(level=2, drop=True).reset_index(level=1).reset_index(level=0)
        data_transposed.columns = ['obs_month', 'index', 'chain_id']
        self.data_transposed = data_transposed.drop_duplicates(subset=['chain_id'])

    def convert_chains(self, excel_path="data/chains.xlsx"):
        return self.data_transposed.to_excel(excel_path, index=False)
