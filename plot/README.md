**Dokumentacja (Problem 1)** 

**Klasa BasePoint** 

**Opis:** Klasa BasePoint reprezentuje punkt na płaszczyźnie z współrzędnymi x i y. 

**Konstruktor:** **Parametry wejściowe:** 

- x (float): Współrzędna x punktu. 
- y (float): Współrzędna y punktu. 

**Złożoność czasowa:** 

- O(1) 

**Opis działania:** Konstruktor inicjalizuje obiekt klasy BasePoint z podanymi współrzędnymi x i y. 

**Metoda** \_\_str\_\_**:** **Wartość zwracana:** 

- (str): Reprezentacja tekstowa punktu w formacie ClassName(x, y). 

**Złożoność czasowa:** 

- O(1) 

**Opis działania:** Metoda zwraca reprezentację tekstową punktu. 

**Klasa LandPoint** 

**Opis:** Klasa LandPoint dziedziczy po klasie BasePoint i nie dodaje żadnej dodatkowej funkcjonalności. Jest używana do oznaczenia punktów lądowych w aplikacji. 

**Konstruktor:** 

Dziedziczy konstruktor od klasy BasePoint. **Parametry wejściowe:** 

- x (float): Współrzędna x punktu. 
- y (float): Współrzędna y punktu. 

**Złożoność czasowa:** 

- O(1) 

**Opis działania:** Konstruktor inicjalizuje obiekt klasy LandPoint z podanymi współrzędnymi x i y. 

**Klasa World** 

**Opis:** Klasa World reprezentuje świat o określonej szerokości i wysokości, zawierający punkty lądowe oraz opcjonalnie punkty ogrodzenia. 

**Metoda** set\_fence\_points **Parametry wejściowe:** 

- points (list[BasePoint]): Lista punktów ogrodzenia. 

**Opis działania:** Metoda ustawia punkty ogrodzenia świata. 

**Metoda** count\_points **Wartość zwracana:** 

- (tuple): Krotka zawierająca liczbę punktów na ogrodzeniu oraz liczbę punktów wewnątrz ogrodzenia. 

**Opis działania:** Metoda zlicza liczbę punktów na ogrodzeniu i wewnątrz ogrodzenia. Jeśli punkty ogrodzenia nie są ustawione, zwraca (0, 0). 

**Klasa WorldGenerator** 

**Opis:** Klasa WorldGenerator służy do generowania punktów lądowych oraz tworzenia świata. 

**Metoda** generate\_land\_points **Parametry wejściowe:** 

- number\_of\_points (int): Liczba punktów lądowych do wygenerowania. 

**Wartość zwracana:** 

- (list[LandPoint]): Lista wygenerowanych punktów lądowych. 

**Opis działania:** Metoda generuje określoną liczbę punktów lądowych w losowych pozycjach w granicach świata. 

**Metoda** generate\_world **Parametry wejściowe:** 

- number\_of\_points (int): Liczba punktów lądowych do wygenerowania. 

**Wartość zwracana:** 

- (World): Wygenerowany obiekt klasy World. 

**Opis działania:** Metoda generuje świat z określoną liczbą punktów lądowych. 

**Klasa WorldVisualizer** 

**Opis:** Klasa WorldVisualizer zawiera metody do wizualizacji świata i jego ogrodzenia. 

**Statyczna metoda** plot\_world **Parametry wejściowe:** 

- world (World): Obiekt klasy World do wizualizacji. 

**Opis działania:** Metoda tworzy wykres punktów lądowych świata. 

**Statyczna metoda** plot\_fence 

**Parametry wejściowe:** 

- world (World): Obiekt klasy World do wizualizacji ogrodzenia. 

**Opis działania:** Metoda tworzy wykres ogrodzenia świata. Jeśli punkty ogrodzenia nie są ustawione, wyświetla odpowiedni komunikat. 

**Klasa GrahamScan** 

**Opis:** Klasa GrahamScan implementuje algorytm Grahama do znajdowania otoczki wypukłej dla danego zestawu punktów na płaszczyźnie. 

