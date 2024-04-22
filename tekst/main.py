# konwertuje znaki na odpowiedniki w kodzie
def convert(character):
    if character == ',' or character == ';':
        return "11010"
    if character == ' ':
        return "11101"
    else:
        return format(ord(letter) - 97, "b").rjust(5, '0')

def swap_words(text):
    # co nalezy zmienic na co
    # jesli bedzie potrzeba zmienic cos jeszcze, dodajemy to tutaj
    swap_candidates = {
        "poli" : "boli"
    }

    text.translate(swap_candidates)

    # zamiana wystapien ze slownika
    for cos, costam in swap_candidates.items():
        text = text.replace(cos, costam)
    return text

with open("2.txt", "r") as file:
    text = file.read()
    text = swap_words(text.replace('\n', ' '))

    print(text)

    for letter in text:
        print(letter + " --> " + convert(letter))
