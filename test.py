aex_wide = pd.read_csv('data/aex.csv')
aex_long = aex_wide.stack().reset_index(level=1).reset_index(level=0, drop=True)
aex_long.columns = ['obs_month', 'chain_key']
aex_clean = aex_long.dropna().drop_duplicates()