**Metoda** find\_convex\_hull **Parametry wejściowe:** 

- points (list[BasePoint]): Lista punktów, dla których ma zostać znaleziona otoczka wypukła. 

**Wartość zwracana:** 

- (list[BasePoint]): Lista punktów tworzących otoczkę wypukłą w porządku przeciwnym do ruchu wskazówek zegara. 

**Opis działania:** 

1. Znajduje punkt o najmniejszej współrzędnej y (a jeśli jest kilka, wybiera ten o najmniejszej współrzędnej x) jako punkt początkowy p0. 
1. Sortuje wszystkie punkty według kąta polarny utworzonego z p0. 
1. Przechodzi przez posortowane punkty i wykorzystuje stos do budowy otoczki wypukłej, usuwając punkty, które nie są częścią otoczki. 

**Złożoność czasowa:** 

- O(n log n) - sortowanie punktów. 

**Metoda** \_is\_clockwise **Parametry wejściowe:** 

- p1 (BasePoint): Punkt pierwszy. 
- p2 (BasePoint): Punkt drugi. 
- p3 (BasePoint): Punkt trzeci. 

**Wartość zwracana:** 

- (bool): True, jeśli punkty p1, p2 i p3 są ułożone w porządku zgodnym z ruchem wskazówek zegara; w przeciwnym razie False. 

**Opis działania:** Metoda sprawdza, czy punkty p1, p2 i p3 tworzą zakręt zgodny z ruchem wskazówek zegara. 

**Złożoność czasowa:** 

- O(1) 

**Metoda** \_by\_polar\_angle **Parametry wejściowe:** 

- p1 (BasePoint): Punkt pierwszy. 
- p2 (BasePoint): Punkt drugi. 

**Wartość zwracana:** 

- (float): Różnica kątów polarnych między punktami p1 i p2 względem punktu początkowego p0. 

**Opis działania:** Metoda sortuje punkty według kątów polarnych tworzonych z p0. Jeśli kąty są równe, sortuje według odległości od p0. 

**Złożoność czasowa:** 

- O(1) 

**Metoda** \_distance\_between **Parametry wejściowe:** 

- p1 (BasePoint): Punkt pierwszy. 
- p2 (BasePoint): Punkt drugi. 

**Wartość zwracana:** 

- (float): Odległość euklidesowa między punktami p1 i p2. 

**Opis działania:** Metoda oblicza odległość euklidesową między dwoma punktami na płaszczyźnie. **Złożoność czasowa:** 

- O(1) 

**Klasa ConvexHullSearcher** 

**Opis:** Klasa ConvexHullSearcher służy do znajdowania otoczki wypukłej dla danego zestawu punktów na płaszczyźnie za pomocą algorytmu Grahama. 

**Konstruktor:** **Parametry wejściowe:** 

- points (list[BasePoint]): Lista punktów, dla których ma zostać znaleziona otoczka wypukła. 

**Metoda** find\_convex\_hull 

**Wartość zwracana:** 

- (list[BasePoint]): Lista punktów tworzących otoczkę wypukłą w porządku przeciwnym do ruchu wskazówek zegara. 

**Opis działania:** Metoda deleguje znajdowanie otoczki wypukłej do algorytmu Grahama. **Złożoność czasowa:** 

- O(n log n) 

**Klasa EdmondsKarp** 

**Opis:** Klasa EdmondsKarp implementuje algorytm Edmonda-Karpa do znajdowania maksymalnego przepływu w sieci przepływowej. 

**Konstruktor:** 

**Parametry wejściowe:** 

- capacity\_matrix (2D array-like): Macierz pojemności krawędzi w sieci przepływowej. 

**Opis działania:** Konstruktor inicjalizuje obiekt klasy EdmondsKarp z podaną macierzą pojemności oraz tworzy macierz przepływu wypełnioną zerami. 

**Metoda** bfs **Parametry wejściowe:** 

- source (int): Wierzchołek źródłowy. 
- sink (int): Wierzchołek docelowy. 
- parent (list[int]): Lista przechowująca ścieżkę augmentacyjną. 

