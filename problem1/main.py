from graham import Graham, Point
from relacje import Relacje, Porter
from graph import Graph
import user
import math


points = [Point(9, 12), Point(27, 23), Point(81, 19), Point(72, 1), Point(31, 10), Point(0, 0), Point(12, 18), Point(20, 8), Point(50, 15), Point(65, 4), Point(30, 15), Point(40, 15)]
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1), (6, 8), (1, 8), (8, 9), (9, 10), (10, 4), (11, 12)]
# points = []
# edges = []
graham = Graham(points)
graph = Graph(points, edges)


while True:
    user.displayMenu()
    userInput = input("Wybierz opcje: ")

    # Dodanie punktow
    if userInput == '1':
        user.askForPoints(points)

    # Dodanie krawedzi
    elif userInput == '2':
        user.askForEdges(points, edges)

    # Wyswietlenie otoczki
    elif userInput == '3':
        graham.updatePoints(points)
        graham.plotConvexHull()

    # Wyswietlenie otoczki oraz grafu
    elif userInput == '4':
        graham.updatePoints(points)
        graham.plotConvexHull()
        graph.updatePointsAndGraph(points, edges)
        graph.plotNetwork(graham)

    # Wyswietlenie drogi od fabryki do punktu odbioru
    elif userInput == '5':
        graham.updatePoints(points)
        graph.updatePointsAndGraph(points, edges)
        user.displayPoints(points)
        factory = int(input("Podaj numer punktu będącego fabryką: "))
        pickup_place = int(input("Podaj numer punktu będącego miejscem odbioru: "))
        distance, path = graph.dijkstra(factory, pickup_place)
        if distance >= float('inf'):
            print(f"Brak połączenia z punktu {factory} do punktu {pickup_place}")
        else:
            print(f"Najkrótsza droga z punktu {factory} do punktu {pickup_place}: {round(distance, 2)}")
            print("Ścieżka:", ' -> '.join(f"({p.x}, {p.y})" for p in path))
            graph.plotNetworkWithPath(graham, path)

    # Wyswietlenie punktow
    elif userInput == '6':
        user.displayPoints(points)

    # Zakonczenie programu
    elif userInput == '7':
        print("Zakończono program.")
        break

    # Bledna opcja
    else:
        print("Nieznana opcja. Powtorz operacje:")


#Przykład użycia klasy relacje
# num_porters = int(input("Podaj liczbę tragarzy: "))
# relacje = Relacje(num_porters)
# relacje.display_relations()ions()