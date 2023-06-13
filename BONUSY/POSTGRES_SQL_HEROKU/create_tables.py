from db_management import create_table


PDSDAT_schema = """
nazwa_zmiennej VARCHAR NOT NULL,
kraj VARCHAR NOT NULL,
wojewodztwo VARCHAR NOT NULL,
status_zdajacych VARCHAR NOT NULL,
plec VARCHAR NOT NULL,
typ_informacji_z_jednostka_miary VARCHAR NOT NULL,
rok VARCHAR NOT NULL,
wartosc VARCHAR NOT NULL
"""

create_table(table="PDSDAT", schema=PDSDAT_schema)
