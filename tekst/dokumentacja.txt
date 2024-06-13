# Dokumentacja Problemu 2. (kodowanie melodii)

## Zastosowane algorytmy:

- Algorytm Huffmana:
   - złożoność (odpowiednio: budowa drzewa, kodowanie, dekodowanie):
      - czasowa: O(NlogN), O(N), O(N)
      - pamięciowa: O(N), O(1), O(1)

## Polecenie 

Musimy przetworzyć ciąg tekstu.
- PRZED zapisem trzeba zamienić substringa "poli" na "boli".
- Kompresujemy tekst, koniecznie bezstratnie oraz...
- zapisujemy go w postaci zer i jedynek tak,
aby dało się go przywrócić do pierwotnej postaci (zdekodować).

## Obsługa

Program domyślnie zczytuje z pliku "infile.txt", zaś zapisuje do pliku "outfile.txt".
Użytkownik może przy uruchomieniu nadpisać te ścieżki, za pomocą argumentów "-i" oraz "-o".
Więcej informacji na ten temat dostarczy podanie argumentu "-h".

## Interpretacja

Plik (w tym wypadku piosenka) jest na tyle mały, że do podmiany wzorca (zamiany dźwięków
poli na boli) wystarczy algorytm zachłanny
