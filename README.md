# Python data science / data analyst task

## Zadanie

Na stronie https://dane.gov.pl/en/dataset/1946/resource/35560 można znaleźć dane dotyczące liczby osób, które przystąpiły oraz zdały maturę w latach 2010-2021 z uwzględnieniem podziału na województwo oraz płeć.

Zadanie polega na napisaniu skryptu, który umożliwiłby przeanalizowanie danych i znalezienie odpowiedzi na następujące pytania:

1) obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa na przestrzeni lat, do podanego roku włącznie, np.

2015 - 123456,

gdzie 123456 jest średnią z lat (2010-2015)

2) obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat, np.

2010 - 50 %
2011 - 52 %
2012 - 57 %
itd. ...
3) podanie województwa o najlepszej zdawalności w konkretnym roku, np.

rok - województwo A

4) wykrycie województw, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku), jeżeli takowe znajdują się w zbiorze, np.

województwo A: 2012 -> 2013
województwo B: 2017 -> 2018

5) porównanie dwóch województw - dla podanych dwóch województw wypisanie, które z województw miało lepszą zdawalność w każdym dostępnym roku, np. przy porównaniu województwa A i B

2010 - A
2011 - B
2012 - B
2013 - A
itd. ...

Zaprojektowanie interfejsu linii poleceń to część tego zadania. Każdy z tych punktów powinien być zrealizowany jako osobna komenda wywoływana z tego samego skryptu. Dodatkowo dla każdej z komend powinny być dostępne filtry:
- osoby bez rozróżnienia na płeć (domyślny, jeżeli użytkownik nie podał inaczej)
- tylko kobiety
- tylko mężczyźni

Wymagania techniczne:

- Python 3.x
- wykorzystanie tylko modułów dostępnych w standardowej bibliotece (nie dotyczy zadań bonusowych)
- README z opisem jak postawić projekt oraz spisem dostępnych komend
- testy jednostkowe z użyciem pytest
- kod napisany obiektowo
- (bonus) pobieranie danych z API lub pliku znajdującego się na serwerze, zamiast pliku lokalnego
- (bonus) napisanie skryptu, który jednorazowo wgrywałby dane do bazy danych (sqlite) oraz pobieranie ich z bazy przy wywołaniu komend

Prośba o umieszczenie rozwiązania w publicznie dostępnym repozytorium systemu kontroli wersji git (github, bitbucket, gitlab itp.)

FAQ:

1) Czy dozwolone będzie użycie biblioteki X do przetwarzania danych z pliku CSV?
Prośba o niekorzystanie z zewnętrznych bibliotek przy tworzeniu logiki aplikacji. Przewidujemy jedynie użycie zewnętrznych paczek dla testów, zadań bonusowych i ewentualnie interfejsu linii poleceń. 
W README można umieścić notatkę, czego i w jaki sposób by się użyło, gdyby owo ograniczenie nie występowało (jaka biblioteka, funkcja, czemu byśmy jej użyli, przykładowy fragment kodu), co będzie dodatkowo punktowane

2) Plik po pobraniu zawiera "dziwne znaczki" zamiast polskich znaków. Czy należy tak plik zostawić?
W przypadku wystąpienia tego problemu należy plik poprawić (ręcznie lub automatycznie), żeby zawierał poprawne polskie znaki
