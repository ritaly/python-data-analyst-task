import pandas as pd
from db_management import populate_table


PDSDAT_df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT8rjDwUmmIprIHEJbi1bRN9w83ULhrdtlHoHK7gYkJvdTnJi8smXhrCbTsxc4Sh8iKbDC2kivkKTyI/pub?gid=0&single=true&output=csv")
populate_table(table_name="PDSDAT", df=PDSDAT_df)
