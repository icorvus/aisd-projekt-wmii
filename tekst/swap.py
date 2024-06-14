def swap_words(text):
    # to nie dziala, trzeba poprawic
    swap_candidates = {"poli": "boli", "\n": " "}
    # zamiana wystapien ze slownika
    for key in swap_candidates.keys():
        text_fixed = text.strip().replace(key, swap_candidates[key])
    return text_fixed
