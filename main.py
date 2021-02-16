import sqlite3
import tools


connection = sqlite3.connect("data/option_data.db")
print(connection.total_changes)

chains = tools.ChainConverter('data/index_keys.csv')
chains.write_calls_to_excel()
#cursor = connection.cursor()
#cursor.execute("CREATE TABLE chains (obs_month TEXT, index_name TEXT, maturity INTEGER, chain_id TEXT)")

