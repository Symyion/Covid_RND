import pandas as pd


class ChainID:
    excel_path = "data/chains.xlsx"

    def __init__(self, data_path):
        self.path = data_path

    def transform_long(self, excel_path):
        wide = pd.read_csv(self.path)
        long = wide.stack().reset_index(level=1).reset_index(level=0, drop=True).dropna()
        long.columns = ['obs_month', 'chain_key']
        return long.drop_duplicates(subset=['chain_key']).to_excel(excel_path, index=False)

    def convert_chains(self, excel_path):
        raw_data = pd.read_csv(self.path, header=[0, 1])
        data_transposed = pd.DataFrame(raw_data.T.stack())
        data_transposed = data_transposed.reset_index(level=2, drop=True).reset_index(level=1).reset_index(level=0)
        data_transposed.columns = ['obs_month', 'index', 'chain_id']
        data_transposed = data_transposed.drop_duplicates(subset=['chain_id'])
        return data_transposed.to_excel(excel_path, index=False)
