from graham import Graham, Point

def askForPoints(points):
    while True:
        answer = input("Czy chcesz dodać punkt? (tak/nie): ").strip().lower()
        if answer == "nie":
            break
        x = float(input("Podaj współrzędną x punktu: "))
        y = float(input("Podaj współrzędną y punktu: "))
        point = Point(x, y)
        points.append(point)
        print(f"Dodano punkt {x, y}.")

def askForEdges(points, edges):
    while True:
        displayPoints(points)
        answer = input("Czy chcesz dodać krawędź? (tak/nie): ").strip().lower()
        if answer == "nie":
            break
        point1 = int(input("Podaj numer pierwszego punktu: "))
        point2 = int(input("Podaj numer drugiego punktu: "))
        if point1 != point2 and point1 > 0 and point2 > 0 and point1 <= len(points) and point2 <= len(points):
            edges.append((point1, point2))
        else:
            print("Nieprawidłowe numery punktów, spróbuj ponownie.")

def displayPoints(points):
    i = 1
    for point in points:
        if i%5 != 0:
            print(f"{i}. ({point.x}, {point.y}),", end="\t")
        else:
            print(f"{i}. ({point.x}, {point.y}),", end="\n")
        i += 1
    print("\n")

def displayMenu():
    options = ["Dodaj punkty", 
               "Dodaj krawedzie", 
               "Wyswietl otoczke", 
               "Wyswietl otoczke wraz z krawedziami", 
               "Znajdz droge od fabryki do punktu odbioru",
               "Wyswietl punkty", 
               "Wyjscie"
               ]
    i = 1
    for opt in options:
        print(f"{i}. {opt}")
        i += 1
