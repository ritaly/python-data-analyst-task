import pandas as pd
from db_management import populate_table


PDSDAT_df = pd.read_csv("https://data.heroku.com/dataclips/eqxbztkzhrxglwwandwdezjnyphf.csv")
populate_table(table_name="PDSDAT", df=PDSDAT_df)
