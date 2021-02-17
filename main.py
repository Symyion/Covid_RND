import sqlite3
import tools

chains = tools.OptionChainConverter()
chains.get_calls(write_excel=True)
#cursor = connection.cursor()
#cursor.execute("CREATE TABLE chains (obs_month TEXT, index_name TEXT, maturity INTEGER, chain_id TEXT)")

