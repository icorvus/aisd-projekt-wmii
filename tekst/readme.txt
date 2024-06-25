# Dokumentacja Problemu 2. (kodowanie melodii)

## Zastosowane algorytmy:

- Algorytm Huffmana:
   - złożoność (odpowiednio: budowa drzewa, kodowanie):
      - czasowa: O(NlogN), O(N)
      - pamięciowa: O(N), O(1)
- Algorytm KMP:
   - złożoność (utworzenie tablicy prefiksów, zastępowanie wzorca)
      - czasowa: O(m), O(n + m)
      - pamiętciowa: O(m), O(n)

## Polecenie 

Musimy przetworzyć ciąg tekstu.
- PRZED zapisem trzeba zamienić substringa "poli" na "boli".
- Kompresujemy tekst, koniecznie bezstratnie oraz...
- zapisujemy go w postaci zer i jedynek tak,
aby dało się go przywrócić do pierwotnej postaci (zdekodować).

## Obsługa

Program domyślnie zczytuje z pliku "in/infile.txt", zaś zapisuje do pliku "out/outfile.txt".
Użytkownik może przy uruchomieniu nadpisać te ścieżki, za pomocą argumentów "-i" oraz "-o".
Do dekodowania należy dodatkowo podać ścieżkę pliku .json zawierającego słownik kodowania.
Więcej informacji na ten temat dostarczy podanie argumentu "-h".

## Interpretacja

Należy zamienić każde wystąpienie dźwięku "poli" na "boli," na przykład przy pomocy 
algorytmu Knutha-Morrisa-Pratta

Musimy znaleźć sposób na przechowanie melodii dla przyszłych pokoleń płaszczaków, aby 
uchronić ją przed zapomnieniem po inwazji Istot z Trzeciego Wymiaru. Kodowanie to musi 
koniecznie być odwracalne. Możemy posługiwać się jedynie dwiema wartościami - 0 bądź 1.

Lepszą metodą kodowania niż zaproponowane przez Informatyka kodowanie każdej litery
przy pomocy pięciu bitów, jest kodowanie oparte o algorytm Huffmana, bowiem wymaga mniej 
miejsca w Maszynie. 
