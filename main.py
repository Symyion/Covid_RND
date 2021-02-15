import sqlite3
import tools


connection = sqlite3.connect("data/option_data.db")
print(connection.total_changes)

AEX = tools.ChainID('data/index_keys.csv', 'AEX')
AEX.transform_long('data/aex.xlsx')
#cursor = connection.cursor()
#cursor.execute("CREATE TABLE chains (obs_month TEXT, index_name TEXT, maturity INTEGER, chain_id TEXT)")
