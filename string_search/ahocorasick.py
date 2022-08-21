import ahocorasick

def using_ahocorasick(full_vals, matching_phrase): # using ahocorasick library - https://pypi.org/project/pyahocorasick/ (Fast / memory efficient substring search in Python)
    A = ahocorasick.Automaton(ahocorasick.STORE_INTS) # create ahocorasick automaton object 
    A.add_word(matching_phrase) # add matching phrase to the automaton
    A.make_automaton() # build the automaton
    mask = full_vals.apply(lambda x: bool(list(A.iter(x)))) # check if any of the words in the full_vals column match the matching_phrase
    return mask