**Wartość zwracana:** 

- (bool): True, jeśli istnieje ścieżka z source do sink, w przeciwnym razie False. 

**Opis działania:** Metoda wykonuje przeszukiwanie wszerz (BFS) w celu znalezienia ścieżki z dodatnią przepustowością z source do sink. Aktualizuje listę parent, aby zapisać ścieżkę. 

**Złożoność czasowa:** 

- O(V^2) w najgorszym przypadku dla grafu z macierzą sąsiedztwa. 

**Metoda** edmonds\_karp **Parametry wejściowe:** 

- source (int): Wierzchołek źródłowy. 
- sink (int): Wierzchołek docelowy. 

**Wartość zwracana:** 

- (int): Wartość maksymalnego przepływu z source do sink. 

**Opis działania:** Metoda implementuje algorytm Edmonda-Karpa, który wielokrotnie wykonuje BFS, aby znaleźć ścieżkę augmentacyjną. Dla każdej znalezionej ścieżki, zwiększa przepływ o minimalną przepustowość na tej ścieżce. Aktualizuje przepływy w obu kierunkach dla każdej krawędzi na ścieżce. 

**Złożoność czasowa:** 

- O(V \* E^2) dla grafu z macierzą sąsiedztwa, gdzie V to liczba wierzchołków, a E to liczba krawędzi. 

**Klasa Graph** 

**Opis:** Klasa Graph reprezentuje graf skierowany z określoną liczbą wierzchołków, krawędziami oraz pojemnościami krawędzi. Jest używana do implementacji algorytmu Edmonda-Karpa do znajdowania maksymalnego przepływu w sieci. 

**Metoda** add\_edge **Parametry wejściowe:** 

- u (int): Wierzchołek początkowy krawędzi. 
- v (int): Wierzchołek końcowy krawędzi. 
- cap (int): Pojemność krawędzi. 

**Opis działania:** Metoda dodaje krawędź z wierzchołka u do v z pojemnością cap. Równocześnie dodaje krawędź odwrotną z pojemnością 0. 

**Metoda** bfs **Parametry wejściowe:** 

- s (int): Wierzchołek źródłowy. 
- t (int): Wierzchołek docelowy. 
- parent (list[int]): Lista przechowująca ścieżkę augmentacyjną. 

**Wartość zwracana:** 

- (bool): True, jeśli istnieje ścieżka z s do t, w przeciwnym razie False. 

**Opis działania:** Metoda wykonuje przeszukiwanie wszerz (BFS) w celu znalezienia ścieżki z dodatnią przepustowością z s do t. Aktualizuje listę parent, aby zapisać ścieżkę. 

**Złożoność czasowa:** 

- O(V + E), gdzie V to liczba wierzchołków, a E to liczba krawędzi. 

**Metoda** edmonds\_karp\_relations **Parametry wejściowe:** 

- source (int): Wierzchołek źródłowy. 
- sink (int): Wierzchołek docelowy. 

**Wartość zwracana:** 

- (int): Wartość maksymalnego przepływu z source do sink. 

**Opis działania:** Metoda implementuje algorytm Edmonda-Karpa, który wielokrotnie wykonuje BFS, aby znaleźć ścieżkę augmentacyjną. Dla każdej znalezionej ścieżki, zwiększa przepływ o minimalną przepustowość na tej ścieżce. Aktualizuje przepływy w obu kierunkach dla każdej krawędzi na ścieżce. 

**Złożoność czasowa:** 

- O(V \* E^2), gdzie V to liczba wierzchołków, a E to liczba krawędzi. 

**Funkcja build\_graph** 

**Opis:** Funkcja tworzy graf na podstawie podanych osób i ich relacji. **Parametry wejściowe:** 

- people (list[dict]): Lista osób, gdzie każda osoba jest reprezentowana jako słownik z kluczami id i hands. 
- relations (list[tuple]): Lista relacji pomiędzy osobami, każda relacja jest krotką (u, v). 

**Wartość zwracana:** 

