# BONUSY

## BONUS 1 - pobieranie danych z API lub pliku znajdującego się na serwerze, zamiast pliku lokalnego

Arkusz pomocniczy w Google Sheets:

https://docs.google.com/spreadsheets/d/1ksRYtgapnIE7pOs5OBjk4zFUOndT3p_IUjXWV9rM5BI

Plik w formacie CSV:

https://docs.google.com/spreadsheets/d/e/2PACX-1vT8rjDwUmmIprIHEJbi1bRN9w83ULhrdtlHoHK7gYkJvdTnJi8smXhrCbTsxc4Sh8iKbDC2kivkKTyI/pub?gid=0&single=true&output=csv

Quickstart:

https://developers.google.com/sheets/api/quickstart/python

Plik odpowiedzialny za to zadanie: import_csv_data_from_api.py
<br>
## BONUS 2 - POSTGRES SQL HEROKU

Link do bazy danych:

https://data.heroku.com/dataclips/eqxbztkzhrxglwwandwdezjnyphf

Plik w formacie CSV:

https://data.heroku.com/dataclips/eqxbztkzhrxglwwandwdezjnyphf.csv

Plik w formacie JSON:

https://data.heroku.com/dataclips/eqxbztkzhrxglwwandwdezjnyphf.json

Integracja z Google Sheets:

=IMPORTDATA("https://data.heroku.com/dataclips/eqxbztkzhrxglwwandwdezjnyphf.csv")

Pliki odpowiedzialne za to zadanie znajduję się w folderze: POSTGRES_SQL_HEROKU

Na podstawie tutoriala:

https://towardsdatascience.com/how-to-build-a-relational-database-from-csv-files-using-python-and-heroku-20ea89a55c63?gi=29ed887411cc

Następnie możemy przetestować tak utworzoną bazę danych i odczytać ją w całości za pomocą pliku read_database.py.
<br>
## WNIOSKI

Aby uzsykać miarodajne wyniki do analizy i porównania zdawalności matur w Polsce pomiędzy poszczególnymi województwami - musimy wprowadzić przelicznik na 10000 mieszkańców z danej populacji dla województw.

Pomocniczy wykres punktowy do analizy danych na tym etapie:

https://scv2pl.github.io/Dash-Plotly_PDSDAT_PL.html

Pomocniczy wykres punktowy "Liczba osób, które przystąpiły oraz zdały maturę w latach 2010-2022 w Polsce w przeliczeniu na 10000 mieszkańców z populacji dla danego województwa.":

https://scv2pl.github.io/Dash-Plotly_PDSDAT_+Population_10000_PL.html

Jest to wstępny wykres, gdyż przydałoby się pozyskać dane populacji dla województw - dla każdego roku z osobna. Dane populacji które użyłem do tego wykresu są średnią z roku 2010 i 2021 - reprezentuje ona wartość dla każdego roku na wykresie. Prezentowana "Wartość/10000" jest przelicznikiem na 10000 mieszkańców z populacji dla danego województwa. Przeprowadziłem taki zabieg w celach: czysto - porównawczych, gdyż większe populacje z założenia mają większe liczby przystępujących do matur niż mniejsze populacje. Oś x wykresu reprezentowana jest przez populacje dla danego województwa i również jest średnią z roku 2010 i 2021 - reprezentuje ona wartość dla każdego roku na wykresie. Przeprowadziłem taki zabieg - aby rozciągnąć dane dla województw na wykresie: od najmniejszej populacji do największej.  

Pomocniczy wykres punktowy "Procent osób które zdały maturę w latach 2010-2022 w Polsce":

https://scv2pl.github.io/Dash-Plotly_PDSDAT_+Population_PL.html

Kolejnym etapem który sobie założyłem - jest przygotowanie plików Python-a, które będę generowały dane CSV dla tych wykresów automatycznie za pomocą zapytań SQL do bazy danych Heroku Postgres SQL. Gdyż obecne wykresy reprezentują dane CSV z arkuszy "Google Sheet":

https://docs.google.com/spreadsheets/d/1ksRYtgapnIE7pOs5OBjk4zFUOndT3p_IUjXWV9rM5BI/edit#gid=0 ,

aby przeprowadzić wstępną analizę wyżej opisanych przypadków.

<hr>

