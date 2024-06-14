### Dokumentacja

#### Klasa RouteOptimizer

**Opis:**
Klasa `RouteOptimizer` służy do optymalizacji trasy patrolowej bazując na zadanej maksymalnej liczbie punktów które mogą być odwiedzone pod rząd bez zatrzymywania się oraz listy jasności tych punktów.

**Konstruktor:**
```python
def __init__(self, brightness: list[int], max_points: int) -> None:
```
- **Wejścia:**
  - `brightness`: lista całkowitych wartości reprezentujących jasność punktów.
  - `max_points`: maksymalna liczba punktów, które mogą być odwiedzone w jednej sekwencji.

#### Funkcja `naive_patrol_route_optimization`

**Opis:**
Funkcja `naive_patrol_route_optimization` służy do naiwnej optymalizacji trasy patrolowej, gdzie analizowane są punkty o zadanych jasnościach.

```python
def naive_patrol_route_optimization(self) -> tuple[int, list[int]]:
```
- **Wejścia:** Brak dodatkowych parametrów poza `self`.
- **Wyjścia:**
  - `melody_listened` (int): minimalna liczba odsłuchań melodii.
  - `stops` (list[int]): lista indeksów punktów, w których należy się zatrzymać.
- **Złożoność:** O(n), gdzie n jest liczbą punktów.

#### Klasa SegmentTree

**Opis:**
Klasa `SegmentTree` implementuje drzewo przedziałowe (segmentowe), które jest używane do efektywnego znajdowania maksimum na przedziale oraz aktualizacji wartości.

**Konstruktor:**
```python
def __init__(self, data: list[int]) -> None:
```
- **Wejścia:**
  - `data`: lista całkowitych wartości reprezentujących energię strażników.
- **Wyjścia:** Brak.
- **Złożoność:** O(n), gdzie n jest liczbą strażników.

#### Funkcja `build`

**Opis:**
Funkcja `build` jest odpowiedzialna za budowanie drzewa segmentowego na podstawie dostarczonych danych.

```python
def build(self, data: list[int]) -> None:
```
- **Wejścia:**
  - `data`: lista całkowitych wartości reprezentujących energię strażników.
- **Wyjścia:** Brak.
- **Złożoność:** O(n), gdzie n jest liczbą strażników.

#### Funkcja `update`

**Opis:**
Funkcja `update` aktualizuje wartość w drzewie segmentowym na danym indeksie i odpowiednio modyfikuje jego struktury.

```python
def update(self, index: int, value: int) -> None:
```
- **Wejścia:**
  - `index`: indeks wartości, która ma zostać zaktualizowana.
  - `value`: nowa wartość do zapisania pod podanym indeksem.
- **Wyjścia:** Brak.
- **Złożoność:** O(logn), gdzie n jest liczbą strażników.

#### Funkcja `query`

**Opis:**
Funkcja `query` zwraca maksimum na zadanym przedziale.

```python
def query(self, left: int, right: int) -> tuple[int, int]:
```
- **Wejścia:**
  - `left`: początek przedziału (włącznie).
  - `right`: koniec przedziału (wyłącznie).
- **Wyjścia:**
  - Krotka `(max_val, index)`, gdzie `max_val` to maksymalna wartość na zadanym przedziale, a `index` to indeks tej wartości.
- **Złożoność:** O(logn), gdzie n jest liczbą strażników.

#### Główna funkcja `main`

**Opis:**
Główna funkcja `main` wczytuje dane z plików, tworzy instancje `SegmentTree` oraz `RouteOptimizer`, a także przeprowadza odpowiednie operacje na tych strukturach danych.

```python
def main():
```
- **Wejścia:** Brak.
- **Wyjścia:** Brak.
- **Złożoność:** Zależy od wielkości wejściowych plików i wykonywanych operacji, w przybliżeniu O(n log n) dla operacji na drzewie segmentowym oraz O(m) dla optymalizacji trasy, gdzie n jest liczbą strażników, a m liczbą punktów.


### Przygotowanie plików wejściowych

Przed uruchomieniem programu należy stworzyć dwa pliki: `guards.txt` oraz `points.txt`.

#### Struktura pliku `guards.txt`

Plik powinien zawierać w pierwszej linii listę liczb całkowitych, każda liczba oddzielona spacją. Są to wartości energii strażników.

**Przykład zawartości `guards.txt`:**
```
10 20 15 30 25 50
```

#### Struktura pliku `points.txt`

Plik powinien zawierać dwie linie:
- Pierwsza linia zawiera jedną liczbę całkowitą reprezentującą maksymalną liczbę punktów, które mogą być odwiedzone w jednej sekwencji.
- Druga linia zawiera listę liczb całkowitych reprezentujących jasność punktów, każda liczba oddzielona spacją.

**Przykład zawartości `points.txt`:**
```
3
5 10 15 20 25 10 5
```

---

Upewnij się, że pliki są poprawnie przygotowane przed uruchomieniem programu.