- (Graph, int, int, list[int], list[int]): Zwraca obiekt grafu, wierzchołek źródłowy, wierzchołek docelowy, listę wierzchołków z rękami front i listę wierzchołków z rękami back. 

**Opis działania:** Funkcja tworzy graf dwudzielny, dodając krawędzie między wierzchołkiem źródłowym a osobami z rękami front, oraz między osobami z rękami back a wierzchołkiem docelowym. Dodaje także krawędzie między osobami z odpowiednimi relacjami. 

**Funkcja draw\_graph** 

**Opis:** Funkcja rysuje graf dwudzielny na podstawie podanych osób i ich relacji. 

**Parametry wejściowe:** 

- people (list[dict]): Lista osób. 
- relations (list[tuple]): Lista relacji pomiędzy osobami. 
- front\_ids (list[int]): Lista wierzchołków z rękami front. 
- back\_ids (list[int]): Lista wierzchołków z rękami back. 

**Opis działania:** Funkcja tworzy i wyświetla wykres grafu dwudzielnego, używając kolorów do oznaczenia różnych grup wierzchołków. 

**Funkcja read\_input** 

**Opis:** Funkcja odczytuje dane wejściowe dotyczące liczby osób, ich atrybutów oraz relacji. 

**Wartość zwracana:** 

- (list[dict], list[tuple]): Lista osób oraz lista relacji. 

**Opis działania:** Funkcja pobiera od użytkownika liczbę osób, atrybuty każdej osoby (czy ma ręce front czy back) oraz relacje między nimi, kończąc na komendzie end 

**UTHILS** 

**Funkcja read\_points\_and\_matrix** 

**Opis:** Funkcja wczytuje punkty i macierz z pliku tekstowego. 

**Parametry wejściowe:** 

- filename (str): Nazwa pliku, z którego mają zostać wczytane dane. 

**Wartość zwracana:** 

- (list[tuple[float, float]], np.ndarray): Lista punktów w formacie (x, y) oraz macierz sąsiedztwa. 

**Opis działania:** 

1. Odczytuje liczbę punktów z pierwszej linii pliku. 
1. Wczytuje kolejne linie, interpretując je jako współrzędne punktów. 
1. Wczytuje macierz sąsiedztwa, interpretując każdą linię jako rząd macierzy. 
1. Przekształca listę wczytanych wierszy na macierz numpy. 

**Złożoność czasowa:** 

- O(n^2), gdzie n to liczba punktów (ze względu na przetwarzanie macierzy). 

**Funkcja read\_relations** 

**Opis:** Funkcja wczytuje relacje między osobami z pliku tekstowego. 

**Parametry wejściowe:** 

- filename (str): Nazwa pliku, z którego mają zostać wczytane dane. 

**Wartość zwracana:** 

- (list[dict], list[tuple[int, int]]): Lista osób oraz lista relacji między nimi. 

**Opis działania:** 

1. Odczytuje liczbę osób z pierwszej linii pliku. 
1. Wczytuje kolejne linie, interpretując je jako atrybuty osób (ręce front lub back). 
1. Wczytuje relacje między osobami, każdą linię interpretując jako parę indeksów osób. 

**Złożoność czasowa:** 

- O(n + r), gdzie n to liczba osób, a r to liczba relacji. 

**Funkcja generate\_points\_and\_matrix** 

**Opis:** Funkcja generuje losowe punkty oraz losową macierz sąsiedztwa. 

**Parametry wejściowe:** 

- num\_points (int): Liczba punktów do wygenerowania. 

**Wartość zwracana:** 

- (list[tuple[float, float]], np.ndarray): Lista wygenerowanych punktów oraz macierz sąsiedztwa. 

**Opis działania:** 

1. Generuje losowe punkty w przedziale od 0 do 100. 
1. Tworzy symetryczną macierz sąsiedztwa z losowymi wartościami od 1 do 10, z zerami na przekątnej. 

**Złożoność czasowa:** 

- O(n^2), gdzie n to liczba punktów (ze względu na tworzenie macierzy). 
